import streamlit as st
import pandas as pd


st.title("Data Science and AI batch 05")

name= st.text_input("Enter your name here: ")


if name:
    st.write(f"Hello, {name}, Welcome to our AI class")

age= st.slider("select your current age please :", 0, 100,30)

st.write(f"{name}, do remember that your age is :{age}") 


option= ["python", "Java", "C++", "JavaScript"]

choice= st.selectbox(" Choose your favourite language:", option)

st.write(f"You selected: {choice}")

data = {"Name": ["Samia", "Zeeshan"," Zoha", "Haya","Hamza"],
        "age": [20,30,40,50,60],
        "City": ["New York","Chicago","Houston","Boston"," California"]
        }

df=pd.DataFrame(data)

df.to_csv("sample data.csv")

st.write(df)


uploaded_file = st.file_uploader("Choose a CSV file ", type= "csv")


if uploaded_file is not None:

    df= pd.read_csv(uploaded_file)

    st.write(df)