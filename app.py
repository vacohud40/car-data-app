# Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('vehicles_us.csv')

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

# --------------------------------------------------
# Filters Section
# --------------------------------------------------

# 1. Model Filter
model_options = df['model'].unique()
selected_models = st.multiselect("Select Models", model_options, default=model_options)

# 2. Fuel Type Filter
fuel_type_options = df['fuel'].unique()
selected_fuel_types = st.multiselect("Select Fuel Types", fuel_type_options, default=fuel_type_options)

# 3. Price Range Filter
min_price = int(df['price'].min())
max_price = int(df['price'].max())
price_range = st.slider("Price Range", min_price, max_price, (min_price, max_price))

# 4. Year Range Filter
min_year = int(df['model_year'].min())
max_year = int(df['model_year'].max())
year_range = st.slider("Year Range", min_year, max_year, (min_year, max_year))

# 5. Condition Filter
condition_options = df['condition'].unique()
selected_conditions = st.multiselect("Select Conditions", condition_options, default=condition_options)

# 6. Type Filter
type_options = df['type'].unique()
selected_types = st.multiselect("Select Vehicle Types", type_options, default=type_options)

# 7. Cylinders Filter
cylinder_options = df['cylinders'].unique()
selected_cylinders = st.multiselect("Select Number of Cylinders", cylinder_options, default=cylinder_options)

# 8. Odometer Filter
min_odometer = int(df['odometer'].min())
max_odometer = int(df['odometer'].max())
odometer_range = st.slider("Odometer Range", min_odometer, max_odometer, (min_odometer, max_odometer))



# --------------------------------------------------
# Apply Filters
# --------------------------------------------------

filtered_df = df[
    df['model'].isin(selected_models) &
    df['fuel'].isin(selected_fuel_types) &
    (df['price'] >= price_range[0]) & (df['price'] <= price_range[1]) &
    (df['model_year'] >= year_range[0]) & (df['model_year'] <= year_range[1]) &
    df['condition'].isin(selected_conditions) &
    df['type'].isin(selected_types) &
    df['cylinders'].isin(selected_cylinders) &
    (df['odometer'] >= odometer_range[0]) & (df['odometer'] <= odometer_range[1])
]

# --------------------------------------------------
# Charts Section (Use filtered_df)
# --------------------------------------------------

# 1. Price Distribution by Model
st.subheader("Price Distribution by Model")
fig_price_model = px.histogram(filtered_df, x="price", color="model", title="Price Distribution by Model (Filtered)")
st.plotly_chart(fig_price_model)

# 2. Distribution of Price by Vehicle Type
st.subheader("Price Distribution by Vehicle Type")
fig_price_by_type = px.box(filtered_df, x="type", y="price", title="Price Distribution by Vehicle Type (Filtered)")
st.plotly_chart(fig_price_by_type)

# 3. Count of Vehicles by Model (Top 10)
st.subheader("Top 10 Vehicle Models")
top_10_models = filtered_df['model'].value_counts().nlargest(10).reset_index()
top_10_models.columns = ['model', 'count']
fig_model_count = px.bar(top_10_models, x="model", y="count", title="Top 10 Vehicle Models (Filtered)")
st.plotly_chart(fig_model_count)

# 4. Price vs. Odometer (Scatter Plot)
st.subheader("Price vs. Odometer")
fig_price_odometer = px.scatter(filtered_df, x="odometer", y="price", color="type", title="Price vs. Odometer (Filtered)")
st.plotly_chart(fig_price_odometer)

# 5. Model Year Distribution
st.subheader("Model Year Distribution")
fig_model_year = px.histogram(filtered_df, x="model_year", title="Model Year Distribution (Filtered)")
st.plotly_chart(fig_model_year)

# 6. Condition Distribution
st.subheader("Condition Distribution")
fig_condition = px.bar(filtered_df, x="condition", title="Condition Distribution (Filtered)")
st.plotly_chart(fig_condition)


# 7. Fuel Type Distribution
st.subheader("Fuel Type Distribution")
fig_fuel = px.pie(filtered_df, names="fuel", title="Fuel Type Distribution (Filtered)")
st.plotly_chart(fig_fuel)



