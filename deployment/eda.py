import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Personal Loan EDA"
)

# Function untuk menjalankan streamlit model predictor
def run():
    # Set title
    st.title('Personal Loan : Exploratory Data Analysis')

    # Load dataset
    data = pd.read_csv("P1M2_Putri_Arzalya_Dataset.csv")

    # Pemisah (garis-garis)
    st.markdown('----')

    # Check Imbalanced Data
    positive_count = data[data['Personal Loan'] == 1].shape[0]
    negative_count = data[data['Personal Loan'] == 0].shape[0]

    labels = 'Ya', 'Tidak'
    sizes = [positive_count, negative_count]
    explode = (0, 0)
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Berapa banyak pelanggan yang menerima pinjaman pribadi yang ditawarkan pada kampanye terakhir?")
    st.pyplot(fig1)
    st.write("Berdasarkan diagram pie, kita dapat melihat bahwa sekitar 9.6% dari total nasabah menerima pinjaman pribadi yang ditawarkan pada kampanye terakhir, sementara 90.4% sisanya tidak menerima pinjaman tersebut. Ini memberikan pemahaman yang jelas tentang efektivitas kampanye pemasaran sebelumnya dalam mendorong konversi pinjaman pribadi. Dengan memahami bahwa hanya sebagian kecil nasabah yang menerima tawaran pinjaman pribadi, manajemen bank dapat melihat kesempatan untuk meningkatkan rasio konversi dalam kampanye pemasaran berikutnya. Strategi pemasaran yang lebih cermat dan target dapat membantu dalam meningkatkan persentase nasabah yang menerima tawaran pinjaman.")

    # Pemisah (garis-garis)
    st.markdown('----')

    # Took personal loan by education
    # Group data berdasarkan kolom 'Education' dan hitung jumlah nasabah yang mengambil pinjaman pribadi
    loan_by_education = data.groupby('Education')['Personal Loan'].sum().reset_index()
    # Membuat bar plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Education', y='Personal Loan', data=loan_by_education, palette='viridis')
    # Menambahkan label dan judul
    plt.xlabel('Pendidikan')
    plt.ylabel('Jumlah Nasabah')
    plt.title('Jumlah Nasabah yang Mengambil Pinjaman Pribadi berdasarkan Pendidikan')
    # Menambahkan legenda
    legend_labels = ['Undergraduate', 'Graduate', 'Advanced/Professional']
    colors = sns.color_palette('viridis', len(legend_labels))
    legend_handles = [plt.Rectangle((0,0),1,1, color=colors[i]) for i in range(len(legend_labels))]
    # Menampilkan legenda
    plt.legend(legend_handles, legend_labels)
    # Mendapatkan objek gambar saat ini
    fig_education_loan = plt.gcf()
    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig_education_loan)
    st.write("Nasabah dengan tingkat pendidikan 'Advanced/Professional' memiliki jumlah pinjaman pribadi yang paling tinggi, diikuti oleh nasabah dengan tingkat pendidikan 'Graduate' dan 'Undergraduate'. Ini menunjukkan bahwa nasabah dengan tingkat pendidikan yang lebih tinggi cenderung lebih cenderung untuk mengambil pinjaman pribadi. Manajemen bank dapat memanfaatkan informasi ini untuk mengarahkan strategi pemasaran mereka. Misalnya, dapat menargetkan kampanye pemasaran pinjaman pribadi pada nasabah dengan tingkat pendidikan yang lebih tinggi karena cenderung memiliki kecenderungan untuk mengambil pinjaman tersebut.")

    # Pemisah (garis-garis)
    st.markdown('----')

    # Income in a year
    plt.hist(data['Income'], bins=20, color='orange', edgecolor='black')
    plt.xlabel('Pendapatan Tahunan')
    plt.ylabel('Frekuensi')
    plt.title('Histogram Pendapatan Tahunan')
    # Mendapatkan objek gambar saat ini
    fig_income_hist = plt.gcf()
    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig_income_hist)
    st.write("Sumbu x pada histogram mewakili kategori-kategori atau interval-interval pendapatan tahunan, di mana setiap nilai mewakili kelompok tertentu dari pendapatan nasabah. Diketahui pendapatan tahunan nasabah pada Bank Thera berada di interval kurang dari 50 hingga lebih dari 50. Akan tetapi dari interval-interval ini dapat membantu mengidentifikasi seberapa banyak nasabah yang berada dalam setiap kategori pendapatan sehingga apakah mayoritas nasabah berada dalam kategori pendapatan rendah, sedang, atau tinggi. Hal ini dapat memberikan wawasan penting untuk strategi pemasaran dan pengambilan keputusan di bank tersebut.")
    
    # Pemisah (garis-garis)
    st.markdown('----')

    # Scatter plot antara 'income' dan 'age'
    fig2, ax2 = plt.subplots()
    ax2.scatter(data['Income'], data['Age'], color='blue', alpha=0.5)
    ax2.set_xlabel('Pendapatan Tahunan')
    ax2.set_ylabel('Usia')
    ax2.set_title('Pendapatan Tahunan vs Usia')
    st.pyplot(fig2)
    st.write("Dari analisis histogram pendapatan tahunan, dapat diamati bahwa sebagian besar nasabah memiliki pendapatan tahunan dalam rentang 0 hingga kurang dari 100. Hal yang serupa juga terlihat pada distribusi umur, di mana rentang umur dari kurang dari 30 hingga lebih dari 60 cukup dominan.")

    # Pemisah (garis-garis)
    st.markdown('----')

    # Scatter plot antara 'CCAvg' dan 'age'
    fig3, ax3 = plt.subplots()
    ax3.scatter(data['CCAvg'], data['Age'], color='green', alpha=0.5)
    ax3.set_xlabel('Rata-rata Pengeluaran Kartu Kredit Bulanan')
    ax3.set_ylabel('Usia')
    ax3.set_title('CCAvg vs Usia')
    st.pyplot(fig3)
    st.write("Pada histogram CCAvg (rata-rata pengeluaran kartu kredit), rentang umur dari kurang dari 30 hingga lebih dari 60 menunjukkan pola yang serupa dengan distribusi pengeluaran kartu kredit dalam rentang 0-3. Dari pola ini, dapat disimpulkan bahwa sebagian besar nasabah memiliki pengeluaran kartu kredit yang tidak signifikan, terlepas dari rentang umur mereka. Dari analisis ini, dapat ditarik kesimpulan bahwa tidak ada korelasi yang kuat antara pendapatan tahunan, CCAvg, dan umur nasabah. Meskipun ada variasi dalam pendapatan dan pengeluaran kartu kredit di berbagai rentang umur, namun pola distribusinya tidak menunjukkan ketergantungan yang signifikan terhadap usia nasabah.")

    # Pemisah (garis-garis)
    st.markdown('----')

    # Scatter plot antara 'Income' dan 'Mortgage'
    fig4, ax4 = plt.subplots()
    ax4.scatter(data['Income'], data['Mortgage'], color='red', alpha=0.5)
    ax4.set_xlabel('Pendapatan Tahunan')
    ax4.set_ylabel('Mortgage')
    ax4.set_title('Scatter Plot Pendapatan Tahunan vs Mortgage')
    st.pyplot(fig4)
    st.write("Terdapat titik yang cenderung terkonsentrasi di bagian bawah, hal ini mungkin menunjukkan bahwa sebagian besar nasabah dengan pendapatan rendah memiliki hipotek yang lebih tinggi, sementara nasabah dengan pendapatan tinggi mungkin memiliki hipotek yang lebih rendah. Tetapi walaupun terdapat titik yang cenderung terkonsentrasi kebawah, titik yang linier (berbanding lurus) pun tetap ada yang artinya pun sebagian dari nasabah memiliki pendapatan yang rendah dengan hipotek yang rendah, begitu juga sebaliknya. Dari plot ini dapat diperoleh informasi mengenai segmentasi pasar seperti bank dapat menargetkan penawaran produk hipotek khusus untuk nasabah dengan pendapatan tinggi yang cenderung memiliki hipotek yang lebih rendah.")

    # Pemisah (garis-garis)
    st.markdown('----')

    # Membuat objek gambar
    fig5, ax5 = plt.subplots(figsize=(12, 5))
    # Membuat grafik bar untuk pendapatan (Income)
    ax5.bar(data['Personal Loan'], data['Income'], color='skyblue', align='center', label='Income')
    ax5.set_ylabel('Income', color='blue')
    plt.xticks(rotation=45)
    plt.xlabel('Personal Loan Status')
    # Membuat sumbu kedua
    ax6 = ax5.twinx()
    # Membuat grafik bar untuk CCAvg
    ax6.bar(data['Personal Loan'], data['CCAvg'], color='salmon', align='edge', label='CCAvg')
    ax6.set_ylabel('CCAvg', color='red')
    # Menambahkan judul dan legenda
    plt.title('Perbandingan Pendapatan dengan CCAvg berdasarkan Pinjaman Pribadi')
    plt.legend()
    # Menyimpan gambar dalam objek fig
    fig_bar_double = plt.gcf()
    # Menampilkan plot menggunakan Streamlit
    st.pyplot(fig_bar_double)
    st.write("Grafik ini untuk membandingkan bagaimana pendapatan dan pengeluaran kartu kredit rata-rata bulanan (CCAvg) bervariasi antara nasabah yang meminjam (1) dan yang tidak (0). Hal ini dapat memberikan wawasan tentang karakteristik finansial nasabah di kedua kelompok tersebut. Dapat dilihat bahwa nasabah yang memiliki income lebih tinggi maka mereka tidak menerima tawaran pinjaman pribadi sedangkan pada nasabah yang rata-rata pengeluaran kartu kredit per bulan nya lebih tinggi maka mereka menerima tawaran pinjaman pribadi. Walaupun persentase yang menerima tawaran pinjaman tersebut kurang lebih 9% berarti dapat dipastikan isi dari 9% tersebut kebanyakan nasabah yang memiliki rata-rata pengeluaran kartu kreditnya tinggi.")


# Jalankan aplikasi
if __name__ == "__main__":
    run()


