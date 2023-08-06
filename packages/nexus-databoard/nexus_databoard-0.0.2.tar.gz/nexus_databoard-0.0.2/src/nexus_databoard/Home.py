from common import config, page_config
import streamlit as st

page_config.set_page_config()

cfg = config.Config()

st.header(cfg.app_name)
st.write(cfg.app_description)