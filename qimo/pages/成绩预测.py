import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np


plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(
    page_title="期末成绩预测", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.title("🔮期末成绩预测")


@st.cache_resource # 缓存模型，避免重复训练
def load_data_and_train_model():
    # 加载数据（替换为你的CSV路径）
    LOCAL_CSV_PATH = "student_data_adjusted_rounded.csv"
    df = pd.read_csv(LOCAL_CSV_PATH)
    
    # 选择特征和目标变量
    X = df[["性别", "专业", "每周学习时长（小时）", "上课出勤率", "期中考试分数", "作业完成率"]]
    y = df["期末考试分数"]
    
    # 构建预处理+模型的管道（处理分类特征的独热编码）
    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), ["性别", "专业"])
        ],
        remainder="passthrough"
    )
    
    # 训练线性回归模型
    model = Pipeline([
        ("preprocessor", preprocessor),
        ("regressor", LinearRegression())
    ])
    model.fit(X, y)
    
    # 返回模型和数据中的专业列表（用于下拉框）
    majors = df["专业"].unique().tolist()
    return model, majors

# 加载模型和专业列表
model, available_majors = load_data_and_train_model()

# 页面：期末成绩预测表单
st.header("期末成绩预测", divider=False)
st.write("请输入学生的学习信息，系统将预测其期末成绩并提供学习建议")

# 输入表单（分左右两列布局）
col_input1, col_input2 = st.columns([2, 1])

with col_input1:
    # 基础信息输入
    student_id = st.text_input("学号", value="12321321")
    gender = st.selectbox("性别", options=["男", "女"], index=0)
    major = st.selectbox("专业", options=available_majors, index=available_majors.index("信息系统") if "信息系统" in available_majors else 0)

with col_input2:
    # 学习指标滑块
    study_hours = st.slider("每周学习时长（小时）", min_value=0.0, max_value=40.0, value=10.0, step=0.5)
    attendance = st.slider("上课出勤率", min_value=0.0, max_value=1.0, value=0.6, step=0.05)
    midterm_score = st.slider("期中考试分数", min_value=0.0, max_value=100.0, value=40.0, step=1.0)
    homework_rate = st.slider("作业完成率", min_value=0.0, max_value=1.0, value=0.7, step=0.05)

# 预测按钮
predict_btn = st.button("预测期末成绩", type="primary")

# 预测逻辑+结果展示
if predict_btn:
    # 构造输入数据
    input_data = pd.DataFrame({
        "性别": [gender],
        "专业": [major],
        "每周学习时长（小时）": [study_hours],
        "上课出勤率": [attendance],
        "期中考试分数": [midterm_score],
        "作业完成率": [homework_rate]
    })
    
    # 预测期末成绩
    predicted_score = model.predict(input_data)[0]
    predicted_score = round(predicted_score, 1)  # 保留1位小数
    
    # 判断是否及格
    is_pass = predicted_score >= 60
    
    # 展示预测结果
    st.subheader("预测结果")
    with st.container():
        # 成绩展示栏
        result_bg = "#22C55E" if is_pass else "#EF4444"

        # 展示对应图片
        if is_pass:
            st.image("https://ts1.tc.mm.bing.net/th/id/R-C.bbaf71a60b6b4505f97f0060e37535c7?rik=8S0qBMM%2fVsbWGw&riu=http%3a%2f%2fpic.616pic.com%2fys_b_img%2f00%2f06%2f11%2fG9aZ00ff4B.jpg&ehk=DHxCVOHaRccAFcLqbRcBzY6tXixgFGfqoDkKnD6qszM%3d&risl=&pid=ImgRaw&r=0", width=100, caption="恭喜！成绩及格")
        else:
            st.image("https://img.ixintu.com/download/jpg/20200803/3c313093ab8f409c6fde482ef2faf3dc_512_512.jpg!ys", width=100, caption="加油！建议增加学习时长")
        
        # 学习建议
        st.write("### 学习建议")
        if not is_pass:
            st.markdown("""
            - 建议将每周学习时长增加至15小时以上
            - 提高上课出勤率（目标≥0.8）
            - 重点复习期中考试薄弱知识点
            """)
        else:
            st.markdown("""
            - 保持当前学习节奏，可适当拓展专业知识
            - 继续保持作业完成率
            """)
