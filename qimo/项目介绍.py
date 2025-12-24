import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="💯",
    layout="wide"
    )

st.title("🎓学生成绩分析与预测系统")
st.markdown('***')
    
c1,c2=st.columns([5,2])
with c1:
    st.header("🗎项目概述")
    st.text("本项目是一个基于Streamlit的学生成绩分析平台，通过数据可视化和机器学习技术，帮助教育工作者和学生深入了解学业表现，并预测期末考试成绩。")

    st.subheader("主要特点：")
    st.markdown("-数据可视化：多维度展示学生学业数据")
    st.markdown("-专业分析：按专业分类的详细统计分析")
    st.markdown("-智能预测：基于机器学习模型的成绩预测")
    st.markdown("-学习建议：根据预测结果提供个性化反馈")
        

with c2:
    st.image("数据分析.png")
        
st.markdown('***')

st.header("🚀项目目标")
c3,c4,c5=st.columns(3)
with c3:
    st.subheader("目标一")
    st.markdown(
        """
        分析影响因素
        - 识别关键学习指标
        - 探索成绩相关因素
        - 提供数据支持决策
    """
    )
with c4:
    st.subheader("目标二")
    st.markdown(
         """
         可视化展示
         - 专业对比分析
         - 性别差异研究
         - 学习模式识别
    """
    )
with c5:
    st.subheader("目标三")
    st.markdown(
        """
        成绩预测
        - 机器学习模型
        - 个性化预测
        - 及时干预预警
    """
    )
st.markdown('***')

st.header("🛠️技术架构")
js_col1,js_col2,js_col3,js_col4=st.columns(4)
with js_col1:
    st.text("前瞻框架")
    python_code="""Streamlit"""
    st.code(python_code)
        
with js_col2:
    st.text("数据处理")
    python_code="""Pandas\nNunPy"""
    st.code(python_code)
with js_col3:
    st.text("可视化")
    python_code="""Plotly\nMatplotlib"""
    st.code(python_code)
with js_col4:
    st.text("机器学习")
    python_code="""Scikit-learn"""
    st.code(python_code)
