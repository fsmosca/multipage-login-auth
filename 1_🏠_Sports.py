"""Main page
"""


import streamlit as st
from modules.utility import page_setting
from modules.login import Login
import trycourier
from modules.sports import Sports
from streamlit_login_auth_ui.mydeta import deta_db


page_setting(
    page_title='Sports',
    icon=f':sports_medal:',
    layout='centered'
)


def main():
    st.title('Sports page')

    info = Sports()
    is_login = False

    # Saves users info in the deta database.
    db = None
    deta_project_key = st.secrets['Deta_Project_Key']
    deta_db_name = st.secrets['Deta_Db_Name']
    db = deta_db(deta_project_key, deta_db_name)

    users_auth_file = st.secrets['users_auth_file']
    courier_auth_token = st.secrets['courier_auth_token']
    
    login = Login(users_auth_file, courier_auth_token, db)
    logauth = login.login_auth()

    # Do not crash the app. If auth key is invalid, send an error message.
    try:
        is_login = logauth.build_login_ui()
    except trycourier.exceptions.CourierAPIException:
        st.error('CourierAPIException, email notification might not be supported. Please contact the developer.')

    info.information()

    if is_login:
        # Get user name.
        username = None
        with st.expander('Username', expanded=False):
            username = logauth.get_username()
            st.markdown(f'''
            Welcome user <span style="color: blue;">**{username}!**</span>
            ''',
            unsafe_allow_html=True)


if __name__ == '__main__':
    main()
