import streamlit as st

def set_page_config():
    st.set_page_config(page_title='Savantly Nexus Analytics', page_icon=None, layout='wide', initial_sidebar_state='auto',
                    menu_items={
            'About': """
            ## Savantly Nexus Analytics  
            This is an *extremely* cool app!  
            For support, email us support@savantly.net
            """
        })