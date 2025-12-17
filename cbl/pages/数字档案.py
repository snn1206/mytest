import pandas as pd
import streamlit as st   # 导入Streamlit并用st代表它

st.title("🕶学生-数字档案")
st.header("🔑基础信息")
st.text("学生ID：000019")
st.markdown("**注册时间：**:green[2025—12—11]**|精神状态：✅正常**")
st.markdown("**当前教室：**:green[实训楼108]**|安全等级：:green[绝密]**")

st.header("📊技能矩阵")
# 定义列布局，分成3列
c1,c2,c3=st.columns(3)
c1.metric(label="c语言",help="问号", value="95%", delta="2%")
c2.metric(label="Pyhon", value="87%", delta="-1%")
c3.metric(label="Java",help="问号", value="68%", delta="-10%")

st.subheader("Streamlit课程进度")
st.text("Streamlit课程进度")
# 课程进度设置为0.4
progress=0.4
st.progress(progress)

st.header("📅任务日志")
# 定义数据,以便创建数据框
data = {
    '日期':['2025—12—11', '2025—12—10', '2025—12—12'],
    '任务':['学生数字档案', '课程管理系统', '数据图表展示'],
    '状态':['✅完成', '🕐进行中', '❌未完成'],
    '难度':['⭐️⭐⚝⚝⚝','⭐⚝⚝⚝⚝','⭐️⭐️⭐⚝⚝',]
}
# 根据上面创建的data，创建数据框
df = pd.DataFrame(data)
st.write(df)

st.subheader("🔐最新代码成果")
python_code="""def hello():
    print("你好，Streamlit！")
"""
st.caption('代码块1：Python代码')
st.code(python_code)

st.markdown('***')
st.markdown(':green[>>SYSTEM MESSAGE:]下一个任务目标已解锁...')
st.markdown(':green[>>TARGET:]课程管理系统')
st.markdown(':green[>>COUNTDOWN:]2025.12.11')
st.text("系统状态：在线 连接状态：已加密")
