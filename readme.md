# 🍬 Factory-to-Customer Shipping Route Efficiency Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analytics-150458?style=for-the-badge\&logo=pandas)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge\&logo=plotly)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### Transforming logistics data into actionable shipping intelligence.

An interactive Streamlit dashboard that analyzes factory-to-customer shipping performance, identifies delivery bottlenecks, evaluates shipping routes, and provides operational insights for **Nassau Candy Distributor**.

</div>

---

## 📖 Overview

Efficient logistics is one of the most important factors affecting customer satisfaction, operational costs, and business scalability. While organizations collect massive amounts of shipment data, valuable insights often remain hidden inside spreadsheets.

This project converts raw shipment records into meaningful operational intelligence by analyzing:

* Factory → Customer shipping routes
* Shipping lead times
* Route efficiency
* Geographic bottlenecks
* Regional logistics performance
* Ship mode comparisons
* Delivery delays
* Interactive KPIs

The result is a business intelligence dashboard that helps logistics managers understand where deliveries perform well and where improvements are needed.

---

# ✨ Features

### 📊 Interactive Dashboard

* Executive KPI cards
* Dynamic charts
* Interactive filtering
* Route performance leaderboard
* Order-level drill-down

### 🚚 Route Efficiency Analysis

* Average lead time
* Route volume
* Fastest shipping routes
* Slowest shipping routes
* Route efficiency score

### 🗺 Geographic Intelligence

* Regional performance
* State-wise shipping analysis
* Factory locations
* Geographic bottleneck identification

### 🚛 Ship Mode Comparison

Compare different shipping methods based on:

* Delivery speed
* Delay frequency
* Average lead time
* Shipment volume

### 📈 Business KPIs

* Total Shipments
* Total Sales
* Gross Profit
* Total Units
* Average Shipping Lead Time
* Delay Percentage
* Route Efficiency Score

---

# 📂 Dataset

The dataset contains shipment records including:

* Order ID
* Order Date
* Ship Date
* Customer Location
* Region
* State
* Ship Mode
* Product Information
* Factory Assignment
* Sales
* Cost
* Gross Profit
* Units

Additional factory coordinates are used for geographic analysis.

---

# 🏭 Factory Network

| Factory           | Products                                                     |
| ----------------- | ------------------------------------------------------------ |
| Lot's O' Nuts     | Nutty Crunch, Fudge Mallows, Scrumdiddlyumptious             |
| Wicked Choccy's   | Milk Chocolate, Triple Dazzle Caramel                        |
| Sugar Shack       | Laffy Taffy, Nerds, Fun Dip, SweeTARTS, Fizzy Lifting Drinks |
| Secret Factory    | Gobstopper, Wonka Gum, Lickable Wallpaper                    |
| The Other Factory | Hair Toffee, Kazookles                                       |

---

# ⚙ Data Processing Pipeline

```
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
Date Validation
      │
      ▼
Lead Time Calculation
      │
      ▼
Factory Assignment
      │
      ▼
Route Creation
      │
      ▼
Feature Engineering
      │
      ▼
KPI Generation
      │
      ▼
Visual Analytics Dashboard
```

---

# 🧠 Feature Engineering

The analytics engine creates several derived metrics including:

* Shipping Lead Time
* Delay Flag
* Factory Assignment
* Route Identifier
* Factory → Region
* Factory → State
* Route Volume
* Route Efficiency Score
* Delay Frequency

---

# 📊 Dashboard Modules

## 🏠 Overview

* KPI Summary
* Shipment Statistics
* Executive Overview
* Performance Snapshot

---

## 🚚 Route Efficiency

* Fastest Routes
* Slowest Routes
* Average Lead Time
* Route Ranking

---

## 🗺 Geographic Analysis

* Regional Performance
* State Performance
* Geographic Bottlenecks
* Factory Distribution

---

## 🚛 Ship Mode Analysis

Compare:

* Standard Class
* Second Class
* First Class
* Same Day

Metrics include:

* Average Lead Time
* Delay Rate
* Shipment Count

---

## 🔎 Route Drill Down

Users can explore:

* Individual routes
* Shipment history
* State-level performance
* Order-level records

---

# 🎛 Interactive Filters

Users can filter the dashboard by:

* Date Range
* Region
* State
* Ship Mode
* Lead Time Threshold
* Factory

---

# 📈 Key Performance Indicators

* Average Shipping Lead Time
* Route Efficiency Score
* Total Shipments
* Delay Frequency
* Total Sales
* Gross Profit
* Total Units
* Highest Performing Route
* Lowest Performing Route

---

# 🛠 Technology Stack

* Python
* Streamlit
* Pandas
* NumPy
* Plotly
* OpenPyXL

---

# 📁 Project Structure

```
Factory-Route-Efficiency-Analysis/

│── app.py
│── engine.py
│── requirements.txt
│── data.csv
│── README.md
│── .gitattributes
│── .gitignore
```

---

# 🚀 Getting Started

Clone the repository

```bash
git clone https://github.com/yourusername/factory-route-efficiency-analysis.git
```

Move into the project

```bash
cd factory-route-efficiency-analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Launch the application

```bash
streamlit run app.py
```

---

# 📌 Project Objectives

* Improve logistics visibility
* Reduce shipping delays
* Identify inefficient routes
* Support data-driven operational decisions
* Enhance nationwide delivery performance

---

# 💡 Future Improvements

* Real-time shipment monitoring
* Predictive delivery delay models
* Machine learning route optimization
* Cost optimization analysis
* Weather integration
* Live logistics API support

---

# 🎓 Academic Purpose

This project was developed as a logistics analytics and business intelligence case study demonstrating practical applications of:

* Data Cleaning
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Interactive Dashboard Development
* Logistics Analytics
* Geographic Visualization
* Business Intelligence

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Built with ❤️ using Python & Streamlit

</div>
