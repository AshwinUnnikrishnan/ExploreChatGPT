import streamlit as st
from config.constants import TITLE, WELCOME_MESSAGE
st.set_page_config(layout="wide")

st.title(TITLE)

st.write(WELCOME_MESSAGE)

