import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av

class EmotionProcessor:
    def recv(self, frm):
        frame = frm.to_ndarray(format="bgr24")

        return av.VideoFrame.from_ndarray(frame, format="bgr24")

lang = st.text_input("Language")
singer = st.text_input("singer")

if lang and singer:
    webrtc_streamer(key="key", desired_playing_state=True,
    video_processor_factory=EmotionProcessor)

btn = st.button("Recommend me songs")


