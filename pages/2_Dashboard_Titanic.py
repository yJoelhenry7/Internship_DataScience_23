import streamlit as st
from matplotlib import image
import os
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

st.set_page_config(page_title="Titanic Dashboard",
                   page_icon=":ship:",
                   layout="wide"
                   )


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "titanic.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "titanic.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

l = ["sex", "alive", "embark_town"]
options = st.selectbox("Select the Option:", l)
col1, col2 = st.columns(2)
bar = df.groupby(options)["survived"].agg("sum").sort_values(ascending=False)
fig1 = px.bar(bar,
              x=bar.index,
              y=bar.values,
              template="plotly_white",
              title="<b> Survived people according to (sex/who/town) </b>",

              color_discrete_sequence=["#AB63FA"]
              )

col1.plotly_chart(fig1, use_container_width=True)

st.markdown("- **in this way we can show barplot**")
st.markdown("- **in the y axis there is count of survive people**")

pie = df.groupby(options)["survived"].agg("sum").sort_values(ascending=False)


# using plotly library
fig2 = px.pie(df, values=pie, names=pie.index,
              title="Survived People at diff Category")
st.plotly_chart(fig2, use_container_width=True)
