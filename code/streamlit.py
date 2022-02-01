import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import pandas as pd
import sqlite3
import config
import pandas as pd
import numpy as np

import plotly.graph_objects as go
from plotly import tools
import plotly.offline as py
import plotly.express as px

#### DB CONNECTION #############
connection = sqlite3.connect(config.DB_FILE)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()

cursor.execute("""SELECT * FROM tesla""")
cursor.fetchall()

df = pd.read_sql_query("""SELECT * FROM tesla""", connection)
####################################
# Set Page Configure ###############

html_header = """
<head>
<title>PControlDB</title>
<meta charset="utf-8">
<meta name="keywords" content="project control, dashboard, management, EVA">
<meta name="description" content="project control dashboard">
<meta name="author" content="Larry Prato">
<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<h1 style="font-size:300%; color:white; font-family:Georgia"> TSLA Sentiment <br>
 <h2 style="color:white; font-family:Georgia"> DASHBOARD</h3> <br>
 <hr style= "  display: block;
  margin-top: 0.5em;
  margin-bottom: 0.5em;
  margin-left: auto;
  margin-right: auto;
  border-style: inset;
  border-width: 1.5px;"></h1>
"""

st.set_page_config(page_title=" Stock Sentiment Dashboard",
                   page_icon="", layout="wide")
st.markdown(
    '<style>body{background-color: #fbfff0}</style>', unsafe_allow_html=True)
st.markdown(html_header, unsafe_allow_html=True)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

html_card_header1 = """
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#e67958; font-family:Georgia; text-align: center; padding: 0px 0;">Polarity Mean</h3>
  </div>
</div>
"""
html_card_footer1 = """
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Baseline 46%</p>
  </div>
</div>
"""
html_card_header2 = """
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#e67958; font-family:Georgia; text-align: center; padding: 0px 0;">Polarity Stan. Dev.</h3>
  </div>
</div>
"""
html_card_footer2 = """
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">Baseline 92.700</p>
  </div>
</div>
"""
html_card_header3 = """
<div class="card">
  <div class="card-body" style="border-radius: 10px 10px 0px 0px; background: #eef9ea; padding-top: 5px; width: 350px;
   height: 50px;">
    <h3 class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">TCPI</h3>
  </div>
</div>
"""
html_card_footer3 = """
<div class="card">
  <div class="card-body" style="border-radius: 0px 0px 10px 10px; background: #eef9ea; padding-top: 1rem;; width: 350px;
   height: 50px;">
    <p class="card-title" style="background-color:#eef9ea; color:#008080; font-family:Georgia; text-align: center; padding: 0px 0;">To Complete Performance Index ≤ 1.00</p>
  </div>
</div>
"""
##########################################################

polarity_mean = round(df['polarity'].mean(), 3)

polarity_sd = round(df['polarity'].std(), 3)

### Block 1#########################################################################################
with st.container():
    col1, col2, col3, col4, col5, col6, col7 = st.columns(
        [1, 15, 1, 15, 1, 15, 1])
    with col1:
        st.write("")
    with col2:
        st.markdown(html_card_header1, unsafe_allow_html=True)
        fig_c1 = go.Figure(go.Indicator(
            mode="number",
            value=polarity_mean,
            number={"font": {"size": 40,
                             'color': "#008080", 'family': "Arial"}},
            #delta={'position': "bottom", 'reference': 46, 'relative': False},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c1.update_layout(autosize=False,
                             width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#262c32", font={'size': 20})
        st.plotly_chart(fig_c1)
       # st.markdown(html_card_footer1, unsafe_allow_html=True)
    with col3:
        st.write("")
    with col4:
        st.markdown(html_card_header2, unsafe_allow_html=True)
        fig_c2 = go.Figure(go.Indicator(
            mode="number",
            value=polarity_sd,
            number={"font": {
                "size": 40, 'color': "#008080", 'family': "Helvetica"}},
            delta={'position': "bottom", 'reference': 92700},
            domain={'x': [0, 1], 'y': [0, 1]}))
        fig_c2.update_layout(autosize=False,
                             width=350, height=90, margin=dict(l=20, r=20, b=20, t=30),
                             paper_bgcolor="#262c32", font={'size': 20})
        fig_c2.update_traces(delta_decreasing_color="#3D9970",
                             delta_increasing_color="#FF4136",
                             delta_valueformat='f',
                             selector=dict(type='indicator'))
        st.plotly_chart(fig_c2)
        #st.markdown(html_card_footer2, unsafe_allow_html=True)
    with col5:
        st.write("")

    with col7:
        st.write("")
html_br = """
<br>
"""
st.markdown(html_br, unsafe_allow_html=True)

####################################################
# st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:50px !important;
    font-family: Georgia;

}
.figure{
    font-size:30px !important;
    font-family: Georgia;
    font-size: 2.4rem;

}

.figure2{
    font-size:10px !important;
    font-family: Georgia;

}




</style>
""", unsafe_allow_html=True)

#st.markdown('<p class="big-font">TSLA Sentiment </p>', unsafe_allow_html=True)
######################################


polarity_mean = round(df['polarity'].mean(), 3)

polarity_sd = round(df['polarity'].std(), 3)


##########################################

#Tesla = df[df['Tesla'] == 1][['Timestamp', 'polarity']]
MA_df = df.sort_values(by='Timestamp', ascending=True)

MA_df['MA Polarity'] = MA_df.polarity.rolling(10, min_periods=10).mean()


####################################
# Plot 1
#####################################
with st.expander("See explanation"):
    st.write("""
         This module gives a sentiment score for Twitter mentions of various stock symbols. A score of 1 means that the sentiment plurality is positve.  A score of -1 indicates a negative connotaion.
         1000 tweets are anaylized once per hour.
     """)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
fig = px.scatter(df,
                 x="Timestamp", y="polarity", hover_data=['Processed Tweet'], trendline='rolling', trendline_options=dict(window=10), trendline_color_override="white", color='polarity', title='Polarity (-1 Negative 0 Neutral 1 Positive)')
fig.update_layout(
    font_family="Helvetica",
    font_color="white",
    title_font_family="Georgia",
    title_font_color="white",
    legend_title_font_color="white"
)

fig.update_xaxes(title_font_family="Helvetica")

st.plotly_chart(fig)

#fig2 = px.line(MA_df, x='Timestamp', y='MA Polarity')
# st.plotly_chart(fig2)
# st.write(df)
# st.write(df2)
