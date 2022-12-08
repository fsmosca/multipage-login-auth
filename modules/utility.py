"""utility module

Handles streamlit-aggrid to support the pages.
"""


import streamlit as st
from st_aggrid import GridOptionsBuilder, AgGrid
from st_aggrid.shared import AgGridTheme


def page_setting(page_title='', icon=':smile:', layout='centered'):
    """Uses streamlit's set_page_config function."""
    st.set_page_config(
        page_title=page_title,
        page_icon=icon,
        layout=layout
    )


def plot_aggrid(df):
    """Prints table using aggrid."""
    df = df.astype({"Rank": int, "Points": float})

    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(min_column_width=4,
                                editable=False)
    gb.configure_column("Points",
                        type=["numericColumn","numberColumnFilter",
                              "customNumericFormat"],
                        precision=2)
    gridOptions = gb.build()
    AgGrid(
        df,
        theme=AgGridTheme.STREAMLIT,
        height=400,
        gridOptions=gridOptions,
        fit_columns_on_grid_load=False,
        enable_enterprise_modules=False
    )


def login_warning():
    """Shows a message as user warning."""
    st.markdown('''
    Please **log in** at **Sports** page to view the contents of this page.
    ''')
