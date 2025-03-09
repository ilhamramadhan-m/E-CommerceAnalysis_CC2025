# import library
import streamlit as st
import pandas as pd
import plotly.express as px

# load dataset
df = pd.read_csv("Dashboard/e-commerce_dataset.csv", parse_dates=["order_purchase_timestamp"])

# Set page config
st.set_page_config(page_title="E-Commerce Analysis Dashboard", layout="wide")

# memberikan logo pada sidebar dan dashboard
st.sidebar.image("Dashboard/coding_camp_logo.png", use_column_width=True)

# membuat header pada sidebar
st.sidebar.header("🔍 Filter")

# membuat filter start date dan end date order
min_date = df["order_purchase_timestamp"].min()
max_date = df["order_purchase_timestamp"].max()

start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=min_date, max_value=max_date)

# membuat filter slider harga berdasarkan payment_value
min_price = int(df["payment_value"].min())
max_price = int(df["payment_value"].max())

price_range = st.sidebar.slider("Price Range", min_price, max_price, (min_price, max_price))

# filter data berdasarkan input
filtered = df[
    (df["order_purchase_timestamp"] >= pd.to_datetime(start_date)) &
    (df["order_purchase_timestamp"] <= pd.to_datetime(end_date)) &
    (df["payment_value"] >= price_range[0]) &
    (df["payment_value"] <= price_range[1])
]

# menghitung summary keseluruhan
total_sales = filtered["payment_value"].sum()
total_orders = filtered["order_id"].count()
mean_review = filtered["review_score"].mean()

# mengambil bulan terakhir dari rentang filter untuk digunakan sebagai perbandingan
latest_month = filtered["order_purchase_timestamp"].dt.to_period("M").max()
previous_month = latest_month - 1

# memfilter data bulan terakhir dan bulan sebelumnya
current_month = filtered[filtered["order_purchase_timestamp"].dt.to_period("M") == latest_month]
previous_month = filtered[filtered["order_purchase_timestamp"].dt.to_period("M") == previous_month]

# menghitung metrik untuk bulan terakhir
current_sales = current_month["payment_value"].sum()
current_orders = current_month["order_id"].count()
current_review = current_month["review_score"].mean()

# menghitung metrik untuk bulan sebelumnya
previous_sales = previous_month["payment_value"].sum()
previous_orders = previous_month["order_id"].count()
previous_review = previous_month["review_score"].mean()

# menghitung persentase perubahan
sales_change = ((current_sales - previous_sales) / previous_sales * 100) if previous_sales != 0 else 0
orders_change = ((current_orders - previous_orders) / previous_orders * 100) if previous_orders != 0 else 0
review_change = ((current_review - previous_review) / previous_review * 100) if previous_review != 0 else 0

# memberikan title untuk dashboard
st.header("📈 E-Commerce Analysis Dashboard")

# membuat layout 3 columns untuk summary
col1, col2, col3 = st.columns(3)

# mengisi layout
with col1:
    st.metric("Total Sales", f"${total_sales:,.2f}", f"{sales_change:.2f}%")

with col2:
    st.metric("Total Orders", f"{total_orders:,.0f}", f"{orders_change:.2f}%")

with col3:
    st.metric("Review Score", f"{mean_review:.2f}", f"{review_change:.2f}%")

# membuat layout untuk grafik
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# mengisi column 1 dengan line chart
with col1:
    st.subheader("📦 Orders Per Month")

    # menambahkan kolom bulan
    filtered["month_name"] = filtered["order_purchase_timestamp"].dt.strftime("%B")

    # menghitung jumlah order per bulan
    monthly_orders = filtered.groupby("month_name")["order_id"].count().reset_index()

    # memberikan nama bulan beserta mengurutkannya
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    monthly_orders["month_name"] = pd.Categorical(monthly_orders["month_name"], categories=month_order, ordered=True)
    monthly_orders = monthly_orders.sort_values("month_name")

    # membuat line chart
    fig_line = px.line(monthly_orders, x="month_name", y="order_id", 
                        labels={"month_name": "Month", "order_id": "Orders"}, 
                        )

    # mengatur supaya sumbu y dimulai dari 0
    fig_line.update_yaxes(range=[0, monthly_orders["order_id"].max()])

    # menampilkan chart
    st.plotly_chart(fig_line, use_container_width=True)

# mengisi column 2 dengan line
with col2:
    st.subheader("💰 Sales Per Month")

    # Menambahkan kolom bulan
    filtered["month_name"] = filtered["order_purchase_timestamp"].dt.strftime("%B")

    # Menghitung total sales per bulan
    monthly_sales = filtered.groupby("month_name")["payment_value"].sum().reset_index()

    # Memberikan urutan bulan
    month_order = ["January", "February", "March", "April", "May", "June", 
                   "July", "August", "September", "October", "November", "December"]
    monthly_sales["month_name"] = pd.Categorical(monthly_sales["month_name"], categories=month_order, ordered=True)
    monthly_sales = monthly_sales.sort_values("month_name")

    # Membuat line chart
    fig_line = px.line(monthly_sales, x="month_name", y="payment_value", 
                        labels={"month_name": "Month", "payment_value": "Sales"}
                        )

    # Mengatur supaya sumbu y dimulai dari 0
    fig_line.update_yaxes(range=[0, monthly_sales["payment_value"].max()])

    # Menampilkan chart
    st.plotly_chart(fig_line, use_container_width=True)

# mengisi column 3 dengan pie
with col3:
    st.subheader("💳 Payment Methods")
    payment_counts = filtered["payment_type"].value_counts()
    fig_pie_payment = px.pie(payment_counts, names=payment_counts.index, values=payment_counts.values,
                            )
    st.plotly_chart(fig_pie_payment, use_container_width=True)

# mengisi column 4 dengan pie
with col4:
    st.subheader("⭐ Review Scores")
    review_counts = filtered["review_score"].value_counts()
    fig_pie_review = px.pie(review_counts, names=review_counts.index, values=review_counts.values,
                            )
    st.plotly_chart(fig_pie_review, use_container_width=True)

# mengisi column 5 dengan bar
st.subheader("🏆 Top 10 Best-Selling Categories")
top_categories = filtered["product_category_name_english"].value_counts().nlargest(10).reset_index()
top_categories.columns = ["Category", "Orders"]
bar_fig = px.bar(top_categories, x="Category", y="Orders",
                 text_auto=True, template="plotly_white")
st.plotly_chart(bar_fig, use_container_width=True)

# streamlit run e-commerce_dashboard.py
