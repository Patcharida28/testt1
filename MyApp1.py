import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.header("🌶️Website Developing using Python🌶️")

st.subheader("🍔Patcharida Choomchoo🍔")
st.image('patch.jpg')

dt=pd.read_csv('/data/iris.csv')
st.write(dt.head('10'))