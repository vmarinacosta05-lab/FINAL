import streamlit as st

st.set_page_config(page_title="Creador de Fábulas", page_icon="📖", layout="centered")

with st.sidebar:
    st.markdown("## 📚 Navegación")
    st.markdown("---")
    st.page_link("app.py", label="🏠 Inicio")
    st.page_link("pages/2_Fabula.py", label="📖 Creador de Fábulas")

st.markdown("<h1 style='text-align:center'>📖 Creador de Fábulas</h1>", unsafe_allow_html=True)
st.markdown("---")
st.info("🚧 Esta sección estará disponible pronto. ¡Aquí crearás tu fábula a partir de un dibujo!")
