import streamlit as st
import pandas as pd

page = st.sidebar.selectbox("选择", ["数字档案","南宁美食数据表","相册","音乐播放器","视频网站"])

if page == "数字档案":
      st.title("数字档案")
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

elif page == "南宁美食数据表":
      st.title("南宁美食数据表")
          # 餐厅数据
      restaurants_data = {
          "餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
          "latitude": [22.853838, 22.965046, 22.812200, 22.809105, 22.839699],
          "longitude": [108.222177, 108.353921, 108.266629, 108.378664, 108.245804]
      }

      #地图
      st.header("🌎地图")
      mp_df=pd.DataFrame(restaurants_data)
      st.map(mp_df)

      st.markdown("***")#分割线

      #条形图
      st.header("⭐️餐厅评分")
      pf_data={
            	"餐厅": ["星艺会尝不忘", "高峰柠檬鸭", "复记老友粉", "好友缘", "西冷牛排店"],
	"评分": [4.2, 4.5, 4.0, 4.7, 4.3]
      }
      pf_df=pd.DataFrame(pf_data)# 根据上面创建的data，创建数据框
      st.bar_chart(pf_df,x='餐厅')# 通过x指定餐厅所在这一列为条形图的x轴
      pf_df.set_index('餐厅', inplace=True)# 修改df，用餐厅列作为df的索引，替换原有的索引

      st.markdown("***")

      #折线图
      st.header("💰️不同类型餐厅价格")
      pr_data={
	"类型": ["快餐", "中餐", "快餐", "自助餐", "西餐"],
	"人均消费(元)": [15, 20, 25, 35, 50],
      }
      pr_df = pd.DataFrame(pr_data)
      st.line_chart(pr_df, x='类型')# 通过x指定餐厅所在这一列为折线图的x轴
      pr_df.set_index('类型', inplace=True)

      #面积图
      st.header("🍽用餐高峰期")
      h_data={
	'月份':['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
	'星艺会尝不忘':[165,156,165,253,461,134,164,135,151,546,615,878],
	'高峰柠檬鸭':[425,324,363,215,455,136,454,133,452,452,458,846],
	'复记老友粉':[546,133,543,611,578,588,544,455,545,761,554,544],
	'好友缘':[543,554,841,123,864,524,468,451,323,586,631,566],
	'西冷牛排店':[233,231,464,354,548,465,564,587,216,125,154,546]
      }
      h_df = pd.DataFrame(h_data)
      st.area_chart(h_df, x='月份')# 通过x指定月份所在这一列为面积图的x轴

      st.markdown("***")

      #价格走势折线图
      st.header("💲价格走势")
      data={
	'月份':['01月','02月','03月','04月','05月','06月','07月','08月','09月','10月','11月','12月'],
	'星艺会尝不忘':[13,12,13,11,14,15,12,13,14,11,13,14],
	'高峰柠檬鸭':[24,21,23,22,21,23,22,22,24,23,21,22],
	'复记老友粉':[16,15,14,17,18,19,14,16,15,17,18,14],
	'好友缘':[23,24,25,25,24,26,24,23,25,24,25,24],
	'西冷牛排店':[45,34,35,43,42,41,40,34,32,39,40,38]
      }
      df = pd.DataFrame(data)
      st.line_chart(df, x='月份')
      df.set_index('月份', inplace=True)

elif page == "相册":
      st.title("相册")
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


elif page == "音乐播放器":
      st.title("音乐播放器")
      st.set_page_config(page_title="简易音乐播放器", page_icon="🎵")

      song_list = [
          {
              "title": "未完结的爱",
              "singer": "Zkaaai",
              "duration": "3:41",
              "cover": "https://picsum.photos/seed/childhood/200/200",        # 专辑封面
              "audio": "https://music.163.com/song/media/outer/url?id=2695903727.mp3"
          },
          {
              "title": "不完美爱情",
              "singer": "杜宣达",
              "duration": "3:30",
              "cover": "https://picsum.photos/seed/rice/200/200",
              "audio": "https://music.163.com/song/media/outer/url?id=3327073434.mp3"
          },
          {
              "title": "亲爱的朋友",
              "singer": "建坤",
              "duration": "2:26",
              "cover": "https://picsum.photos/seed/jasmine/200/200",
              "audio": "https://music.163.com/song/media/outer/url?id=3322330158.mp3"
          }
      ]
      if "current_song_index" not in st.session_state:
           st.session_state.current_song_index = 0

      # 上一首函数
      def pre_song():
          st.session_state.current_song_index = (st.session_state.current_song_index - 1) % len(song_list)

      # 下一首函数
      def next_song():
          st.session_state.current_song_index = (st.session_state.current_song_index + 1) % len(song_list)

      st.title("🎵 音乐播放器")
      st.subheader("Streamlit制作")

      # 显示当前播放的歌曲信息
      current_song = song_list[st.session_state.current_song_index]
      c1, c2 = st.columns([1, 2])
      with c1:
          st.image(current_song["cover"], caption="专辑封面", width=200)
      with c2:
          st.subheader(f"歌曲：{current_song['title']}")
          st.write(f"歌手：{current_song['singer']}")
          st.write(f"时长：{current_song['duration']}")
          c1_pre, c2_next = st.columns(2)
          with c1_pre:
               # 上一首按钮
               st.button("⏮ 上一首", on_click=pre_song,use_container_width=True)
          with c2_next:
                st.button("⏭ 下一首", on_click=next_song,use_container_width=True)


      st.audio(current_song["audio"], format="audio/mp3", start_time=0)

      # 分割线
      st.divider()

else:
      st.title("视频网站")
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