import streamlit as st
# from flask import Flask, render_template, request ,jsonify,make_response
import streamlit as st
import time
import datetime
from datetime import  time
from datetime import date
import pandas as pd
import sqlite3
import calendar 
from flask_cors import CORS
import numpy as np
import streamlit as st
import configparser
parser = configparser.ConfigParser()
parser.read('config_data_calibration.cfg')
from subprocess import call
import subprocess
# import webbrowser

# from bokeh.models.widgets import Div
# import streamlit as st

# if st.button('Go to Streamlit'):
#     js = "window.open('http://127.0.0.1:5000/foo')"  # New tab or window
#     js = "window.location.href = 'http://localhost:8501/'"  # Current tab
#     html = '<img src onerror="{}">'.format(js)
#     div = Div(text=html)
#     st.bokeh_chart(div)

# st.sidebar.header('ABB Cement App')
# genre = st.sidebar.radio(
# "ABB Cement Selection Panel",
# ('Control Panel', 'Deviation'))

#app.py
import Sub_file1
import Sub_file2
import streamlit as st
PAGES = {
    "Config Data": Sub_file1,
    "Deviation": Sub_file2
}
st.sidebar.header('ABB Cement App')
selection = st.sidebar.radio("ABB Cement Selection Panel", list(PAGES.keys()))
page = PAGES[selection]
page.app()
