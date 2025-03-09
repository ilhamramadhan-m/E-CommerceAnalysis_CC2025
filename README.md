# 🛒 E-Commerce Analysis

## 📌 Project Description
This project analyzed public e-commerce datasets to gain insights into customer behavior patterns, seller distribution, product sales, and payment trends. The analysis involved integrating multiple tables, exploratory data analysis (EDA), and data visualization to support data-driven decision making.

## 📂 Directory Structure
```
ProjectDataAnalysis-DBS/
│── Dashboard/
│   ├── e-commerce_dashboard.py
│   ├── e-commerce_dataset.csv
│── Data/
│   ├── customer_dataset.csv
│   ├── geolocation_dataset.7z
│   ├── order_items_dataset.csv
│   ├── order_payments_dataset.csv
│   ├── order_reviews_dataset.csv
│   ├── orders_dataset.csv
│   ├── product_category_name_translation.csv
│   ├── products_dataset.csv
│   ├── sellers_dataset.csv
│── README.md
│── e-commerce_analysis.ipynb
│── requirements.txt
│── url.txt
```

## 🛠 Steps
### 1️⃣ Setup Environment
- Install Python (If not already exist)
- Check the Python version to make sure it is installed
```
python --version
```
- Clone Repository and navigate to the project directory
```
git clone https://github.com/ilhamramadhan-m/ProjectDataAnalysis-DBS
cd ProjectDataAnalysis-DBS/Dashboard
```
- Install Libraries
```
pip install -r requirements.txt
```

### 2️⃣ Data Wrangling
- **Gathering Data**: Importing an e-commerce dataset consisting of several tables such as customers, orders, payments, and products.
- **Assessing Data**: Checking data types, missing values, and inconsistencies in the dataset.
- **Data Cleaning**: Removes duplicate data, handles missing values, and adjusts data formats (such as date conversion).
### 3️⃣ Exploratory Data Analysis (EDA)
Analyze the data in each table and visualize it to gain insight and evaluate it.
### 4️⃣ Data Integration
Merge multiple tables to get the main dataset.
### 5️⃣ Dashboard with Streamlit
```
streamlit run Dashboard/e-commerce_dashboard.py
```
