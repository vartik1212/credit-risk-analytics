📄 Interactive Project Previews
📑 **[View Full 2-Page Executive Dashboard (PDF)](Loan_default.pdf) **
📥 **[Download Source .pbix Model](https://github.com/vartik1212/credit-risk-analytics/raw/main/Loan_default.pbix)**

Live Dashboard Previews

Page 1: Portfolio Risk and Default Monitoring (Executive View)
Designed for Chief Risk Officers and credit policy committees to evaluate balance sheet exposure, vintage cycles, and macro concentration risk.

![Portfolio Risk Overview](https://github.com/vartik1212/credit-risk-analytics/blob/main/assets/page1.png)

- Portfolio Metrics: Monitors $19.39B in aggregate exposure, $4.18B in realized default losses, and a 19.97% baseline default rate.
- Vintage and Volume Trends: Visualizes loan origination growth alongside historical default rate spikes from 2007 through 2018.
- Two-Dimensional Risk Heatmap: Cross-tabulates Credit Grades (A through G) against Debt-to-Income (DTI) tiers to identify high-loss compounding risk zones.
- Purpose and Geographic Risk: Tracks default probability variances by borrowing intent (small business vs. low-risk personal loans) and regional state-level exposure across the US.

---

Page 2: Credit Underwriting Triage Engine (Operational Queue)
Designed for underwriting leads and credit analysts to automate routine decisions and prioritize ambiguous, capital-heavy files.

![Underwriting Triage](assets/page2_underwriting_triage.png)

- Automated Decision Routing: Classifies incoming pipeline into Auto-Approve, Auto-Decline, and Manual Review streams.
- Borrower Quality Indicators: Dynamic queue-level KPIs showing average DTI (20.29%), average FICO score (691.56), and total capital pending underwriter review ($10.87B).
- Policy Validation Matrix: Verifies clean default separation across risk tiers to prevent adverse selection.
- Prioritized Underwriter Worklist: Interactive loan table providing applicant-level financial markers (income, loan size, FICO, DTI) to expedite credit decisions.

---

Core Business Highlights and Impact

- 43.43% Pipeline Automation: By establishing policy gates for low-risk approvals (Grade A/B with DTI < 20%) and high-risk exclusions (Grade E/F/G or DTI > 35%), the engine automated 43.43% of total loan processing volume[cite: 1].
- Risk Separation: Auto-approved segments maintained default rates below 10%, whereas auto-declined segments captured distressed profiles defaulting at >38%.
- $10.87B Queue Triaged: Channeled 56.57% of ambiguous files into a transparent review backlog displaying critical risk drivers for credit committee sign-off.
- Leverage Trumps Nominal Income: Data modeling reveals that high-earning applicants (> $100k annual income) with elevated DTI (> 35%) default at higher rates than modest earners with controlled debt ratios.

---

System Architecture and Data Flow

[Raw Lending Records (~2.26M rows / 1.6GB CSV)]
                       │
                       ▼ (Python: 50,000-row chunked stream via SQLAlchemy)
[PostgreSQL Database Warehouse]
                       │
                       ▼ (SQL View: Filtering mature lifecycles and feature extraction)
[view_cleaned_loan_risk (1.0M mature completed loans)]
                       │
                       ▼ (Star Schema / Direct DAX Modeling)
[Power BI Analytical Suite]
   ├── Page 1: Executive Portfolio Risk and Vintage Exposure
   └── Page 2: Operational Underwriting Decision Terminal

---

Tech Stack and Methodology

- Database and Warehousing: PostgreSQL[cite: 1]
- Data Engineering (ETL): Python (pandas, SQLAlchemy, psycopg2)[cite: 1]
- Data Modeling and BI: Power BI Desktop, DAX[cite: 1]
- Analytical Techniques: Vintage analysis, cohort risk bucketing, categorical normalization, regular expression parsing[cite: 1]
---
