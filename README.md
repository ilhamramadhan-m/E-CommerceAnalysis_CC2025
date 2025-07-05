
# 🛒 Interactive Analytics of E-Commerce Transactions

## 📌 Project Overview
This project presents an interactive data analysis of a public e-commerce dataset from Brazil, integrating customer, order, product, and review data. The goal is to uncover insights on customer behavior, payment trends, delivery performance, seller distribution, and the relationship between pricing and satisfaction — all through a dynamic dashboard built using **Streamlit**.

## 🗂️ Dataset Overview
Data used in this project comes from a multi-table e-commerce dataset, which includes:
- Customer information
- Product metadata (category, price)
- Order timelines and delivery estimates
- Review scores and payment methods
- Seller details and location

🔗 Source: [Brazilian E-Commerce Public Dataset](https://www.kaggle.com/olistbr/brazilian-ecommerce)

## 📊 Key Features & Dashboard Insights
The dashboard allows users to:
- Filter by **purchase date range** and **payment type**
- View **monthly comparisons** of total sales, orders, and review scores
- Analyze **delivery efficiency** (on-time, early, or late)
- Understand **price vs review correlations**
- Explore **review score distributions by product price category**
- Identify **top cities by customer and seller counts**

## 📁 Directory Structure
```

ProjectDataAnalysis-DBS/
│── Dashboard/
│   ├── e-commerce\_dashboard.py
│   ├── e-commerce\_dataset.csv 
│
│── Data/ 
│   ├── customer\_dataset.csv
│   ├── geolocation\_dataset.7z
│   ├── order\_items\_dataset.csv
│   ├── order\_payments\_dataset.csv
│   ├── order\_reviews\_dataset.csv
│   ├── orders\_dataset.csv
│   ├── product\_category\_name\_translation.csv
│   ├── products\_dataset.csv
│   ├── sellers\_dataset.csv
│
│── e-commerce\_analysis.ipynb 
│── requirements.txt      
│── url.txt 
│── README.md

````

## 🚀 How to Run the Dashboard
Follow the steps below to set up and run the Streamlit dashboard locally.

### 1️⃣ Install Python (if not already installed)

### 2️⃣ Install Required Libraries
```bash
pip install -r requirements.txt
````

### 3️⃣ Clone the Repository

```bash
git clone https://github.com/ilhamramadhan-m/ProjectDataAnalysis-DBS.git
```

### 4️⃣ Create & Activate Virtual Environment

```bash
# Install pipenv (if not installed)
pip install pipenv

# Create and activate environment
pipenv install
pipenv shell
```

### 5️⃣ Navigate to the Dashboard Folder

```bash
cd ProjectDataAnalysis-DBS/Dashboard
```

### 6️⃣ Launch the Dashboard

```bash
streamlit run e-commerce_dashboard.py
```
