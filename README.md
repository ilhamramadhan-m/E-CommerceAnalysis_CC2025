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

## 🛠 Dashboard Steps
### 1️⃣ Install Python (If not already exist)
### 2️⃣ Install Libraries
```
pip install -r requirements.txt
```
### 3️⃣ Clone Repository and navigate to the project directory
```
git clone https://github.com/ilhamramadhan-m/ProjectDataAnalysis-DBS.git
```
### 4️⃣ Set Up Virtual Environment
```
# Install pipenv if not installed
pip install pipenv

# Create and activate virtual environment
pipenv install
pipenv shell
```
### 5️⃣ Select Directory
```
cd ProjectDataAnalysis-DBS/Dashboard
```
### 6️⃣ Run Dashboard
```
streamlit run e-commerce_dashboard.py
```
