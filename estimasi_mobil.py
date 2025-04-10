import pickle
import streamlit as st
import numpy as np

# Load model
model = pickle.load(open('estimasi_mobil.sav', 'rb'))

# Set page config
st.set_page_config(page_title="Estimasi Harga Mobil Bekas", page_icon="🚗")

# Header
st.title('🚗 Estimasi Harga Mobil Bekas')
st.markdown("""
Selamat datang di aplikasi **prediksi harga mobil bekas**!  
Masukkan detail mobil kamu di bawah ini, dan sistem akan memperkirakan harga jualnya 📉📈.
""")

st.markdown("---")

# Layout form input
col1, col2 = st.columns(2)

with col1:
    year = st.number_input('📅 Tahun Mobil', min_value=1990, max_value=2025, value=2015)
    mileage = st.number_input('🛣️ Kilometer Mobil (Km)', min_value=0, value=50000)
    tax = st.number_input('💰 Pajak Mobil (£)', min_value=0, value=150)

with col2:
    mpg = st.number_input('⛽ Konsumsi BBM (mpg)', min_value=0.0, value=50.0)
    engineSize = st.number_input('⚙️ Ukuran Mesin (L)', min_value=0.0, value=1.6)

st.markdown("---")

# Prediksi
predict = None
if st.button('🔍 Estimasi Harga Mobil'):
    input_data = np.array([[year, mileage, tax, mpg, engineSize]])
    predict = model.predict(input_data)[0]
    predict_idr = predict * 19000

    st.success('✅ Estimasi Harga Mobil Berhasil!')
    st.markdown(f"""
    ### 💷 Estimasi Harga Mobil Bekas:
    **£ {predict:,.2f}**  
    **Rp {predict_idr/1e6:,.2f} Juta**
    """)
