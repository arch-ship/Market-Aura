import os
import re
import io
import datetime
import urllib.parse
import xml.etree.ElementTree as ET
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    BeautifulSoup = None

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

try:
    import docx
except ImportError:
    docx = None

try:
    from deep_translator import GoogleTranslator
except ImportError:
    GoogleTranslator = None


def _load_local_env():
    """Loads key=value pairs from root .env into os.environ if not already present."""
    candidates = [
        os.path.join(os.getcwd(), ".env"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".env"),
    ]
    for env_path in candidates:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for raw_line in f:
                        line = raw_line.strip()
                        if not line or line.startswith("#") or "=" not in line:
                            continue
                        k, v = line.split("=", 1)
                        k = k.strip()
                        v = v.strip().strip('"').strip("'")
                        if k and k not in os.environ:
                            os.environ[k] = v
            except Exception:
                pass
            break


_load_local_env()


def _strip_html(raw_html: str) -> str:
    if not raw_html:
        return ""
    if BeautifulSoup is not None:
        try:
            return BeautifulSoup(raw_html, "html.parser").get_text(" ", strip=True)
        except Exception:
            pass
    return re.sub(r"<[^>]+>", " ", raw_html).strip()


class DocumentParser:
    """Ingests .txt, .pdf, .docx, and .xml files into structured document records."""

    @classmethod
    def parse_uploaded_file(cls, filename: str, file_bytes: bytes) -> dict:
        ext = os.path.splitext(filename.lower())[1]
        if ext == ".pdf":
            text = cls._parse_pdf(file_bytes)
        elif ext == ".docx":
            text = cls._parse_docx(file_bytes)
        elif ext == ".xml":
            return cls._parse_xml(filename, file_bytes)
        else:
            text = cls._parse_txt(file_bytes)

        return {
            "id": "USER_UPLOAD_0",
            "title": f"Uploaded Brief: {filename}",
            "source": "user.upload.local",
            "url": "#uploaded-file",
            "date": datetime.date.today().isoformat(),
            "text": text.strip() or f"Uploaded market analysis document: {filename}",
            "outlinks": ["google.com", "reuters.com", "bloomberg.com"]
        }

    @staticmethod
    def _parse_txt(file_bytes: bytes) -> str:
        return file_bytes.decode("utf-8", errors="ignore")

    @staticmethod
    def _parse_pdf(file_bytes: bytes) -> str:
        if not PdfReader:
            return "PDF parser unavailable."
        reader = PdfReader(io.BytesIO(file_bytes))
        pages = [page.extract_text() or "" for page in reader.pages]
        return "\n".join(pages)

    @staticmethod
    def _parse_docx(file_bytes: bytes) -> str:
        if not docx:
            return "DOCX parser unavailable."
        doc = docx.Document(io.BytesIO(file_bytes))
        return "\n".join(p.text for p in doc.paragraphs if p.text)

    @staticmethod
    def _parse_xml(filename: str, file_bytes: bytes) -> dict:
        try:
            root = ET.fromstring(file_bytes.decode("utf-8", errors="ignore"))
            title = root.findtext("title") or f"XML Document: {filename}"
            source = root.findtext("source") or "verified.xml.source"
            date_str = root.findtext("date") or datetime.date.today().isoformat()
            body = root.findtext("body") or ET.tostring(root, encoding="unicode", method="text")
            return {
                "id": "USER_UPLOAD_XML",
                "title": title.strip(),
                "source": source.strip(),
                "url": "#uploaded-xml",
                "date": date_str.strip(),
                "text": body.strip(),
                "outlinks": [source.strip(), "google.com"]
            }
        except Exception:
            return {
                "id": "USER_UPLOAD_XML",
                "title": filename,
                "source": "xml.upload.local",
                "url": "#uploaded-xml",
                "date": datetime.date.today().isoformat(),
                "text": file_bytes.decode("utf-8", errors="ignore")[:2000],
                "outlinks": ["google.com"]
            }


class QueryFormulator:
    """Handles Cross-Language Query Translation and Multi-Query Regional Expansion."""

    STOPWORDS = {
        "the", "and", "for", "with", "that", "this", "from", "into", "over",
        "are", "was", "were", "will", "about", "what", "when", "where", "which"
    }

    @classmethod
    def translate_to_english(cls, text: str) -> str:
        if not text:
            return ""
        # Skip network call for plain ASCII English strings (saves 500ms-1500ms on Vercel!)
        if all(ord(ch) < 128 for ch in text):
            return text
        if GoogleTranslator is not None:
            try:
                return GoogleTranslator(source="auto", target="en").translate(text)
            except Exception:
                return text
        return text

    @classmethod
    def formulate_query_from_input(cls, raw_query: str, uploaded_doc: dict = None) -> str:
        if raw_query and raw_query.strip():
            return cls.translate_to_english(raw_query.strip())
        if uploaded_doc and uploaded_doc.get("text"):
            words = re.findall(r"[a-zA-Z]{4,}", uploaded_doc["text"].lower())
            filtered = [w for w in words if w not in cls.STOPWORDS]
            top_terms = [w for w, _ in Counter(filtered).most_common(6)]
            return " ".join(top_terms) if top_terms else "market strategy analysis"
        return "global industry market strategy"

    @classmethod
    def generate_expanded_regional_queries(cls, base_query: str, region: str) -> list:
        q = base_query.strip()
        reg = region.strip() if region and region.strip() else "India"
        if reg.lower() in ["global", "worldwide", "world"]:
            return [
                f"{q} companies",
                f"top {q} companies worldwide market share 2026",
                f"largest {q} brands globally by revenue",
                f"popular {q} products prices globally"
            ]
        return [
            f"{q} companies in {reg}",
            f"top {q} brands in {reg} market share 2026",
            f"largest {q} companies {reg}",
            f"best {q} products and prices in {reg}"
        ]


class WebAndSocialCrawler:
    """
    Parallelized Multi-Query Google Custom Search JSON API + Google Gemini Search Grounding +
    Alternate Multi-Query Web/News Scraper.
    Runs concurrent HTTP calls so serverless execution stays fast (~2-3s total).
    """

    @staticmethod
    def _fetch_google_cse_single(api_key: str, cse_id: str, eq: str, q_idx: int, query: str, today_str: str) -> list:
        out = []
        try:
            params = {"key": api_key, "cx": cse_id, "q": eq, "num": 4}
            resp = requests.get("https://www.googleapis.com/customsearch/v1", params=params, timeout=2.5)
            if resp.status_code == 200:
                items = resp.json().get("items", [])
                for idx, item in enumerate(items):
                    link = item.get("link", "https://www.google.com")
                    domain = urllib.parse.urlparse(link).netloc.replace("www.", "") or "google.com"
                    pagemap = item.get("pagemap", {})
                    cse_imgs = pagemap.get("cse_image") or pagemap.get("cse_thumbnail") or []
                    img_url = cse_imgs[0].get("src", "") if cse_imgs and isinstance(cse_imgs[0], dict) else ""
                    out.append({
                        "id": f"GOOGLE_CSE_{q_idx}_{idx}",
                        "title": item.get("title", f"{query} Market Report"),
                        "source": domain,
                        "url": link,
                        "image_url": img_url,
                        "date": today_str,
                        "text": item.get("snippet", ""),
                        "expanded_query_used": eq,
                        "scraper_engine": "Google Custom Search JSON API",
                        "outlinks": [domain, "google.com", "reuters.com"]
                    })
        except Exception:
            pass
        return out

    @staticmethod
    def _fetch_news_rss_single(eq: str, q_idx: int, hl_gl: str, query: str, today_str: str) -> list:
        out = []
        try:
            q_enc = urllib.parse.quote(eq)
            rss_url = f"https://news.google.com/rss/search?q={q_enc}&hl={hl_gl}"
            resp = requests.get(
                rss_url,
                headers={"User-Agent": "Mozilla/5.0 (compatible; MarketAuraBot/5.0)"},
                timeout=2.2
            )
            if resp.status_code == 200:
                root = ET.fromstring(resp.content)
                channel = root.find("channel")
                if channel is not None:
                    for idx, item in enumerate(channel.findall("item")[:3]):
                        title = item.findtext("title") or f"{query} Market Update"
                        link = item.findtext("link") or f"https://www.google.com/search?q={q_enc}"
                        source_el = item.find("source")
                        source_url = source_el.attrib.get("url", "https://news.google.com") if source_el is not None else "https://news.google.com"
                        source_domain = urllib.parse.urlparse(source_url).netloc.replace("www.", "") or "news.google.com"
                        raw_desc = item.findtext("description") or title
                        clean_desc = _strip_html(raw_desc)
                        out.append({
                            "id": f"ALT_NEWS_{q_idx}_{idx}",
                            "title": title,
                            "source": source_domain,
                            "url": link,
                            "image_url": "",
                            "date": today_str,
                            "text": clean_desc[:360] if clean_desc else title,
                            "expanded_query_used": eq,
                            "scraper_engine": "Alternate Multi-Query Web News Scraper",
                            "outlinks": [source_domain, "google.com"]
                        })
        except Exception:
            pass
        return out

    @classmethod
    def crawl_live_web(
        cls,
        query: str,
        max_results: int = 12,
        region: str = "India"
    ) -> list:
        _load_local_env()
        api_key = (os.environ.get("GOOGLE_API_KEY") or os.environ.get("GEMINI_API_KEY") or "").strip()
        cse_id = (os.environ.get("GOOGLE_CSE_ID") or "").strip()

        expanded_queries = QueryFormulator.generate_expanded_regional_queries(query, region)
        results = []
        today_str = datetime.date.today().isoformat()

        # TIER 1: PARALLEL GOOGLE CUSTOM SEARCH JSON API
        if api_key and cse_id:
            with ThreadPoolExecutor(max_workers=4) as executor:
                futures = [
                    executor.submit(cls._fetch_google_cse_single, api_key, cse_id, eq, q_idx, query, today_str)
                    for q_idx, eq in enumerate(expanded_queries[:4])
                ]
                for fut in as_completed(futures):
                    try:
                        results.extend(fut.result())
                    except Exception:
                        pass

        # TIER 2: GOOGLE GEMINI SEARCH GROUNDING (if CSE wasn't configured or returned few hits)
        if len(results) < 5 and api_key and api_key.startswith("AIza"):
            try:
                gemini_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={urllib.parse.quote(api_key)}"
                payload = {
                    "contents": [{
                        "parts": [{
                            "text": (
                                f"Using Google Search, identify the top 5 real companies, their market share or revenue, "
                                f"and popular real consumer products with realistic unit prices for '{query}' specifically in '{region}' (2026)."
                            )
                        }]
                    }],
                    "tools": [{"google_search": {}}]
                }
                resp = requests.post(gemini_url, json=payload, timeout=3.8)
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        grounded_text = " ".join(p.get("text", "") for p in parts if "text" in p).strip()
                        grounding_chunks = (
                            candidates[0].get("groundingMetadata", {}).get("groundingChunks", [])
                        )
                        for idx, chunk in enumerate(grounding_chunks[:max_results]):
                            web_info = chunk.get("web", {})
                            uri = web_info.get("uri", "https://www.google.com")
                            title = web_info.get("title", f"Google Grounded Source #{idx+1}")
                            domain = urllib.parse.urlparse(uri).netloc.replace("www.", "") or "google.com"
                            results.append({
                                "id": f"GOOGLE_GROUNDED_{idx}",
                                "title": title,
                                "source": domain,
                                "url": uri,
                                "image_url": "",
                                "date": today_str,
                                "text": grounded_text[:450] if grounded_text else f"Google Search Grounded data for {query} in {region}.",
                                "expanded_query_used": expanded_queries[0],
                                "scraper_engine": "Google Gemini Search Grounding API",
                                "outlinks": [domain, "google.com"]
                            })
                        if not grounding_chunks and grounded_text:
                            results.append({
                                "id": "GOOGLE_GROUNDED_MAIN",
                                "title": f"Google Grounded Intelligence: {query} ({region})",
                                "source": "google.com",
                                "url": f"https://www.google.com/search?q={urllib.parse.quote(expanded_queries[0])}",
                                "image_url": "",
                                "date": today_str,
                                "text": grounded_text[:520],
                                "expanded_query_used": expanded_queries[0],
                                "scraper_engine": "Google Gemini Search Grounding API",
                                "outlinks": ["google.com", "reuters.com"]
                            })
            except Exception:
                pass

        # TIER 3: PARALLEL ALTERNATE MULTI-QUERY NEWS RSS SCRAPER
        if len(results) < max_results:
            is_india = any(
                city in region.lower()
                for city in [
                    "india", "delhi", "mumbai", "bengaluru", "bangalore", "noida",
                    "ghaziabad", "gurugram", "gurgaon", "hyderabad", "chennai",
                    "pune", "kolkata", "gujarat", "maharashtra", "karnataka"
                ]
            )
            hl_gl = "en-IN&gl=IN&ceid=IN:en" if is_india else "en-US&gl=US&ceid=US:en"
            with ThreadPoolExecutor(max_workers=3) as executor:
                futures = [
                    executor.submit(cls._fetch_news_rss_single, eq, q_idx, hl_gl, query, today_str)
                    for q_idx, eq in enumerate(expanded_queries[:3])
                ]
                for fut in as_completed(futures):
                    try:
                        results.extend(fut.result())
                    except Exception:
                        pass

        return results[:max_results]
