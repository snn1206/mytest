import streamlit as st
import pandas as pd

st.set_page_config(page_title="相册",page_icon="🐈")
st.title("我的相册")

if 'ind' not in st.session_state:
	st.session_state['ind']=0

images=[
          {
	'url':"https://cdn.pixabay.com/photo/2023/07/05/04/45/european-shorthair-8107433_1280.jpg",
	'text':"猫"
           },{
	'url':"https://pica.zhimg.com/v2-27588ebcf916bbc6fc47c36971efc70f_720w.jpg?source=172ae18b",
	'text':"狗"
           },{
	'url':"https://img.shetu66.com/2023/11/19/1700386999855512.jpg",
	'text':"鸟"
           }]

st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['text'])

def nextImg():
	st.session_state['ind']=(st.session_state['ind']+1)%len(images)

c1,c2=st.columns(2)
with c1:
	st.button("上一张",on_click=nextImg,use_container_width=True)
with c2:
	st.button("下一张",on_click=nextImg,use_container_width=True)