# Mutual Fund Analytics

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

A professional mutual fund analytics engine and pipeline designed to ingest, process, and analyze complex financial datasets. The project supports retrieving real-time Net Asset Values (NAV), parsing historical performance, examining portfolio holdings, and tracking investor inflows/transactions to extract actionable investment insights.

Perfect for portfolios, internship applications, or financial analysis showcases.

---

## 🚀 Features

*   **Real-time Data Fetching**: Interactive API client (`live_nav_fetch.py`) fetching real-time NAVs directly from public mutual fund APIs (`mfapi.in`).
*   **Robust Data Ingestion**: Scripted batch ingestion (`data_ingestion.py`) parsing raw financial structures and printing summary metadata (shape, preview, schema diagnostics).
*   **Structured Data Storage**: Clear separation between `raw` and `processed` transactional and index datasets.
*   **Enterprise Directory Layout**: Scalable folder structure ready for analytical notebooks, database schemas (SQL), report exports, and interactive frontend dashboards.

---

## 🛠️ Tech Stack

*   **Core**: Python 3.8+
*   **Data Processing**: Pandas
*   **HTTP Clients**: Requests
*   **Target Environments**: Git, GitHub, Local Virtual Environments (`venv`)

---

## 📂 Project Directory Structure

```text
MutualFundAnalytics/
│
├── Submission_Day1/        # Day 1 milestone verification & execution screenshots
│   ├── Screenshot (99).png
│   ├── Screenshot (100).png
│   └── Screenshot (101).png
│
├── data/                   # Data Storage Directory (Standard git-ignored raw files)
│   ├── raw/                # Original, unaltered CSVs & JSON API responses
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   ├── 03_aum_by_fund_house.csv
│   │   ├── 04_monthly_sip_inflows.csv
│   │   ├── 05_category_inflows.csv
│   │   ├── 06_industry_folio_count.csv
│   │   ├── 07_scheme_performance.csv
│   │   ├── 08_investor_transactions.csv
│   │   ├── 09_portfolio_holdings.csv
│   │   ├── 10_benchmark_indices.csv
│   │   └── nav_data.json
│   └── processed/          # Cleaned & normalized data (ready for analysis)
│
├── dashboard/              # [Placeholder] Dashboard files (Streamlit / Dash / React)
├── notebooks/              # Jupyter Notebooks for EDA (Exploratory Data Analysis)
├── sql/                    # SQL scripts for database loading, indexes, and queries
├── reports/                # PDF reports and visualization charts exports
│
├── .gitignore              # Professional Git file-exclusion guidelines
├── data_ingestion.py       # Python pipeline for loading & auditing raw datasets
├── live_nav_fetch.py       # Python script to query and cache real-time NAV API data
└── README.md               # Main project documentation (this file)
```

---

## ⚙️ Installation & Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/mutual-fund-analytics.git
cd mutual-fund-analytics
```

### 2. Set Up a Virtual Environment (Recommended)
**On Windows (Command Prompt/PowerShell):**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install pandas requests
```

---

## 💻 Usage Instructions

### Run the Data Ingestion Pipeline
To verify and ingest the local raw CSV files, run:
```bash
python data_ingestion.py
```
This script scans the `data/raw/` directory, checks all CSV schemas, and outputs shapes along with headers for quality control.

### Fetch Live NAV Data
To fetch live NAV data from the API endpoint and store it locally:
```bash
python live_nav_fetch.py
```
This queries the REST endpoint for a sample scheme and generates `data/raw/nav_data.json`.

---

## 📈 Roadmap

- [x] Day 1: Build ingestion scripts and integrate real-time REST APIs.
- [ ] Day 2: Relational database design, SQL schema generation, and bulk loading.
- [ ] Day 3: Analytical SQL queries (KPI calculation, rolling averages, AUM metrics).
- [ ] Day 4: Exploratory analysis using Jupyter Notebooks and visualization libraries (Matplotlib/Seaborn).
- [ ] Day 5: Develop interactive dashboard (Streamlit) for investment visualization.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or additions.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
