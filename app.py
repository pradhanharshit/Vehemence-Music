import streamlit as st
from multiapp import MultiApp
from apps import login_signup
app = MultiApp()

app.add_app("Home", login_signup.main)
app.run()

