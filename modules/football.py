"""football module

Supports the football page in pages folder.
"""


import streamlit as st
import pandas as pd


class Football:
    def __init__(self):
        self.name = 'Football'
        self.description = '''
        Football is a family of team sports that involve, to varying degrees, kicking a ball to score a goal.
        '''


@st.experimental_singleton
def get_fifa_ranking():
    """Crawl FIFA wiki.
    """
    url = 'https://en.wikipedia.org/wiki/FIFA'
    dfs = pd.read_html(url, header=0)
    df = dfs[9]
    df = df.iloc[2:22]
    df.columns = ['Rank', 'Change', 'Team', 'Points']
    df = df.reset_index(drop=True)
    df = df.rename(columns={"Team": "Country"})
    df = df[['Rank', 'Country', 'Points']]

    return df
