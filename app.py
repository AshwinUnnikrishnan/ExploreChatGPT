import streamlit as st
from config import constants
from config import widget_key
from frontend.main_screen import main_UI
st.set_page_config(layout="wide")

st.title(constants.TITLE)
st.write(constants.WELCOME_MESSAGE)


def app():
    main_UI()



if __name__ == "__main__":
    if widget_key.OPEN_AI_API_KEY_DATA not in st.session_state:
        st.session_state[widget_key.OPEN_AI_API_KEY_DATA] = constants.OPEN_AI_API_KEY
    
    app()
