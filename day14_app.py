# 先简单了解下streamlit这个工具，用来做可交互式的网页，运行的话必须在终端输入streamlit run 才行


import streamlit as st
import pandas as pd

st.title("我的第一个数据看板 🚀")

# 读取你前几天处理好的成绩CSV文件
df = pd.read_csv("students_day13.csv")

# 在网页上展示表格
st.dataframe(df)

# 画一个简单的折线图或柱状图
st.line_chart(df["score"])