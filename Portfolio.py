import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from pathlib import Path
cur_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
prof_pic = cur_dir / "assets" / "profile.jpg"
PROJECTS = {
    "🏆 Ecommerce-Website (Build With Express Js and Firebase)": "https://github.com/yJoelhenry7/Ecommerce-Website",
    "🏆 Translate-Text (Andriod-Translator-App)": "https://github.com/yJoelhenry7/TranslateText",
    "🏆 Youtube Video-To-Mp3 Bot (Telegram Bot)": "https://github.com/yJoelhenry7/Yotube-Video-to-Mp3-Bot"}


st.header("My :red[portfolio] :sunglasses:")
st.write("")
img = Image.open(prof_pic)
col1, col2 = st.columns([10, 7])
with col1:
    st.image(img)
with col2:
    st.header("Joel Henry")
    st.caption("Full Stack || Data Science || Machine Learning")
    st.write(
        "I am Joel Henry Currently Doing My Bachelor's Degree in Vishnu Institute of Technology in the Stream of Artificial Intelligence and Data science .I have a strong foundation in HTML, CSS, and JavaScript, as well as experience working with Node.js and Express.js. In addition, I have experience with programming languages such as Python and Java. I am proficient in using tools such as Git, VS Code, Jupyter, and Colab Notebook. I am passionate about creating dynamic, user-friendly web applications that meet the needs of both clients and end-users. I am also currently learning data Science, Machine Learning , NLP and I am excited to apply my skills in this area to future projects."
    )


st.subheader("my_skills = {")
st.write(
    """
  'Programming': ['Python','Java','JavaScript'], \n
  'Data Visualization' : ['Plotly', 'Seaborn', 'Matplotlib'], \n
  'Frameworks' : ['FastAPI', 'Dash', 'Django'], \n
  'Python Library' :  ['numpy', 'opencv', 'pandas','requests'],\n
  'Databases':  Postgre SQL,Mongo DB \n
 'Other Skills': ['Git', 'Github','Firebase']\n
    """
)
st.subheader("   }")
st.subheader("Work Experience : ")
st.write("---")
st.write("Full Stack Web Development Intern")
st.write("09/2022 - 11/2022")
st.write(
    """
- ► Worked On Ecommerce Website and Created a Full-Stack Ecommerce web Application
- ► Got Internship Experience Certificate
"""

)

st.write("\n")
st.subheader("Projects :")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
st.write("\n")
columns = st.columns(5)
columns[0].button('Full Stack')
columns[1].button('Andriod Development')
columns[2].button("Data Science")
columns[3].button("Data Analytics")
