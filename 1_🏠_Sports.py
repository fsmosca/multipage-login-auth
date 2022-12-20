"""Main page
"""


import streamlit as st
from modules.utility import page_setting
from modules.login import Login
import trycourier
from modules.sports import Sports


page_setting(
    page_title='Sports',
    icon=f':sports_medal:',
    layout='centered'
)


def main():
    st.title('Sports page')

    info = Sports()
    is_login = False

    users_auth_file = st.secrets['users_auth_file']
    courier_auth_token = st.secrets['courier_auth_token']
    login = Login(users_auth_file, courier_auth_token)
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

        # Get users info.
        if username == 'ferdz':
            df_users = login.get_users_info()
            st.dataframe(df_users)


if __name__ == '__main__':
    main()
