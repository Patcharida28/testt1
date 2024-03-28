import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.header("🌶️Website Developing using Python🌶️")

st.subheader("🍔Patcharida Choomchoo🍔")
st.image('patch.jpg')

dt=pd.read_csv('./data/iris.csv')

st.header("ข้อมูลดอกไม้ iris")
st.write(dt.head(10))

st.subheader("สถิติข้อมูลดอกไม้ iris")
st.write('ผลรวม')
cl1,cl2,cl3,cl4 = st.columns(4)
cl1.write(dt['sepal.length'].sum())
cl2.write(dt['sepal.width'].sum())
cl3.write(dt['petal.length'].sum())
cl4.write(dt['petal.width'].sum())
#Index(['sepal.length', 'sepal.width', 'petal.length', 'petal.width',
#      'variety'],

st.write('ค่าเฉลี่ย')
cl1,cl2,cl3,cl4 = st.columns(4)
cl1.write(dt['sepal.length'].mean())
cl2.write(dt['sepal.width'].mean())
cl3.write(dt['petal.length'].mean())
cl4.write(dt['petal.width'].mean())
st.write('ค่ามากที่สุด')
st.write('ค่าน้อยที่สุด')