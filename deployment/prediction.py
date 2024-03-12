import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

model_path = os.path.abspath('model.pkl')
# load model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.set_page_config(
    page_title='Prediksi Penerimaan Pinjaman Pribadi'
)

def run():
    st.title('Personal Loan Prediction')

    st.header('Isi form untuk memprediksi')
    st.markdown('---')

# membuat form untuk data inference
    st.subheader('Input Data Nasabah')

    with st.form('form'):
        Age = st.number_input('Usia Pelanggan (Tahun)', format='%d', step=1)
        Experience = st.number_input('Pengalaman Profesional (Tahun)', format='%d', step=1)
        Income = st.number_input('Pendapatan Tahunan($)', format='%d', step=1)
        ZIP_Code = st.number_input('Kode Pos Alamat Rumah', format='%d', step=1)
        Family = st.number_input('Jumlah Anggota Keluarga', format='%d', step=1)
        CCAvg = st.number_input('Rata-rata Pengeluaran Kartu Kredit per Bulan ($1000)')
        Education = st.selectbox('Jenjang Pendidikan', [1, 2, 3, 4])
        Mortgage = st.number_input('Nilai Hipotek Rumah($)', format='%d', step=1)
        Securities_Account = st.selectbox('Rekening Surat Berharga', {0: 'Tidak', 1: 'Ya'})
        CD_Account = st.selectbox('Rekening Sertifikat Deposito (CD)', {0: 'Tidak', 1: 'Ya'})
        Online = st.selectbox('Penggunaan Fasilitas Internet Banking', {0: 'Tidak', 1: 'Ya'})
        Credit_Card = st.selectbox('Penggunaan Kartu Kredit Bank', {0: 'Tidak', 1: 'Ya'})

        submit = st.form_submit_button('Predict Default')

    data_baru = {
        'Age': Age,
        'Experience': Experience,
        'Income': Income,
        'ZIP Code': ZIP_Code,
        'Family': Family,
        'CCAvg': CCAvg,
        'Education': Education,
        'Mortgage': Mortgage,
        'Securities Account': Securities_Account,
        'CD Account': CD_Account,
        'Online': Online,
        'CreditCard': Credit_Card
    }

    data_inf = pd.DataFrame([data_baru])

    st.dataframe(data_inf)

    if submit:
        score = model.predict(data_inf)
        if score == 0:
            st.write('### Prediksi penerimaan pinjaman pribadi:')
            st.text('Nasabah ini diprediksi tidak akan menerima tawaran pinjaman pribadi.')
        else:
            st.write('### Prediksi penerimaan pinjaman pribadi:')
            st.text('Nasabah ini diprediksi akan menerima tawaran pinjaman pribadi.')

if __name__ == "__main__":
    run()