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
# import webbrowser

# from bokeh.models.widgets import Div
# import streamlit as st

# if st.button('Go to Streamlit'):
#     js = "window.open('http://127.0.0.1:5000/foo')"  # New tab or window
#     js = "window.location.href = 'http://localhost:8501/'"  # Current tab
#     html = '<img src onerror="{}">'.format(js)
#     div = Div(text=html)
#     st.bokeh_chart(div)

st.sidebar.header('ABB Cement App')
genre = st.sidebar.radio(
"ABB Cement Selection Panel",
('Control Panel', 'Deviation'))

if genre == 'Control Panel':
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

else:
    
    conn = sqlite3.connect('.///deviation.db',check_same_thread=False)
    c = conn.cursor()
    c.execute('SELECT * FROM Deviations')
    df=pd.DataFrame(c.fetchall(),columns=['tag','start','end'])

    df.sort_values(by=['start'],ascending=False,inplace=True)
    df['start'] = pd.to_datetime(df['start'],unit='ms')
    #print(df["start"])

    for i in  range (len(df)):
        try:
            df['end'].iloc[i] = pd.to_datetime(df['end'].iloc[i],unit='ms')
        except ValueError :
            continue
    df["start"]=df["start"].astype(str)

    st.write("""
    # Deviation Data!
    """)



    st.sidebar.header('Deviation Date Time Picker')

    st.subheader("Deviation Date Time Picker")


    StartDate = st.sidebar.date_input('Start date')
    start_time = st.sidebar.time_input('Select Deviation Start Time ', datetime.time(1, 00))
    st.write('start time',StartDate, start_time)


    EndDate=st.sidebar.date_input('End date')
    end_time= st.sidebar.time_input('Select Deviation End Time', datetime.time(1, 45))
    st.write('end time',EndDate ,end_time)
    end = str(EndDate)+" "+str(end_time)
    start =  str(StartDate)+" "+str(start_time)
    #st.write("end  start",end,start)
    def get_date_from_html(start,end):
        
        start_time= start
        end_time= end
        conn = sqlite3.connect('.///deviation.db',check_same_thread=False)
        c = conn.cursor()
        c.execute('SELECT * FROM Deviations')
        df=pd.DataFrame(c.fetchall(),columns=['tag','start','end'])
        df.set_index('tag',inplace=True)
        df = df.replace({"NULL":None})
        df = df.replace({None:np.nan})
        df['end'] = df['end'].astype('Int64')

        df['start']= df['start'].astype('Int64')

        def epoch_time(x):
            format = '%Y-%m-%d %H:%M:%S' # The format 
            time = x
            datetime_str = datetime.datetime.strptime(time, format) 
            epoch = calendar.timegm(datetime_str.timetuple())
            return (epoch)
        start_time = epoch_time(start_time)
        end_time = epoch_time(end_time)

        start_time = start_time*1000
        end_time = end_time * 1000
        dk=df[df['start']>=start_time] 
        dk= dk[dk['end']<= end_time]

        dk['start'] = pd.to_datetime(dk['start'],unit='ms')
        dk['end'] = pd.to_datetime(dk['end'],unit='ms')
        df["start"].astype(str)
        df["end"].astype(str)
        dk.reset_index(inplace=True)

        # user = dk.values.tolist()
        return dk

    dk=get_date_from_html(start,end)
    st.write("Data with Start and End Time")
    st.dataframe(dk)


















    st.write("Complete Data")
    st.dataframe(data=df, width=9000)




    df_concat = pd.DataFrame()
    df_concat["period"] = df["tag"].astype(str) +" |"+ df["start"].astype(str)+" |"+df["end"].astype(str)
    df_concat["period"] = df_concat["period"].astype(object)
    k=df_concat["period"].tolist()

    option = st.selectbox('Select the Data to see Graph!',k)

    st.write('You selected: ', option)
    # print(option)








    #Tag list for selecting data from deviation
    df["tag"]=df["tag"].astype(str)
    tag_list = df["tag"].unique()
    tag_list.sort()
    #tag_list.sort()
    #print(df["tag"].unique())
    #st.write('tags', tag_list)
    tag_name = st.selectbox('Select the Tag to see Data!',tag_list)

    st.write('You selected: ', tag_name)

    st.dataframe(df[df["tag"]==tag_name])






    #Data Ploting Change the values accordingly to plot the graph.Here i have used random data for plotting. 

    import streamlit as st
    import plotly.figure_factory as ff
    import numpy as np
    import plotly.express as px
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig1 = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])
    fig = px.line(hist_data, x=x1, y=x2, )
    # Plot!
    st.plotly_chart(fig1, use_container_width=True)

    st.plotly_chart(fig, use_container_width=True)

