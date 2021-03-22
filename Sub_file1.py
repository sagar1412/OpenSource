import streamlit as st
from flask import Flask, render_template, request ,jsonify,make_response
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



# app1.py
import streamlit as st
def app():


    st.title("Config Data")

    #lets try a both a text input and area as well as a date
    historytype_fetch_data = (st.text_input('Enter HistoryType for fetching raw data '))
    historytype_save_data_types = (st.text_input('Enter HistoryType for saving Shapes data'))
    subset_method_std_tag = (st.text_input('Enter subset method standard tag'))
    phantom_rolling_tag = (st.text_input('Enter Phantom rolling signal tag'))
    cobble_signals = (st.text_input('Enter cobble signals as a list contaning strings'))
    url_fetch_data = (st.text_input('Enter data fetch url'))
    url_save_data = (st.text_input('Enter data save url'))
    historytype_save_data_risk = (st.text_input('Enter HistoryType for saving Risk data'))
    historytype_save_data_plantrisk = (st.text_input('Enter HistoryType for saving Plantrisk data'))
    risk_time_period = (st.text_input('Enter time span to calculate riskscore'))
    no_of_billets_processed = (st.text_input('Enter number of billets to be processed for clustering '))
    plantrisk_property = (st.text_input('Enter property to save plantrisk to '))
    billets_to_be_sampled = (st.text_input('Enter number of billets to be sampled for probability distribution '))
    number_of_clusters_stands = (st.text_input('Enter number of clusters of shapes for stands '))
    number_of_clusters_shear = (st.text_input('Enter number of clusters of shapes for shear and pinchroll '))  
    model_version = (st.text_input('Enter model version to be used for computation ')) 
    opening_condition_low_threshold = (st.text_input('Enter opening threshold for deviations (0-1) '))
    opening_condition_mid_threshold = (st.text_input('Enter mid threshold for deviations (0-1) '))
    opening_condition_high_threshold = (st.text_input('Enter high threshold for deviations (0-1) '))
    window_size = (st.text_input('Enter window size for detecting deviations '))
    proxy = (st.text_input('Enter proxy url address '))
    stand_tags = (st.text_input('Enter Stand-wise tags in the format {1: {"tags": ["Plants.Profile.St1.SpeedActual","Plants.Profile.St1.TorqueActual","Plants.Profile.St1.Voltage"]} '))
    standrisk_tags = (st.text_input('Enter Stand-wise tags in the format {1:"Plants.Profile.St1.RiskScore",...} '))


    #date = list(st.date_input('Your birthday', start_date))

    if st.button('Submit'):
        if historytype_fetch_data == '':
            pass
        else:
            parser.set('Config_data', 'historytype_fetch_data', historytype_fetch_data)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if historytype_save_data_types == '':
            pass
        else:
            parser.set('Config_data', 'historytype_save_data_types', historytype_save_data_types)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)
                
        if subset_method_std_tag == '':
            pass
        else:
            parser.set('Config_data', 'subset_method_std_tag', subset_method_std_tag)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if phantom_rolling_tag == '':
            pass
        else:
            parser.set('Config_data', 'phantom_rolling_tag', phantom_rolling_tag)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if cobble_signals == '':
            pass
        else:
            parser.set('Config_data', 'cobble_signals', cobble_signals)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if url_fetch_data == '':
            pass
        else:
            parser.set('Config_data', 'url_fetch_data', url_fetch_data)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if url_save_data == '':
            pass
        else:
            parser.set('Config_data', 'url_save_data', url_save_data)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)
        
        if historytype_save_data_risk == '':
            pass
        else:
            parser.set('Config_data', 'historytype_save_data_risk', historytype_save_data_risk)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)
        
        if historytype_save_data_plantrisk == '':
            pass
        else:
            parser.set('Config_data', 'historytype_save_data_plantrisk', historytype_save_data_plantrisk)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)
        
        if risk_time_period == '':
            pass
        else:
            parser.set('Config_data', 'risk_time_period', risk_time_period)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)
        
        if no_of_billets_processed == '':
            pass
        else:
            parser.set('Config_data', 'no_of_billets_processed', no_of_billets_processed)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if plantrisk_property == '':
            pass
        else:
            parser.set('Config_data', 'plantrisk_property', plantrisk_property)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if billets_to_be_sampled == '':
            pass
        else:
            parser.set('Config_data', 'billets_to_be_sampled', billets_to_be_sampled)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if number_of_clusters_stands == '':
            pass
        else:
            parser.set('Config_data', 'number_of_clusters_stands', number_of_clusters_stands)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if number_of_clusters_shear == '':
            pass
        else:
            parser.set('Config_data', 'number_of_clusters_shear', number_of_clusters_shear)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if model_version == '':
            pass
        else:
            parser.set('Config_data', 'model_version', '_v_'+model_version)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if opening_condition_low_threshold == '':
            pass
        else:
            parser.set('Config_data', 'opening_condition_low_threshold', opening_condition_low_threshold)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if opening_condition_mid_threshold == '':
            pass
        else:
            parser.set('Config_data', 'opening_condition_mid_threshold', opening_condition_mid_threshold)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if opening_condition_high_threshold == '':
            pass
        else:
            parser.set('Config_data', 'opening_condition_high_threshold', opening_condition_high_threshold)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if window_size == '':
            pass
        else:
            parser.set('Config_data', 'window_size', window_size)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)
            
        if proxy == '':
            pass
        else:
            parser.set('Config_data', 'proxy', proxy)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if stand_tags == '':
            pass
        else:
            parser.set('Config_data', 'stand_tags', stand_tags)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        if standrisk_tags == '':
            pass
        else:
            parser.set('Config_data', 'standrisk_tags', standrisk_tags)
            with open('config_data_calibration.cfg', 'w') as configfile:
                parser.write(configfile)

        st.write("Updated")
# 




