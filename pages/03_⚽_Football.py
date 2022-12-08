import streamlit as st 
from modules.utility import page_setting, plot_aggrid, login_warning
from modules.football import Football, get_fifa_ranking


st.session_state.update(st.session_state)


sports = Football()
ball_imoji = 'soccer'
page_setting(
    page_title=f'Sports/{sports.name}',
    icon=f':{ball_imoji}:',
    layout='centered'
)


def main():
    st.title(f'{sports.name.title()} page')

    # Get FIFA ranking.
    st.markdown(f'''
    ### FIFA World Ranking Men
    https://en.wikipedia.org/wiki/FIFA
    ''')
    df = get_fifa_ranking()
    with st.container():
        plot_aggrid(df)
    

if __name__ == '__main__':
    # LOGGED_IN key is defined by streamlit_login_auth_ui in the session state.
    if 'LOGGED_IN' in st.session_state and st.session_state.LOGGED_IN:
        main()
    else:
        login_warning()
