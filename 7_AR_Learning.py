import streamlit as st

# ✅ Set Page Configuration
st.set_page_config(
    page_title="🌱 AR-Based Learning",
    page_icon="📲",
    layout="wide"
)

# ✅ Path to QR Code Image
qr_code_path = "Graphics/QR Tomato.jpeg"

# ✅ Display Title
st.markdown("<h1 style='text-align: center;'>🌱 AR-Based Learning Experience</h1>", unsafe_allow_html=True)

# ✅ Centered QR Code with Reduced Size
col1, col2, col3 = st.columns([1, 2, 1])  # Centering layout
with col2:
    st.image(qr_code_path, width=350)  # Adjust width as needed

# ✅ Centered Instruction
st.markdown("<h3 style='text-align: center;'>📲 Scan the QR Code to Experience AR Learning!</h3>", unsafe_allow_html=True)
