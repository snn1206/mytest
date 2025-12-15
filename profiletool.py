import streamlit as st
from datetime import time

#修改标签页的文字和图标
st.set_page_config(page_title="个人简历生成器",page_icon="",layout="wide")



c1,c2=st.columns([1,2])#分成两列，比例1：2
with c1:
      user_name=st.text_input('姓名')
      user_age=st.number_input('年龄',min_value=20, max_value=60, value=20)#年龄区间20~60，默认20
      job=st.text_input('工作')
      num=st.text_input('电话')
      email=st.text_input('邮箱')
      date = st.date_input("出生日期", value=None)
      sex=st.radio('性别',['女','男','其他'],label_visibility='visible')# 设置为默认，水平排列
      education=st.selectbox('学历：',['大专','本科','研究生','博士'],index=1)#单选下拉框
      languages=st.multiselect('语言能力', ['中文', '英语', '德语', '日语', '法语'],['英语'], max_selections=2)#多选下拉框，最多选两个
      skill=st.multiselect('技能', ['无','python', '数据库', 'java', 'web', 'c语言'],['无'])
      experience=st.slider('工作经验(年)', 0, 40, 5) #数值滑块
      pay=st.slider('期望薪资(元)', 3000, 40000, (5000,7000)) #范围滑块
      init_text = "这个人什么都没留下"
      about=st.text_area(label='个人简介：', placeholder='请输入您的个人简介',value=init_text,height=200, max_chars=200)
      time_contact=st.time_input('每日最佳联系时段',time(8, 45))
      photo=st.file_uploader("上传个人照片", type=['jpg', 'png', 'jpeg'])#上传照片，支持jpg、png、jpeg格式

with c2:
      st.title("简历预览")
      st.header(user_name)
      c3,c4=st.columns(2)
      with c3:
          if photo:
                st.image(photo, width=200)
          st.write("年龄:",user_age,"岁")
          st.write("工作：",job)
          st.write("电话：",num)
          st.write("邮箱：",email)
          st.write("学历：",education)
      with c4:
          st.write("出生日期：",date)
          st.write("性别：",sex)

          st.write("语言能力：",", ".join(languages))
          st.write("工作经验：",experience,"年")
          st.write("期望薪资：",pay,"元")
          st.write("每日最佳联系时段：",time_contact)

      st.markdown("***")
      st.header("个人简介")
      st.write(about)
      st.header("技能" )
      st.write(", ".join(skill))

      st.markdown("***")
      