<h1 align="center">📊 AI Sales Forecasting Dashboard</h1>
<p align="center">
  A sleek and interactive dashboard built with <strong>Streamlit</strong> + <strong>Plotly</strong><br>
  for analyzing and forecasting e-commerce sales performance using smart filters and visual insights.
</p>
<p align="center">
  
![Landing Page Screenshot](https://github.com/anshkumar2311/FUTURE_ML_01/blob/main/Assets/Screenshot_20250728_163609.png)
</p>

<p align="center">
  <a href="https://aisalesforecasting.streamlit.app/">🌐 Live Demo</a> |
  <a href="https://github.com/anshkumar2311/FUTURE_ML_01">🔗 GitHub</a> |
  <a href="https://www.linkedin.com/in/ansh-kumar-747009311/">👨‍💻 Author</a>
</p>

---

## 🚀 Overview

The **AI Sales Forecasting Dashboard** is a data visualization tool that helps you monitor and analyze sales trends, performance metrics, and promotional impact. Ideal for business analysts, data science learners, and product teams.

It features:
- Clear KPIs
- Time-series analysis
- Smart filters
- CSV export

---

## 🧩 Features

✅ **Filterable by Date, Region, and Category**  
📅 **Weekend & Holiday Checkboxes**  
📈 **Key Performance Indicators**: Sales, Profit, Orders, Discounts  
📊 **Interactive Graphs Powered by Plotly**  
🔮 **Sales Forecasting using Prophet**  
📥 **Download Filtered Data as CSV**  
💡 **Responsive and Clean UI using Streamlit Layouts**

---

## 🛠 Tech Stack Used

This project combines the power of modern data science tools and web technologies:

- **📊 Streamlit** – For building fast and beautiful interactive dashboards
- **📈 Matplotlib Plotly Express** – For dynamic and customizable data visualizations
- **🐍 Python 3.11+** – Core language for data manipulation and backend logic
- **🧮 Pandas** – For handling and filtering the sales dataset
- **📦 Pyngrok** – To expose the local app securely over the internet
- **🗃️ CSV File** – Used as the backend data source (no database required)

> ⚙️ Deployed on **Streamlit Cloud**.

---

## 🔮 Forecasting Model (Prophet)

We use [Facebook Prophet](https://facebook.github.io/prophet/) for time series forecasting:
- Trained on historical `Sales` data
- Forecasts future sales
- Visualized directly in the dashboard
  
![](https://github.com/anshkumar2311/FUTURE_ML_01/blob/main/Assets/Screenshot_20250728_163658.png)
---

## 📌 Visuals
![](https://github.com/anshkumar2311/FUTURE_ML_01/blob/main/Assets/download%20(1).png)
 
![](https://github.com/anshkumar2311/FUTURE_ML_01/blob/main/Assets/Screenshot_20250727_222450.png)

![](https://github.com/anshkumar2311/FUTURE_ML_01/blob/main/Assets/download%20(2).png)
![](https://github.com/anshkumar2311/FUTURE_ML_01/blob/main/Assets/Screenshot_20250727_222926.png)

---

## 📁 Dataset Schema

Ensure your `your_final_dataset.csv` contains:

```csv
Order Date, Category, Region, Sales, Profit, Order ID, Discount, IsWeekend, IsHoliday
```
---

## ▶️ Getting Started

Ready to launch the AI Sales Forecasting Dashboard on your machine? Follow these simple steps:

---

### 🔧 Setup

```bash
git clone https://github.com/anshkumar2311/FUTURE_ML_01.git
cd FUTURE_ML_01
pip install -r requirements.txt
streamlit run app.py
```
---

## 📥 Download Filtered Data

🎯 **Purpose**: Empower users to focus only on the data they care about!

The dashboard offers an intuitive and seamless way to:

- 📅 **Select Date Range**
- 🛒 **Choose Product Categories**
- 🌍 **Filter by Sales Region**
- 🏖️ **Toggle Weekend and Holiday Filters**

Once filtered, users can easily:

✅ **Export the view as a downloadable CSV file**  
📤 **Use the data for further analysis or reporting**

Whether you're a marketer, business analyst, or data enthusiast — this feature brings flexibility and control to your fingertips.

---

## 🌟 Show Some Love

If you like this project, please consider:

⭐️ **Starring** the repo  
🍴 **Forking** it for your own version  

Let’s connect and grow together 🚀

