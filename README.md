# 🌐 MarketAura — Market Intelligence & Startup Launch Platform

> **Live Deployment:** https://market-aura.vercel.app/

**MarketAura** is a real-time competitive intelligence, product benchmarking, and startup launch platform designed for founders, analysts, and emerging challengers. Enter any industry—from **Milk & Dairy** and **Specialty Coffee** to **Smartphones**, **Electric Vehicles**, **E-Commerce**, or **SaaS**—to uncover verified regional or global market leaders, realistic local product pricing, and a practical step-by-step market-entry blueprint.

---

## ⚡ Core Features & Capabilities

### 1. Multi-Query Google API Scraping & Cross-Query Consensus
- **Environment-Managed API Keys (`.env`):** Automatically loads `GOOGLE_API_KEY` / `GEMINI_API_KEY`, `GOOGLE_CSE_ID`, and optional `GROQ_API_KEY` from `.env` (or Vercel Environment Variables) without exposing manual key inputs in the UI.
- **Multi-Query Regional Expansion:** Expands every industry query into multiple regional search queries (e.g., `"milk companies in India"`, `"top milk brands in India market share 2026"`, `"best milk products and prices in India"`) and cross-verifies brand frequency across queries to confirm authentic local leaders.
- **Resilient Multi-Tier Pipeline:** Combines the **Google Custom Search JSON API** (including live image thumbnails), **Google Gemini 2.5 Flash with Google Search Grounding**, an **alternate multi-query web/news scraper**, and curated regional fallback datasets so the platform works seamlessly even when offline or rate-limited.

---

### 2. Region-Specific & Global Intelligence (Globe Picker + GPS + Auto-Currency)
- **Top-Right Globe & Sidebar Region Scope:** Search any country, city, or small local neighborhood (powered by live OpenStreetMap Nominatim autocomplete plus a built-in gazetteer) or click **Use My Current Location (GPS)** to auto-detect your exact region.
- **Automatic Currency Synchronization:** Switching regions automatically updates the display currency across all products and recommendations across 10 currencies with real country flag icons (**INR ₹**, **USD $**, **EUR €**, **GBP £**, **JPY ¥**, **AED**, **SGD S$**, **AUD A$**, **CAD C$**, and **CHF**).
- **Dynamic Regional Re-Ranking:** Searching the same industry across different scopes adapts the competitive landscape—for instance, **Milk** in **India** surfaces *Amul (GCMMF)*, *Mother Dairy*, *Nandini (KMF)*, *Hatsun Agro*, *Parag Milk Foods*, and *Country Delight*, while **Global** surfaces *Groupe Lactalis*, *Nestlé*, *Dairy Farmers of America*, *Danone*, *Arla Foods*, and *Yili Group*.

---

### 3. Corporate Hierarchy (`The Companies Strategies`)
- **Ranked Market Leaders:** Dynamically lists the top industry players ordered by market share and scale for your selected region.
- **PPT-Style Morph Transitions & Terminal Typewriter:** Clicking a card smoothly enlarges it while fading out surrounding cards and typing headlines with a sequential terminal block cursor (`█`).
- **Deep-Dive Company Dossiers:**
  - **Reversed History Timeline:** Vertical chronological timeline ordered with the **latest era at the top**, tracking founding strategy, pivots, and current market posture.
  - **Latest Products Portfolio:** Core active product lines with direct links to official company portals.
  - **Market Value, Share & Trajectory:** Enterprise scale figures, regional share bars, and 4-quarter market share trajectory charts.

---

### 4. Product & Launch Radar (`The Product Reviews`)
- **Industry-Adaptive Categories & Realistic Unit Pricing:** Automatically tailors category filters, photography, and pricing to the searched industry (e.g., *A2 & Organic Fresh*, *Full Cream & Daily Fresh*, and *Toned & Value Pouch* priced around ₹54–₹125/L for Milk; *Flagship*, *Mid-Range Performance*, and *Budget 5G* for Smartphones).
- **Conditional Upcoming Launches:** Displays upcoming release windows only for industries with active launch cycles, automatically hiding the section for everyday staples.
- **Scroll-Triggered Lazy Reveal:** Lower-tier product cards and recommendations animate smoothly into view as you scroll.
- **Aura-Bot Floating Spec Inspector:** Clicking **`>_ Detail & Specs`** summons an animated SVG assistant from a random edge of the screen to type out product specifications followed sequentially by brand positioning—without blurring or locking background scrolling.
- **★ Recommended Market-Entry Product Opportunity:** Recommends an underserved price-to-quality sweet-spot offering calibrated to real industry unit economics.

---

### 5. Startup Launch Studio (`/api/venture-roadmap`)
- Accessible via the full-width button at the bottom of the Sector Command Hub or the left sidebar.
- Written in clear, actionable startup language for founders—letting you configure **Starting Capital Stage**, **Competitive Advantage Focus**, **Go-To-Market Channel**, and a **Custom Startup Goal** to generate:
  - **Custom Executive Launch Strategy**
  - **Strategic Trade-Offs, Competitor Risks & Mitigation Playbook**
  - **18-Month 4-Step Operational Launch Roadmap**
  - **Region-Specific Distributor, Co-Packing, EMS & Supply Chain Partners**
  - **Curated Startup Investors & Venture Capital Directory** with direct portal links

---

### 6. Settings & Data Engine (Split Backend Diagnostics)
Keeps all technical engines cleanly organized inside two separate backend panels in the left sidebar:
- **Information Retrieval (IR) Backend:** Live `.env` connection status (`/api/env-status`), source trust weight ($\alpha$), multi-query expansion toggle, executed regional query log, cross-query verified entities, PageRank/HITS/Spam/Consensus reliability matrix, precision metrics, and inverted index preview.
- **Game Theory (GT) Backend:** $3 \times 3$ Normal-Form Payoff Matrix, Strictly Dominant Strategy & IESDS elimination, Pure Strategy Nash Equilibrium, Pareto Optimality, Two-Person Zero-Sum Mixed-Strategy Linear Programming (LP) solver, Extensive-Form Backward Induction (SPNE), Bayesian Signaling, Repeated Games ($\delta \ge 0.75$), and Evolutionarily Stable Strategies (ESS).

---

## 🏗️ Repository File Structure

```text
Market-Aura/
│
├── api/
│   └── index.py                       # FastAPI serverless backend (/, /api/search, /api/venture-roadmap, /api/env-status)
│
├── data/
│   ├── sample_article.txt             # Sample unstructured market analysis brief
│   └── sample_upload.xml              # Sample semi-structured XML dataset
│
├── modules/
│   ├── __init__.py                    # Python package initializer
│   ├── stage1_ingestion_crawler.py    # Multi-format parser, multi-query regional expansion & Google API crawler
│   ├── stage2_indexer.py              # Preprocessing, inverted, positional & compressed indexes
│   ├── stage3_retrieval.py            # Vector Space Model (TF-IDF), BM25 & semantic search
│   ├── stage4_reliability.py          # PageRank, HITS authority, spam filter & consensus scoring
│   ├── stage5_ranking_qa.py           # Hybrid scoring, extractive QA & evaluation metrics
│   └── stage6_game_theory.py          # Regional/global brand extractor, realistic pricing & GT solvers
│
├── public/
│   └── index.html                     # 3D WebGL frontend, Globe/GPS picker, Startup Launch Studio & Settings
│
├── .env                               # Local API keys (ignored by Git)
├── .gitignore                         # Excludes .env, __pycache__, and virtual environments
├── vercel.json                        # Vercel serverless routing configuration
├── requirements.txt                   # Deployment dependencies
└── README.md                          # Platform documentation
```

---

## 🚀 Local Setup & Development

### 1. Clone the Repository

```bash
git clone https://github.com/arch-ship/Market-Aura.git
cd Market-Aura
```

### 2. Create and Activate a Virtual Environment

```bash
# macOS / Linux
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure `.env` (Recommended for Live Google Search & Grounded AI)

Create a `.env` file in the root directory (excluded from Git via `.gitignore`):

```env
GOOGLE_API_KEY=your_google_ai_studio_or_cloud_api_key
GOOGLE_CSE_ID=your_google_programmable_search_engine_cx_id
# Optional alternative LLM provider:
GROQ_API_KEY=your_groq_api_key
```

*(If no API keys are provided, MarketAura automatically runs using its alternate multi-query web scraper, NLP brand extractor, and regional knowledge base.)*

### 5. Run the Application

```bash
uvicorn api.index:app --reload
```

Open **`http://127.0.0.1:8000`** in your browser.

---

## ☁️ Deployment (Vercel)

The project is deployed at **https://market-aura.vercel.app/**:

1. `vercel.json` routes all `/` and `/api/*` traffic to the FastAPI application in `api/index.py`.
2. Add `GOOGLE_API_KEY` and `GOOGLE_CSE_ID` (and optional `GROQ_API_KEY`) under **Vercel Project Settings → Environment Variables**, then redeploy so the serverless runtime loads the credentials automatically.

---

## 👥 Authors

- **Developers:** Aditya Garg & Ayaz Wasee Al Ansari
- **Institution:** Department of Computer Applications, Jaypee Institute of Information Technology (JIIT), Noida