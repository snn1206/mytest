import streamlit as st

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