import streamlit as st
import pandas as pd
st.title('Data Text input')

name = st.text_input('Enter your name')

# Create a slider to get the user's age
age = st.slider('Enter your age', 0, 100 ,25)

options = ['Python', 'Java', 'JavaScript', 'C++', 'Go']

# Create a selectbox to choose a favorite programming language
language = st.selectbox('Choose your favorite programming language', options)

# Display the user's input
 
st.write(f'Favorite programming language: {language}')

# Add a submit button

if name:
    st.write(f"name is {name} and age is {age}")

upload_file = st.file_uploader('Upload a CSV file',type= ['csv'])

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.dataframe(df)
    