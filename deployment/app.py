import streamlit as st
import prediction
from prediction import run
import eda

navigasi = st.sidebar.selectbox('Page Selector :', 
                                ('Home Page','Model Prediksi', 'EDA'))

if navigasi == 'Home Page':
    st.header('Welcome to Home Page!')
    st.write('')
    st.image('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWppejVjNndna2JyZTFrZHJmaTA2cWdvcmt1b3g4NXpyajFsajBqcCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/xT4uQs6eF8OMip7oas/giphy.gif')
    st.write('Milestone 2')
    st.write('Putri Arzalya Maharani')
    st.write('HCK-013')
    st.write('Project ini bertujuan memprediksi apakah nasabah akan menerima tawaran pinjaman pribadi atau sebaliknya')
    st.write('')
    st.caption('Silahkan pilih menu pada Page Selector yang berada di sebelah kiri layar^^')
    st.write('')
    st.write('')

elif navigasi == 'Model Prediksi':
    st.write('Implementasi Model Prediksi')
    prediction.run()

else:
    st.write('Exploratory Data Analysis (EDA)')
    eda.run()