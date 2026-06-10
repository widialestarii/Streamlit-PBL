import streamlit as st
import joblib
import pandas as pd

# =====================================
# Konfigurasi Halaman
# =====================================
st.set_page_config(
    page_title="Prediksi Tsunami",
    page_icon="🌊",
    layout="centered"
)

# =====================================
# Load Model
# =====================================
@st.cache_resource
def load_artifacts():
    model = joblib.load("random_forest_model.pkl")
    scaler = joblib.load("scaler.pkl")
    fitur = joblib.load("fitur.pkl")
    return model, scaler, fitur

model, scaler, FITUR = load_artifacts()

# =====================================
# Header
# =====================================
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

input_user = {}

for fitur in FITUR:
    input_user[fitur] = st.sidebar.number_input(
        label=fitur,
        value=0.0,
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