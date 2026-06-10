import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Prediksi Tsunami",
    page_icon="🌊",
    layout="centered"
)

@st.cache_resource
def load_artifacts():
    model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.pkl")
    fitur = joblib.load("fitur.pkl")
    return model, scaler, fitur

model, scaler, FITUR = load_artifacts()

st.title("🌊 Prediksi Potensi Tsunami")
st.write(
    "Masukkan parameter gempa bumi untuk memprediksi apakah "
    "berpotensi menimbulkan tsunami atau tidak."
)

st.divider()

# =====================================
# Sidebar Input
# =====================================
st.sidebar.header("Input Data Gempa")

magnitude = st.sidebar.number_input(
    "Magnitude",
    min_value=0.0,
    max_value=10.0,
    value=6.0,
    step=0.1
)

depth = st.sidebar.number_input(
    "Depth (km)",
    min_value=0.0,
    value=10.0,
    step=0.1
)

felt = st.sidebar.number_input(
    "Jumlah Laporan Felt",
    min_value=0,
    value=100
)

# Mapping negara
country_mapping = {
    "Afghanistan": 0,
    "Alaska": 1,
    "Argentina": 2,
    "Arkansas": 3,
    "Azerbaijan": 4,
    "Bangladesh": 5,
    "Bolivia": 6,
    "Bosnia and Herzegovina": 7,
    "Brazil": 8,
    "California": 9,
    "Canada": 10,
    "Chile": 11,
    "China": 12,
    "Costa Rica": 13,
    "Democratic Republic": 14,
    "Djibouti": 15,
    "Ecuador": 16,
    "El Salvador": 17,
    "Florida": 18,
    "Greece": 19,
    "Guatemala": 20,
    "Illinois": 21,
    "India": 22,
    "Indonesia": 23,
    "Iran": 24,
    "Japan": 25,
    "Kansas": 26,
    "Kermadec Islands": 27,
    "Kyrgyzstan": 28,
    "Louisiana": 29,
    "Mariana Islands region": 30,
    "Mexico": 31,
    "Montana": 32,
    "Myanmar": 33,
    "Nebraska": 34,
    "Nepal": 35,
    "Nevada": 36,
    "New Jersey": 37,
    "New Mexico": 38,
    "New Zealand": 39,
    "Nicaragua": 40,
    "Ohio": 41,
    "Oklahoma": 42,
    "Pakistan": 43,
    "Peru": 44,
    "Philippines": 45,
    "Portugal": 46,
    "Russia": 47,
    "Somalia": 48,
    "Taiwan": 49,
    "Tanzania": 50,
    "Tennessee": 51,
    "Texas": 52,
    "Timor Leste": 53,
    "Turkey": 54,
    "Utah": 55,
    "Vietnam": 56,
    "Washington": 57,
    "central Mid-Atlantic Ridge": 58
}

negara = st.sidebar.selectbox(
    "Negara/Wilayah Gempa",
    options=list(country_mapping.keys()),
    index=23  # Indonesia
)

country_encoded = country_mapping[negara]

risk_score = st.sidebar.number_input(
    "Risk Score",
    min_value=0.0,
    value=50.0,
    step=0.1
)

# =====================================
# Prediksi
# =====================================
if st.sidebar.button(
    "Prediksi Tsunami",
    type="primary",
    use_container_width=True
):

    try:
        data_input = pd.DataFrame(
            [[input_user[f] for f in FITUR]],
            columns=FITUR
        )

        data_scaled = scaler.transform(data_input)

        prediksi = model.predict(data_scaled)[0]
        probabilitas = model.predict_proba(data_scaled)[0]

        st.subheader("Hasil Prediksi")

        if prediksi == 1:
            st.error(
                f"⚠️ Berpotensi TSUNAMI\n\n"
                f"Tingkat Keyakinan: {probabilitas[1]*100:.2f}%"
            )
        else:
            st.success(
                f"✅ Tidak Berpotensi Tsunami\n\n"
                f"Tingkat Keyakinan: {probabilitas[0]*100:.2f}%"
            )

        # Menampilkan input
        st.subheader("Data Input")
        st.dataframe(data_input, use_container_width=True)

        # Feature Importance
        st.subheader("Feature Importance")

        importance_df = pd.DataFrame({
            "Fitur": FITUR,
            "Importance": model.feature_importances_
        }).sort_values(
            by="Importance",
            ascending=False
        )

        st.dataframe(
            importance_df,
            use_container_width=True,
            hide_index=True
        )

    except Exception as e:
        st.error(f"Terjadi error: {e}")

else:
    st.info(
        "Isi nilai parameter gempa pada sidebar lalu klik tombol Prediksi Tsunami."
    )

# =====================================
# Footer
# =====================================
st.divider()
st.caption(
    "Aplikasi Prediksi Tsunami Menggunakan Random Forest Classifier"
)