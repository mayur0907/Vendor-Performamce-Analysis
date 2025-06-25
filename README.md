# 🧾 Vendor Analysis Project

This project aims to perform in-depth analysis on vendor performance and procurement efficiency using data from multiple sources. The goal is to help organizations make better decisions about vendor selection, pricing strategies, and purchase volume.

---

## 📌 Project Objectives

- Analyze vendor purchase behavior
- Identify top-performing vendors based on volume and pricing
- Detect pricing anomalies or inconsistencies
- Provide insights for better procurement decisions

---

## 📂 Folder Structure



Vendor_Analysis_Project/
│
├── data/ # Raw and cleaned datasets
│ ├── vendors.csv
│ ├── purchase_orders.csv
│ └── products.csv
│
├── notebooks/ # Jupyter notebooks for analysis
│ └── vendor_analysis.ipynb
│
├── scripts/ # Python scripts for data ingestion and cleaning
│ └── ingestion_db.py
│
├── output/ # Reports and visualizations
│ └── vendor_summary.xlsx
│
└── README.md # Project documentation



---

## 📊 Tools & Technologies

- **Python** (Pandas, NumPy, Matplotlib, Seaborn)
- **SQL** (for data querying)
- **Jupyter Notebook**
- **Excel / Power BI** (for final reporting)
- **Git** for version control

---

## ⚙️ Key Features

- Aggregates purchase data across vendors
- Calculates total spend, average price, and volume per vendor
- Flags vendors with irregular pricing patterns
- Ranks vendors based on performance KPIs
- Interactive charts for quick insights (in Power BI or Matplotlib)

---

## 🗃️ Sample SQL Query

```sql
SELECT 
    VendorNumber,
    VendorName,
    SUM(PurchasePrice * Quantity) AS TotalSpend,
    AVG(PurchasePrice) AS AvgPrice,
    SUM(Quantity) AS TotalVolume
FROM purchase_orders
GROUP BY VendorNumber, VendorName
ORDER BY TotalSpend DESC;
