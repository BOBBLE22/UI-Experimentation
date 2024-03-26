"""
    Streamlit front-end for cyberattack summary
    Author: Alexander Bieniek
    Sources/Inspiration: Wolf Paulus weather.api code
    https://github.com/wolfpaulus/weather_ui/blob/main/app/data.py
"""

# used as a code reference area

'''from pkgutil import get_data
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="World Attack Map",
)

summary = get_data()
periods = summary["properties"]["periods"]

for p in periods:
    p["wind"] = max([int(w) for w in p["windSpeed"].split()])

st.title("World Attack Map")

with st.container(border=True):
    col1, col2, col3 = st.columns(3)
    col1.metric("Country", f"{periods[0]['target countries']} °F")
    col2.metric("Origin", f"{periods[0]['windSpeed']}")
    col3.metric("Humidity", f"{periods[0]['relativeHumidity']['value']} %")

updat_btn = st.sidebar.button("Update", type="primary")
columns = ["isDaytime", "temperature", "name", "wind", "shortForecast"]
chart_data = pd.DataFrame(periods, columns=columns)

st.altair_chart(use_container_width=True, theme=None)'''
