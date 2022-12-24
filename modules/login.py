"""login module

Manages user authentication. It supports sports main page.
"""


import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import json
import pandas as pd


class Login:
    def __init__(self, users_auth_file, courier_auth_token, db):
        self.users_auth_file = users_auth_file
        self.courier_auth_token = courier_auth_token
        self.db = db

    def login_auth(self):
        ret = __login__(
            auth_token=self.courier_auth_token,
            company_name="My company name",
            width=200,
            height=250,
            logout_button_name='Logout',
            hide_menu_bool=False,
            hide_footer_bool=False,
            lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json',
            users_auth_file=self.users_auth_file,
            detadb=self.db
        )
        return ret


    def get_users_info(self):
        with open(self.users_auth_file, 'r') as f:
            data = json.load(f)
        return pd.DataFrame.from_dict(data)
