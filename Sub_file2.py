# app2.py
import streamlit as st
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
# from flask_cors import CORS
import numpy as np
import streamlit as st
import configparser
parser = configparser.ConfigParser()
parser.read('config_data_calibration.cfg')
from subprocess import call
import subprocess
































def app():
    import streamlit as st
    import streamlit as st
#     from flask import Flask, render_template, request ,jsonify,make_response
    import streamlit as st
    import time
    import datetime
    from datetime import  time
    from datetime import date
    import pandas as pd
    import sqlite3
    import calendar 
#     from flask_cors import CORS
    import numpy as np
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

    st.write(""" Deviation Data!""")



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

#         dk['start'] = pd.to_datetime(dk['start'],unit='ms')
#         dk['end'] = pd.to_datetime(dk['end'],unit='ms')
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
    import plotly
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

