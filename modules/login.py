"""login module

Manages user authentication. It supports sports main page.
"""


import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import json
import pandas as pd


class Login:
    def __init__(self):
        pass

    def login_auth(self, auth_token='courier_auth_token'):
        ret = __login__(
            auth_token=auth_token,
            company_name="My company name",
            width=200,
            height=250,
            logout_button_name='Logout',
            hide_menu_bool=False,
            hide_footer_bool=False,
            lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json'
        )
        return ret


def get_username(logauth):
    if not st.session_state['LOGOUT_BUTTON_HIT']:
        fetched_cookies = logauth.cookies
        if '__streamlit_login_signup_ui_username__' in fetched_cookies.keys():
            username = fetched_cookies['__streamlit_login_signup_ui_username__']
            return username


def get_users_info():
    with open('_secret_auth_.json') as f:
        data = json.load(f)
    
    return pd.DataFrame.from_dict(data)
