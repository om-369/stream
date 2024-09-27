import streamlit as st
import pandas as pd

st.title('Streamlit Text Input')

name = st.text_input('Enter your name :')

age = st.slider('select your age :',0,100,25)
st.write(f"YOur age is {age}.")

options = ['Python', 'java','c++', 'javascript']
choice = st.selectbox("choose your favorite language :",options)
st.write(f"You have selected {choice}.")


if name:
    st.write(f"Hello,{name}")

data = {
    "Name": ['John','Jane','JAke','Jill'],
    "Age" : [24,32,35,40],
    "City" : ["NEWyork","loss Angeles", 'chicago','Houston']
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_files = st.file_uploader("choose a csv file",type='csv')

if uploaded_files is not None:
    df = pd.read_csv(uploaded_files)
    st.write(df)
