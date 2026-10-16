## 📄 Interactive Project Previews
* 📑 **[View Full 2-Page Executive Dashboard (PDF)] **
* 📥 **[Download Source .pbix Model](https://github.com/vartik1212/credit-risk-analytics/raw/main/Loan_default.pbix)**

\# 🏦 Retail Credit Risk Analytics \& Automated Underwriting Engine



An end-to-end business intelligence system evaluating \*\*$19.39B in retail credit exposure\*\* across 1M mature loans. Features a chunked PostgreSQL ETL pipeline, custom DAX risk matrices, and a dual-perspective Power BI application.



\---



\## 📊 Live Dashboard Previews



\### Page 1: Portfolio Risk \& Default Monitoring (Executive View)

!\[Portfolio Risk Overview](assets/page1\_portfolio\_overview.png)



\### Page 2: Credit Underwriting Engine (Operational Queue)

!\[Underwriting Triage](assets/page2\_underwriting\_triage.png)



\---



\## ⚡ Core Business Highlights

\* \*\*Automated Decisioning:\*\* Safely automated \*\*43.43%\*\* of decisions (31.39% auto-approved at <10% default, 12.04% auto-declined at >38% default).

\* \*\*Underwriter Prioritization:\*\* Triaged \*\*$10.87B in pending capital\*\* to a prioritized queue showing applicant DTI, FICO, and purpose.

\* \*\*Key Finding:\*\* Leverage trumps income—borrowers earning >$100k with DTI >35% default at higher rates than modest earners with DTI <15%.



\---



\## 🛠️ Architecture \& Tech Stack

\* \*\*Storage \& Modeling:\*\* PostgreSQL, SQL (`view\_cleaned\_loan\_risk`)

\* \*\*Pipeline:\*\* Python (`pandas`, `SQLAlchemy`)

\* \*\*Analytics \& UI:\*\* Power BI Desktop, DAX

