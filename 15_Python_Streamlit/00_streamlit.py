import streamlit as st
import pandas as pd
import numpy as np

## Title of the app

st.title('Data Analysis App')

# Display a simple txt

st.write('This app is for data analysis')

## Create simple data frame

data = {
    'Name': ['John', 'Jane', 'Alice'],
    'Age': [25, 30, 28],
    'City': ['New York', 'London', 'Paris']
}

df = pd.DataFrame(data)

st.write(df)

## Create a line chart

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['A', 'B', 'C'])

st.line_chart(chart_data)
    