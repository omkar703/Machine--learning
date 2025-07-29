import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df , iris.target_names

df, target_names = load_data()

model = RandomForestClassifier()
# (independent variables[except last one -1], dependent variable)
model.fit(df.iloc[:, :-1], df['species'])

st.title('Iris Species Predictor')
st.sidebar.title('Input Feautures')

sepal_length = st.sidebar.slider('Sepal Length', min_value=0.0, max_value=8.0, value=0.0)

sepal_width = st.sidebar.slider('Sepal Width', min_value=0.0, max_value=3.0, value=0.0)

petal_length = st.sidebar.slider('Petal Length', min_value=0.0, max_value=6.0, value=0.0)

petal_width = st.sidebar.slider('Petal Width', min_value=0.0, max_value=2.5, value=0.0)

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# predict the species
prediction = model.predict(input_data)

st.write('Predicted Species:', target_names[prediction[0]])