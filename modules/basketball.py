"""basketball module

Supports the basketball page in pages folder.
"""


import streamlit as st
import pandas as pd


class Basketball:
    def __init__(self):
        self.name = 'Basketball'
        self.description = '''
        Basketball is a team sport in which two teams, most commonly of five players each,
        opposing one another on a rectangular court, compete with the primary objective of
        shooting a basketball through the defender's hoop
        '''


@st.experimental_singleton
def get_fiba_ranking():
    """Crawl FIBA official site.
    """
    url = "https://www.fiba.basketball/rankingmen"
    dfs = pd.read_html(url)[0]
    df = dfs[['World rank', 'Country', 'Current points']]
    df = df.rename(columns={"World rank": "Rank", "Current points": "Points"})

    return df
