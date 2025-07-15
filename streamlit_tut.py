import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title('Hello Streamlit')

# use the command - streamlit run streamlit.py

# Display a simple text
st.write('This is a webpage')

# Display simple dataframe

df = pd.DataFrame({'First':[1,2,3,4,5], 'Second':[6,7,8,9,10]})
st.write('Dataframe')
st.write(df)

# Create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['A', 'B', 'C']
)

st.line_chart(chart_data)

# Creating widgets and more interactive app using streamlit
st.title('User Input here')
name = st.text_input('Enter your name-')
try:
    if name:
        st.write(f'Your name is {name}')
except Exception as e:
    print('Enter correctly',e)

# Display a slider
age = st.slider('Select your age',12,100,20)
st.write('Your age is:',age)

# Display a selectbox
lang = ['Python', 'C', 'C++', 'JavaScript']
choice = st.selectbox('Choose your programming language:',lang)
st.write('You selected-',choice)

# Upload a file
upload_file = st.file_uploader("Select your csv file",type='csv')
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)
