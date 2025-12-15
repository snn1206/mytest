import streamlit as st

st.set_page_config(page_title="电影世界",page_icon="🎥")
st.title('视频播放器')

# 读取视频数据
video_file = [{
	'url':'https://www.w3school.com.cn/example/html5/mov_bbb.mp4',
	'title':'第1集',
	'desc':'动态视频演示，展示高清播放流畅性'
        },{
	'url':'https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4',
	'title':'第2集',
	'desc':'第2集简介'
        },{
	'url':'https://sf1-cdn-tos.huoshanstatic.com/obj/media-fe/xgplayer_doc_video/mp4/xgplayer-demo-360p.mp4',
	'title':'第3集',
	'desc':'第3集简介'
        }
]

# 显示视频
if 'ind' not in st.session_state:
     st.session_state['ind']=0

st.video(video_file[st.session_state['ind']]['url'],autoplay=True)
#显示简介
st.write(f"### {video_file[st.session_state['ind']]['title']} ")
st.write(video_file[st.session_state['ind']]['desc'])

def play(i):
      st.session_state['ind']=int(i)
#换集按钮
cols = st.columns(len(video_file))
for i,col in enumerate(cols):
      with col: 
            st.button('第'+str(i+1)+'集',use_container_width=True,on_click=play, args=([i]))
