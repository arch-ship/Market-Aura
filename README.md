# 🌐 MarketAura

> **Live Deployment:** https://market-aura.vercel.app/

Accessible via the production URL in the repository description above.

**MarketAura** is an autonomous market intelligence, corporate strategy, and quantitative game theory decision platform. By analyzing live competitive landscapes, product releases, and market share hierarchies, MarketAura computes mathematically optimal entry playbooks and product blueprints that allow new entrants to carve out profitable positions without getting trapped in destructive price wars.

---

## ⚡ Core Features & Capabilities

### 1. Dual-Engine Real-World Data Verification
* **Engine A (Zero-Key Live Web & Encyclopedia Scraper):** Scrapes live web endpoints, corporate filings, and Wikipedia knowledge graphs in real time to extract current brand market shares, product releases, and strategic shifts.
* **Engine B (Autonomous Strategic Knowledge Engine):** Connects with live AI synthesis APIs (Groq / Gemini) when configured, or deploys deterministic game-theoretic modeling.
* **Dual-Source Consensus Scoring:** Cross-verifies data points between both engines to establish high-confidence market metrics and reliability scores.

---

### 2. Module 01 // The Companies Strategies
* **Top-10 Corporate Hierarchy:** Dynamically ranks the industry's top players in descending order of market share and total enterprise valuation.
* **PPT-Style Morph Transition:** Clicking a company card smoothly enlarges it while fading out background rows, taking over the viewport with an interactive terminal interface.
* **Deep-Dive Company Dossiers:**
  * **Reversed History & Strategic Pivots:** Vertical chronological timeline organized with the **latest era at the top** to trace business model evolutions from inception to the present.
  * **Latest Products Portfolio:** Active flagship and core product offerings with direct links to official corporate portals.
  * **Market Value, Share & Trajectory:** Enterprise capitalization figures, overall segment control, and a 4-quarter market share performance bar chart.

---

### 3. Module 02 // The Product Reviews & Launch Radar
* **Pre-Launch Pipeline Radar:** Upcoming flagship and disruptor products with projected launch dates, technical specs, and pre-emptive signaling strategies.
* **Tiered Market Catalog:** Active products categorized into **Ultra-Premium Flagship**, **Mid-Range Disruptor**, and **Value / Entry Tier**.
* **Scroll-Triggered Lazy Reveal:** Lower-tier cards and deep analyses load smoothly as you scroll into their viewport.
* **Multi-Currency Engine with Real Flag Icons:** Live price formatting defaulting to **INR (₹)** with an interactive country-flag switcher supporting USD ($), EUR (€), GBP (£), JPY (¥), AED (د.إ), SGD (S$), AUD (A$), CAD (C$), and CHF (Fr).
* **Aura-Bot Floating Spec Inspector:** An animated SVG Cyber-Quant bot that flies in randomly from any edge of the screen to project specifications without blurring or freezing background navigation.
* **★ Market-Boom Product Blueprint:** Recommends the exact price point, spec sheet, and value proposition guaranteed by Backward Induction to capture market share without provoking incumbent price wars.

---

### 4. Mathematical Game Theory Solvers
* **Normal-Form Payoff Matrices:** Models 3×3 non-cooperative games between entrants and incumbents.
* **Dominance & IESDS:** Identifies strictly dominant strategies and eliminates dominated actions (such as head-on price wars) using Iterated Elimination of Strictly Dominated Strategies.
* **Nash Equilibrium & Pareto Optimality:** Calculates pure strategy equilibria and identifies Pareto-efficient co-opetition outcomes.
* **Zero-Sum Games & Mixed-Strategy Optimization:** Formulates two-person zero-sum marketing games, calculating Maximin, Minimax, Saddle Points, and Linear Programming (LP) probability distributions.
* **Extensive-Form Game Trees (Backward Induction):** Proves Subgame Perfect Nash Equilibria (SPNE) where rational incumbents accommodate focused niche entrants to protect core margins.
* **Advanced Models:** Incorporates Bayesian Incomplete-Information games, Costly Quality Signaling, Repeated Games ($\delta \ge 0.75$), Evolutionarily Stable Strategies (ESS), and Vickrey Second-Price mechanism design.

---

### 5. Settings & Background Engine
* Segregates background web extraction diagnostics, source authority parameters, query expansion controls, and reliability matrices inside a dedicated settings panel to keep the primary tactical workspace clean and focused.

---

## 🏗️ Repository File Structure

```text
MarketAura/
│
├── api/
│   └── index.py                       # FastAPI serverless backend entry point
│
├── data/
│   ├── sample_article.txt             # Sample industry analysis document
│   └── sample_upload.xml              # Sample semi-structured XML dataset
│
├── modules/
│   ├── __init__.py                    # Python package initializer
│   ├── stage1_ingestion_crawler.py    # Multi-format parser, web crawler & CLIR
│   ├── stage2_indexer.py              # Inverted, positional, and compressed indexer
│   ├── stage3_retrieval.py            # Vector Space Model, BM25 & semantic search
│   ├── stage4_reliability.py          # PageRank, HITS, spam classification & clustering
│   ├── stage5_ranking_qa.py           # Hybrid scoring, QA extraction & evaluation
│   └── stage6_game_theory.py          # MarketAura game theory & product intelligence engine
│
├── public/
│   └── index.html                     # Interactive 3D WebGL frontend terminal
│
├── .gitignore                         # Excludes cache, virtual environments, and secrets
├── vercel.json                        # Vercel serverless routing configuration
├── requirements.txt                   # Deployment dependencies
└── README.md                          # Platform documentation

```

---

## 🚀 Local Setup & Development

### 1. Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/MarketAura.git
cd MarketAura

```

### 2. Create and Activate a Virtual Environment

```bash
# macOS/Linux
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

### 4. Optional: Configure Live LLM API Keys

Create a `.env` file in the root folder if you wish to enable Option B external API synthesis:

```env
GROQ_API_KEY=your_groq_api_key_here
# or
GEMINI_API_KEY=your_gemini_api_key_here

```

*(If no API key is provided, MarketAura runs in autonomous mode with internal consensus validation).*

### 5. Run the Application

```bash
uvicorn api.index:app --reload

```

Open **`http://127.0.0.1:8000`** in your browser.

---

## ☁️ Deployment (Vercel)

The project is configured for direct deployment on Vercel:

1. `vercel.json` rewrites all incoming traffic to `api/index.py`.
2. Vercel provisions the Python runtime as a serverless function while serving `public/index.html` as the interactive client.
3. Access the live platform via the production link pinned in the repository description.

---

## 👥 Authors

* **Developers:** Aditya Garg & Ayaz Wasee Al Ansari
* **Institution:** Department of Computer Applications, Jaypee Institute of Information Technology (JIIT), Noida

```

```
