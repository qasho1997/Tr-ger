import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title='Trägerkalkulation', layout='wide')

st.title('Beam Calculator')

inputCol, graphCol = st.columns([1, 3])

with inputCol:
    with st.form('input'):
        firstspanlenght = st.number_input('span 1', value=3.0)


