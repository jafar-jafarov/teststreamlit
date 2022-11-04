import streamlit as st
import pandas as pd
import numpy as np
import psycopg2 as pc
import altair as alt
import time
import datetime


option = st.selectbox(
     'What is your favorite color?',
     ('Mavi', 'Qirmizi', 'Yasil'))

st.write('Your favorite color is ', option)

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue'],
     ['Yellow', 'Red'])

st.write('You selected:', options)
st.write('Hello, *World!* :sunglasses:')
st.write(1234)
st.header("Salam")
st.subheader("salam")
st.caption("Captionn")
st.text("ahahah")
st.latex("hahahah")
st.code("elvin  ")
df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)

@st.experimental_singleton
def init_connection():
    return pc.connect(**st.secrets["postgres"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
@st.experimental_memo(ttl=600)
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

#rows = run_query("SELECT patient_name, kys, nurse, request_date, pin, insert_user, insert_date FROM patient;")
#dataframe =rows
#st.dataframe(dataframe)
def load_table_as_dataframe(table):
    
    query=pd.read_sql("SELECT patient_name, kys, nurse, request_date, pin, insert_user, insert_date FROM public.patient;".format(str(table)),conn)
    st.dataframe(query)
    df = pd.DataFrame(query, columns=['patient_name','insert_date'])
    st.bar_chart(df)
df = load_table_as_dataframe("table") 


# Print results.
#for row in rows:
 #   st.write(f"{row[0]} has a :{row[1]}:")

st.write("Hello from Streamlit")

d = st.date_input(
    "When's your birthday",
    datetime.date(2000, 7, 16))
st.write('Your birthday is:', d)
if st.button('Say hello'):
    st.balloons()
else:
    st.balloons()
#dataframe =rows
#st.dataframe(dataframe)

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  #time.sleep(0.1)


  chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)


st.title('🖼️ yt-img-app')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
  st.write('This app retrieves the thumbnail image from a YouTube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://youtu.be/JwSS70SZdyM')

def get_ytid(input_url):
  if 'youtu.be' in input_url:
    ytid = input_url.split('/')[-1]
  if 'youtube.com' in input_url:
    ytid = input_url.split('=')[-1]
  return ytid

# Display YouTube thumbnail image
if yt_url != '':
  ytid = get_ytid(yt_url) # yt or yt_url

  yt_img = f'http://img.youtube.com/vi/{ytid}/{img_quality}.jpg'
  st.image(yt_img)
  st.write('YouTube video thumbnail image URL: ', yt_img)
else:
  st.write('☝️ Enter URL to continue ...')
  
