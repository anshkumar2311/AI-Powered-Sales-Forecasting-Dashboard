# 📊 AI Sales Forecasting Dashboard using Streamlit

import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="AI Sales Forecasting", layout="wide")

# Title
st.title("📊 AI Sales Forecasting Dashboard")
st.markdown("""
Welcome to your interactive analytics dashboard!  
Track performance across **regions**, **categories**, and **time**, and gain valuable insights on **sales**, **profit**, and **discount trends**.
""")

# Load CSV
try:
    df = pd.read_csv("your_final_dataset.csv", parse_dates=["Order Date"])
except FileNotFoundError:
    st.error("❌ Dataset file 'your_final_dataset.csv' not found. Please upload it.")
    st.stop()

# Validate required columns
required_columns = ["Order Date", "Category", "Region", "Sales", "Profit", "Order ID", "Discount", "IsWeekend", "IsHoliday"]
missing = [col for col in required_columns if col not in df.columns]
if missing:
    st.error(f"❌ Missing required columns: {', '.join(missing)}")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter Your Data")

start_date = st.sidebar.date_input("Start Date", df["Order Date"].min().date())
end_date = st.sidebar.date_input("End Date", df["Order Date"].max().date())

categories = st.sidebar.multiselect("Select Category", options=df["Category"].unique(), default=df["Category"].unique())
regions = st.sidebar.multiselect("Select Region", options=df["Region"].unique(), default=df["Region"].unique())

weekend_only = st.sidebar.checkbox("✅ Only Weekends")
holiday_only = st.sidebar.checkbox("✅ Only Holidays")

# Apply filters
filtered_df = df[
    (df["Order Date"] >= pd.to_datetime(start_date)) &
    (df["Order Date"] <= pd.to_datetime(end_date)) &
    (df["Category"].isin(categories)) &
    (df["Region"].isin(regions))
]

if weekend_only:
    filtered_df = filtered_df[filtered_df["IsWeekend"] == True]
if holiday_only:
    filtered_df = filtered_df[filtered_df["IsHoliday"] == True]

# --- KPIs ---
st.markdown("---")
st.subheader("📈 Key Performance Indicators")
k1, k2, k3, k4 = st.columns(4)
k1.metric("💰 Total Sales", f"₹{filtered_df['Sales'].sum():,.0f}")
k2.metric("📈 Total Profit", f"₹{filtered_df['Profit'].sum():,.0f}")
k3.metric("🧾 Total Orders", filtered_df["Order ID"].nunique())
k4.metric("🔖 Avg Discount", f"{filtered_df['Discount'].mean():.2%}")

# --- Monthly Sales Trend ---
st.markdown("---")
st.subheader("📅 Monthly Sales Trend")
monthly = filtered_df.copy()
monthly["Month"] = monthly["Order Date"].dt.to_period("M").astype(str)
monthly_summary = monthly.groupby("Month")[["Sales"]].sum().reset_index()

fig1 = px.line(monthly_summary, x="Month", y="Sales", markers=True, title="Monthly Sales")
st.plotly_chart(fig1, use_container_width=True)

# --- Category Sales ---
st.markdown("---")
st.subheader("🛍️ Sales by Category")
cat_sales = filtered_df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
fig2 = px.bar(
    x=cat_sales.index,
    y=cat_sales.values,
    labels={"x": "Category", "y": "Sales"},
    title="Sales by Category",
    color=cat_sales.index,
)
st.plotly_chart(fig2, use_container_width=True)

# --- Region Pie Chart ---
st.markdown("---")
st.subheader("🌍 Regional Sales Distribution")
region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()
fig3 = px.pie(region_sales, names="Region", values="Sales", title="Sales Distribution by Region")
st.plotly_chart(fig3, use_container_width=True)

# --- Profit vs Discount ---
st.markdown("---")
st.subheader("📊 Profit vs Discount")
fig4 = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    size="Sales",
    color="Category",
    title="Profit vs Discount",
    hover_data=["Region"]
)
st.plotly_chart(fig4, use_container_width=True)

# --- NEW: Sales by Weekday ---
st.markdown("---")
st.subheader("📆 Sales by Day of Week")
filtered_df["Weekday"] = filtered_df["Order Date"].dt.day_name()
weekday_sales = filtered_df.groupby("Weekday")["Sales"].sum().reindex([
    "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"
]).reset_index()

fig5 = px.bar(
    weekday_sales,
    x="Weekday",
    y="Sales",
    title="Sales by Weekday",
    color="Weekday"
)
st.plotly_chart(fig5, use_container_width=True)

# --- Data Table & Export ---
st.markdown("---")
st.subheader("📋 Filtered Data Table")
st.dataframe(filtered_df, use_container_width=True)

csv = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download Filtered Data", csv, file_name="filtered_ai_sales_forecasting_data.csv", mime="text/csv")
