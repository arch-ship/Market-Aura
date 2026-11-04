# Market-Aura
Market exploration and Strategic discovery.

An interactive **Game Theory & Strategic Market Intelligence System** powered by a live **5-Stage Information Retrieval (IR) Pipeline**. 

When a user enters any interest industry (e.g., *Cloud Computing*, *Artificial Intelligence*, *Smartphones*, *E-Commerce*, or any custom domain), the system crawls and verifies live web intelligence to generate:
1. **🏆 Top-Tier Incumbent Brands & ⚡ Middle/Low-End Challengers:** Live market share, current status, and active strategic posture.
2. **🚀 Immediate Actionable Entry Strategy (Zero Extensive Research Required):** A 4-step *Judo Strategy & Ecosystem Co-opetition Playbook* that a new entrant can execute immediately to carve out a profitable position without getting crushed in a price war.
3. **📊 Interactive Game Theory Mathematical Models (Modules 1–5):** Full computational breakdown of Normal-Form Payoff Matrices, Dominant Strategies, IESDS, Pure Strategy Nash Equilibrium, Pareto Optimality, Two-Person Zero-Sum Maximin/Minimax & Mixed-Strategy Linear Programming, Extensive-Form Backward Induction (Subgame Perfect Equilibrium), Bayesian Signaling, Repeated Games ($\delta$), Evolutionarily Stable Strategies (ESS), and Vickrey Auctions.

---

## 📚 Course Syllabus Mapping (`23B61CA412 / C402 — Game Theory`)

| Syllabus Module | Implemented Mathematical Models & Features (`modules/stage6_game_theory.py`) |
| :--- | :--- |
| **Module 1: Introduction & Strategic Decision Making** | Players (Top Incumbents, Mid/Low-Tier Challengers, New User Entrant), Actions & Strategies, Utility/Payoff Functions, Cooperative vs. Non-Cooperative, Simultaneous vs. Sequential, Complete vs. Incomplete Information. |
| **Module 2: Strategic Games & Nash Equilibrium** | $3 \times 3$ Normal-Form Payoff Matrix, Strictly Dominant & Dominated Strategies, Iterated Elimination of Strictly Dominated Strategies (IESDS), Best Response Analysis, Pure Strategy Nash Equilibrium, Pareto Optimality, and Classic Game Archetypes (*Prisoner's Dilemma*, *Stag Hunt*, *Coordination Game*). |
| **Module 3: Zero-Sum Games & Optimization** | Two-Person Zero-Sum Market Attention Game, Maximin (Lower Value) & Minimax (Upper Value) Criteria, Saddle Point Detection, Analytical Mixed-Strategy Probabilities, and Linear Programming (LP) Formulation. |
| **Module 4: Advanced Game Theory Models** | Extensive-Form Game Tree solved via **Backward Induction** (Subgame Perfect Nash Equilibrium), **Bayesian Games** (Incomplete Information on Competitor Cost Types), **Signaling Games**, **Repeated Games** (*Generous Tit-for-Tat*), **Evolutionarily Stable Strategy (ESS)**, and **Mechanism Design** (*Vickrey Second-Price Auction*). |
| **Module 5: Applications in Computing & Business** | Multi-Agent Resource Allocation, Multi-Cloud Spot Load Balancing, Algorithmic Bidding, and Strategic Decision Support Systems. |

---

## 🏗️ Repository File Structure

```text
├── api/
│   └── index.py                       # FastAPI Serverless Backend (IR + Game Theory Engine)
├── data/
│   ├── sample_upload.xml              # Sample semi-structured XML file for upload testing
│   └── sample_article.txt             # Sample text file for upload testing
├── modules/
│   ├── __init__.py                    # Python package initializer
│   ├── stage1_ingestion_crawler.py    # Multi-format file parser, CLIR & Live Web Crawler
│   ├── stage2_indexer.py              # Tokenization, Stemming, Inverted, Positional & n-gram Indexes
│   ├── stage3_retrieval.py            # VSM (TF-IDF), Okapi BM25, LSA Semantic & Personalized Search
│   ├── stage4_reliability.py          # PageRank, HITS, Naive Bayes Spam Filter & K-Means Clustering
│   ├── stage5_ranking_qa.py           # Hybrid Credence Ranking, Extractive QA & IR Evaluation Metrics
│   └── stage6_game_theory.py          # Game Theory Brand & Market Strategy Engine (Modules 1-5)
├── public/
│   └── index.html                     # Frontend UI (Game Theory Dashboard + 5 IR Verification Tabs)
├── .gitignore                         # Git ignore rules
├── vercel.json                        # Vercel Serverless deployment routing
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository
```bash
git clone [https://github.com/](https://github.com/)<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the FastAPI + Web Interface Locally
```bash
uvicorn api.index:app --reload
```
Open **http://127.0.0.1:8000** in your browser.

### 4. Run Individual Stages in Terminal (For Viva / CLI Verification)
You can test the Game Theory engine or any Information Retrieval stage independently from the root directory:
```bash
python -m modules.stage6_game_theory
python -m modules.stage1_ingestion_crawler
python -m modules.stage2_indexer
python -m modules.stage3_retrieval
python -m modules.stage4_reliability
python -m modules.stage5_ranking_qa
```

---

## ☁️ Deploying to Vercel

1. Push this repository to your GitHub account.
2. Go to [Vercel](https://vercel.com/new) and import your repository.
3. Leave the build settings at default—Vercel automatically reads `vercel.json` and builds the Python Serverless Function (`api/index.py`).
4. Click **Deploy** to generate your live production URL.

---

## 👥 Authors & Academic Context

* **Course:** Game Theory (`23B61CA412 / C402`) & Information Retrieval (`23B61CA414 / CBAC405`)
* **Institution:** Department of Computer Applications, Jaypee Institute of Information Technology (JIIT), Noida
* **Developers:** Aditya Garg & Ayaz Wasee Al Ansari