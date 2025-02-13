# Importing necessary libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv(r"C:\Users\vacoh\car-data-app\vehicles_us.csv")
st.write("Data loaded successfully!")
