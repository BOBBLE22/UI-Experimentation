"""
    Obtain Flight Locations
    Author: Alexander Bieniek
    Sources/Inspiration: Wolf Paulus weather.api code
    https://github.com/wolfpaulus/weather_ui/blob/main/app/data.py
"""

import pandas as pd
import streamlit as st
from requests import get

DATA_URL = "https://attackmap.sonicwall.com/live-attack-map/rest/lam-summary/summary.json"

# DATA_FILE = "./app/data/cyber_attacks_summary.json"
DATA_FILE = get(DATA_URL, timeout=3).json()

st.set_page_config(
    page_title="World Attack Map",
)
st.markdown(" # World Cyber Attack Report")

#st.write(DATA_FILE)

st.write(list(DATA_FILE.keys()))

st.write(DATA_URL)

with st.expander("click to view different format"):
    with st.container(border=True):
        col1, col2 = st.columns([1,2])
        for k in DATA_FILE.keys():
            col1.markdown(k)
        for l in DATA_FILE.values():
            col2.markdown(l)


gr = pd.columns = (f"{k}:____________        Values: {l}" for k, l in DATA_FILE.items())
st.table(gr)

