# Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv(r"C:\Users\vacoh\car-data-app\vehicles_us.csv")

# Convert date_posted to datetime
df['date_posted'] = pd.to_datetime(df['date_posted'])

# Drop the constant column
df.drop('is_4wd', axis=1, inplace=True)

# Impute missing values in model_year with the median
median_model_year = df['model_year'].median()
df['model_year'] = df['model_year'].fillna(median_model_year)

# Impute missing values in cylinders with the median
median_cylinders = df['cylinders'].median()
df['cylinders'] = df['cylinders'].fillna(median_cylinders)

# Impute missing values in odometer with the median
median_odometer = df['odometer'].median()
df['odometer'] = df['odometer'].fillna(median_odometer)

# Impute categorical column with the mode
mode_paint_color = df['paint_color'].mode()[0]
df['paint_color'] = df['paint_color'].fillna(mode_paint_color)

st.title("Car Advertisement Data Analysis")
st.write("Explore car data and trends.")

# 1. Price Distribution by Make/Model
st.subheader("Price Distribution by Make/Model")
fig_price_make = px.histogram(df, x="price", color="model", title="Price Distribution by Make/Model")
st.plotly_chart(fig_price_make)

# 2. Distribution of Price by Vehicle Type
st.subheader("Price Distribution by Vehicle Type")
fig_price_by_type = px.box(df, x="type", y="price", title="Price Distribution by Vehicle Type")
st.plotly_chart(fig_price_by_type)

# 3. Count of Vehicles by Model (Top 10)
st.subheader("Top 10 Vehicle Makes")
top_10_makes = df['model'].value_counts().nlargest(10).reset_index()
top_10_makes.columns = ['model', 'count']
fig_make_count = px.bar(top_10_makes, x="model", y="count", title="Top 10 Vehicle Makes")
st.plotly_chart(fig_make_count)
