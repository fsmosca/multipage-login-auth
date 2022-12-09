"""Main page
"""


import streamlit as st
from modules.utility import page_setting
from modules.login import Login, get_username, get_users_info
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
    info.information()

    is_login = False
    login = Login()
    # logauth = login.login_auth(auth_token=st.secrets['your_courier_auth_token'])  # streamlit cloud
    logauth = login.login_auth(auth_token='courier_auth_token')

    # Do not crash the app. If auth key is invalid, send an error message.
    try:
        is_login = logauth.build_login_ui()
    except trycourier.exceptions.CourierAPIException:
        st.error('CourierAPIException, email notification might not be supported. Please contact the developer.')

    if is_login:
        # Get user name.
        username = None
        with st.expander('Username', expanded=False):
            username = get_username(logauth)
            st.markdown(f'''
            Welcome user <span style="color: blue;">**{username}!**</span>
            ''',
            unsafe_allow_html=True)

        # Get users info.
        if username == 'ferdz':
            df_users = get_users_info()
            st.dataframe(df_users)


if __name__ == '__main__':
    main()
