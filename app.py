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