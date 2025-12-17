import streamlit as st 
import pandas as pd
import plotly.express as px

st.sidebar.empty()

def get_dataframe_from_excel():
    # pd.read_excel()函数用于读取Excel文件的数据
    # 'supermarket_sales.xlsx'表示Excel文件的路径及名称
    # sheet_name='销售数据'表示读取名为“销售数据”的工作表的数据
    # skiprows=1表示跳过 Excel中的第1行，因为第1行是标题
    # index_col='订单号'表示将“订单号”这一列作为返回的数据框的索引
    # 最后将读取到的数据框赋值给变量 df
    df = pd.read_excel('supermarket_sales.xlsx', 
            sheet_name='销售数据',
            skiprows=1, 
            index_col='订单号'
    )
    # df['时间']取出原有的'时间'这一列，其中包含交易的完整时间字符串，如'10:25：30'
    # pd. to_datetime 将·时间·列转换成 datetime 类型
    # format="용日：M:8S"指定原有时间字符串的格式
    # .dt.hour 表示从转换后的数据框取出小时数作为新列
    # 最后赋值给 sale df[’小时门，这样就可以得到一个包含交易小时的新列
    df['小时数']= pd.to_datetime(df ["时间"],format="%H:%M:%S").dt.hour
    return df

def add_sidebar_func(df):
    # 创建侧边栏
    with st.sidebar:
        # 添加侧边栏标题
        st.header ("请筛选数据：")
        # 求数据框“城市”列去重复后的值，赋值给city_unique
        city_unique = df["城市"].unique()
        city = st.multiselect (
           "请选择城市：",
             options=city_unique,#将所有选项设置为city_unique
             default=city_unique, #第1次的默认选项为city unique
         )
        customer_type_unique=df["顾客类型"].unique()
        customer_type = st.multiselect (
             "请选择顾客类型：",
             options=customer_type_unique,
             default=customer_type_unique,
         )
        gender_unique=df["性别"].unique()
        gender= st.multiselect (
             "请选择性别：",
             options=gender_unique,
             default=gender_unique,
         )
        df_selection=df.query(#query():查询方法，传入过滤条件字符
               "城市==@city&顾客类型==@customer_type&性别==@gender"#通过@可以使用Streamlit多选下拉按钮的值
          )
        return df_selection

def product_line_chart(df):
    sales_by_product_line=(
          df.groupby(by=["产品类型"])[["总价"]].sum().sort_values(by="总价")
    )
    fig_product_sales=px.bar(
          sales_by_product_line,
          x="总价",
          y=sales_by_product_line.index,
          orientation="h",#生成横向条形图
          title="<b>按产品类型划分的销售额</b>",
    )
    return fig_product_sales

def hour_chart(df):
    sales_by_hour=(
         df.groupby(by=["小时数"])[["总价"]].sum()
    )
    fig_hour_sales=px.bar(
          sales_by_hour,
          y="总价",
          x=sales_by_hour.index,
          title="<b>按小时数划分的销售额</b>",
    )
    return fig_hour_sales

def main_page_demo(df):
    st.title(':bar_chart:销售仪表板')
    left_key_col,middle_key_col,right_key_col=st.columns(3)
    total_sales=int(df["总价"].sum())
    average_rating=round(df["评分"].mean(),1)#选中数据框中的“评分”列，使用mean（）计算“评分”列的平均值，使用round（）四舍五入保留一位小数
    star_rating_string=":star:"*int(round(average_rating,0))
    average_sales_by_transaction=round(df["总价"].mean(),2)#保留两位小数

    with left_key_col:
        st.subheader("总销售额：")
        st.subheader(f"RMB ¥ {total_sales:,}")
    with middle_key_col:
        st.subheader("顾客评分的平均值：")
        st.subheader(f"{average_rating} {star_rating_string}")
    with right_key_col:
        st.subheader("每单的平均销售额：")
        st.subheader(f"RMB ¥ {average_sales_by_transaction}")

    st.divider()#水平分割线

    left_chart_col,right_chart_col=st.columns(2)
    with left_chart_col:
        hour_fig=hour_chart(df)
        st.plotly_chart(hour_fig,use_container_width=True)
    with right_chart_col:
        product_fig=product_line_chart(df)
        st.plotly_chart(product_fig,use_container_width=True)

def run_app():
    """启动应用"""
    st.set_page_config(
        page_title="销售仪表板",
        page_icon=":bar_chart:",
        layout="wide"
    )
    sale_df=get_dataframe_from_excel()
    df_selection=add_sidebar_func(sale_df)
    main_page_demo(df_selection)

if __name__=="__main__":
        run_app()