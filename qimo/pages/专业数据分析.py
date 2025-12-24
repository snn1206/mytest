import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go


st.set_page_config(
    page_title="专业分析看板", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

st.title("📊专业数据分析")
st.markdown("***")

LOCAL_CSV_PATH = "student_data_adjusted_rounded.csv"

@st.cache_data  
def load_real_data(local_path):
    """加载本地CSV真实数据，筛选有效记录并返回"""
    df_raw = pd.read_csv(local_path)
    # 筛选有效数据：性别为男/女，专业不为空
    df_valid = df_raw[(df_raw["性别"].isin(["男", "女"])) & (df_raw["专业"].notna())]
    return df_valid
    

# 加载真实原始数据
df_raw = load_real_data(LOCAL_CSV_PATH)

# 统计各专业各性别的人数
gender_count = df_raw.groupby(["专业", "性别"]).size().reset_index(name="人数")
# 计算各专业总人数
gender_total = gender_count.groupby("专业")["人数"].sum().reset_index(name="总人数")
# 合并人数和总人数，计算比例
gender_ratio = pd.merge(gender_count, gender_total, on="专业")
gender_ratio["比例"] = round(100 * gender_ratio["人数"] / gender_ratio["总人数"], 1)
# 只保留需要的列（专业、性别、比例）
gender_ratio = gender_ratio[["专业", "性别", "比例"]]

# 学习指标数据（基于真实数据按专业聚合核心指标）
df = df_raw.groupby("专业").agg({
    "每周学习时长（小时）": "mean",
    "期中考试分数": "mean",
    "期末考试分数": "mean",
    "上课出勤率": lambda x: round(x.mean() * 100, 1)
}).reset_index()
# 重命名列名
df.columns = ["专业", "study_hours", "midterm_score", "final_score", "出勤率"]
df = df.round(1)

# 大数据管理专业成绩分布
bigdata_scores = df_raw[df_raw["专业"] == "大数据管理"][["期末考试分数"]].rename(
    columns={"期末考试分数": "final_score"}
).dropna()

# 1. 各专业男女性别比例
st.header("1.各专业男女性别比例", divider=False)
col_g1, col_g2 = st.columns([2, 1])

with col_g1:
    fig_gender = px.bar(
        gender_ratio,
        x="专业",
        y="比例",
        color="性别",
        barmode="group",
        color_discrete_map={"男": "#66b3ff", "女": "#2046A1"},
        template="plotly_dark",
        height=300,
        labels={"比例": "比例(%)", "专业": ""},
        text=None
    )
    fig_gender.update_layout(
        showlegend=True,
        legend_title_text='',
        xaxis_tickangle=0,
        yaxis_range=[0, 100],
        margin=dict(l=0, r=0, t=20, b=0),
        font=dict(color="white", size=10),
        title=None,
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    fig_gender.update_traces(text='')
    st.plotly_chart(fig_gender, use_container_width=True)

with col_g2:
    st.write("### 性别比例数据")
    # 透视表转换（修复重复列问题）
    gender_table = gender_ratio.pivot(index="专业", columns="性别", values="比例").round(1).fillna(0)
    # 重置索引并改名（避免索引冲突）
    gender_table = gender_table.reset_index()
    gender_table.columns.name = None  # 清除列索引的名称
    gender_table = gender_table.rename(columns={"专业": "major"})
    st.dataframe(gender_table.set_index("major"), hide_index=False, use_container_width=True)

st.markdown("***")

# 2. 各专业学习指标对比
st.header("2.各专业学习指标对比", divider=False)
col_s1, col_s2 = st.columns([3, 1])

with col_s1:
    plt.rcParams['font.sans-serif'] = ['SimHei', 'WenQuanYi Micro Hei', 'Heiti TC']
    
    fig, ax1 = plt.subplots(figsize=(12, 5), facecolor='#0E1117')
    ax1.set_facecolor('#0E1117')
    x = range(len(df["专业"]))
    
    ax1.bar(x, df["study_hours"], color='#87CEEB', alpha=1, label='平均学习时间')
    ax1.set_ylabel('平均学习时间（小时）', color='white', fontsize=10)
    ax1.tick_params(axis='y', colors='white')
    ax1.tick_params(axis='x', colors='white')
    ax1.set_xticks(x)
    ax1.set_xticklabels(df["专业"], color='white', rotation=0)
    ax1.set_ylim(0, max(df["study_hours"]) * 1.2)
    
    ax2 = ax1.twinx()
    ax2.plot(x, df["midterm_score"], color='#FFA500', marker='_', linewidth=2, label='平均期中成绩')
    ax2.plot(x, df["final_score"], color='#32CD32', marker='_', linewidth=2, label='平均期末成绩')
    ax2.set_ylabel('成绩（分）', color='white', fontsize=10)
    ax2.tick_params(axis='y', colors='white')
    ax2.set_ylim(0, 100)
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1+lines2, labels1+labels2, loc='upper left', facecolor='#0E1117', labelcolor='white', fontsize=8)
    ax1.set_title("各专业平均学习时间与成绩对比", color='white', fontsize=12, pad=5)
    
    st.pyplot(fig)

with col_s2:
    st.write("### 详细数据")
    study_table = df[["专业", "study_hours", "midterm_score", "final_score"]].rename(columns={"专业": "major"})
    st.dataframe(study_table.set_index("major"), hide_index=False, use_container_width=True)

st.markdown("***")

# 3. 各专业出勤率分析
st.header("3.各专业出勤率分析", divider=False)
col_a1, col_a2 = st.columns([2, 1])

with col_a1:
    fig_att = px.bar(
        df.sort_values("出勤率", ascending=False),
        x="专业",
        y="出勤率",
        color="出勤率",
        color_continuous_scale=["#FFFF00", "#800080"],
        template="plotly_dark",
        height=300,
        labels={"出勤率": "平均出勤率（%）", "专业": ""},
        text=None
    )
    fig_att.update_layout(
        showlegend=False,
        xaxis_tickangle=0,
        yaxis_range=[max(0, min(df["出勤率"]) - 5), min(100, max(df["出勤率"]) + 5)],
        margin=dict(l=0, r=0, t=20, b=0),
        font=dict(color="white", size=10),
        title="各专业平均出勤率",
        title_font=dict(size=12, color='white'),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
    fig_att.update_traces(text='')
    st.plotly_chart(fig_att, use_container_width=True)

with col_a2:
    st.write("### 出勤率排名")
    att_rank = df.sort_values("出勤率", ascending=False).reset_index(drop=True)
    att_rank["排名"] = att_rank.index + 1
    att_rank_table = att_rank[["排名", "专业", "出勤率"]].rename(columns={"出勤率": "平均出勤率（%）"})
    st.dataframe(att_rank_table.set_index("排名"), hide_index=False, use_container_width=True)

st.markdown("***")

# 4. 大数据管理专业专项分析
st.header("4.大数据管理专业专项分析", divider=False)
# 关键指标卡片
bigdata_df = df[df["专业"] == "大数据管理"]
if not bigdata_df.empty:
    avg_attendance = f"{bigdata_df['出勤率'].iloc[0]}%"
    avg_final_score = f"{bigdata_df['final_score'].iloc[0]}分"
    pass_rate = round(len(bigdata_scores[bigdata_scores["final_score"] >= 60]) / len(bigdata_scores) * 100, 1) if len(bigdata_scores) > 0 else 0
    avg_study_hours = f"{bigdata_df['study_hours'].iloc[0]}小时"
else:
    avg_attendance = "暂无数据"
    avg_final_score = "暂无数据"
    pass_rate = 0
    avg_study_hours = "暂无数据"

col_m1, col_m2, col_m3, col_m4 = st.columns(4)
with col_m1:
    st.metric("平均出勤率", avg_attendance)
with col_m2:
    st.metric("平均期末成绩", avg_final_score)
with col_m3:
    st.metric("及格率", f"{pass_rate}%" if pass_rate != 0 else "暂无数据")
with col_m4:
    st.metric("平均学习时间", avg_study_hours)

# 成绩分布
col_d1, col_d2 = st.columns(2)
with col_d1:
    if len(bigdata_scores) > 0:
        fig_dist = px.histogram(
            bigdata_scores,
            x="final_score",
            color_discrete_sequence=["#32CD32"],
            template="plotly_dark",
            title="大数据管理专业期末成绩分布",
            labels={"final_score": "final_score"},
            nbins=10
        )
        fig_dist.update_layout(
            font=dict(color="white"),
            xaxis_range=[0, 100],
            margin=dict(l=0, r=0, t=20, b=0)
        )
        st.plotly_chart(fig_dist, use_container_width=True)
    else:
        st.info("暂无大数据管理专业的成绩数据")

with col_d2:
    if len(bigdata_scores) > 0:
        fig_box = px.box(
            bigdata_scores,
            y="final_score",
            color_discrete_sequence=["#32CD32"],
            template="plotly_dark",
            title="大数据管理专业期末成绩箱线图",
            labels={"final_score": "final_score"}
        )
        fig_box.update_layout(
            font=dict(color="white"),
            yaxis_range=[0, 100],
            margin=dict(l=0, r=0, t=20, b=0)
        )
        st.plotly_chart(fig_box, use_container_width=True)
    else:
        st.info("暂无大数据管理专业的成绩数据")
