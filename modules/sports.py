import streamlit as st


class Sports:
    def __init__(self):
        pass

    def information(self):
        st.markdown(f'''
        ##### Objective
        This app is a demo on how to use
        [streamlit](https://github.com/streamlit/streamlit)
        multipages feature and
        [streamlit-login-auth-ui](https://github.com/GauriSP10/streamlit_login_auth_ui)
        package used to authenticate a user. The main page is
        <span style="color: magenta;">**sports**</span> with subpages
        <span style="color: magenta;">**basketball**</span>
        and <span style="color: magenta;">**football**</span>.

        The `pages` folder has
        `02_🏀_Basketball.py` and `03_⚽_Football.py` files. This app also has
        `modules` folder that contains `baskeball.py`, `football.py` and other
        files that support the files in the pages folder. The **class** and
        **functions** from these files are imported to the files in `pages` folder.
        The basketball and football pages have the FIBA and FIFA ranking list
        respectively. They can only be seen when a user is logged in.
        The source code of this app can be found in my
        [github](https://github.com/fsmosca/multipage-login-auth) repository.
        ##### Authentication
        If a <span style="color: magenta;">**Logout**</span> button appears
        in the sidebar on this page, that means a user is logged in.
        To log in, a user has to **create an
        account** and use the username and password. Username, password
        and <span style="color: magenta;">**email**</span> are important.
        The **email** is used when a user forgets the password.
        [argon2-cffi](https://pypi.org/project/argon2-cffi/) manages the
        password hashing.
        The user info along with the hashed password is saved in the file
        `_secret_auth_.json` under the streamlit project folder.
        ##### The courier service
        [Courier](https://www.courier.com/) handles the email notification
        when user forgets the password. It will send a temporary password
        to the user via the email specified by the user during account
        creation. The user can then reset the password.
        The **developer** should register in Courier site in order to get the
        **courier-auth-token** so that the email notification will work. There is
        a [free tier](https://www.courier.com/pricing/) with a decent number
        of messages to use per month. It is fine not to register though,
        <span style="color: magenta;">**streamlit-login-auth-ui**</span>
        still allows account creation and user log in/out.
        ''',
        unsafe_allow_html=True)