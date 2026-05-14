import streamlit as st
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

st.set_page_config(page_title="Creador de Fábulas", page_icon="📖", layout="centered")

# --- Sidebar con página bloqueada ---
with st.sidebar:
    st.markdown("## 📚 Navegación")
    st.markdown("---")
    st.page_link("app.py", label="🎙️ Inicio", icon="🏠")
    st.markdown("🔒 **Creador de Fábulas** *(bloqueado)*")
    st.caption("Di la contraseña secreta para desbloquear")

# --- Contenido principal ---
st.markdown("<h1 style='text-align:center'>📖 Bienvenido al Creador de Fábulas</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px'>Oprime el botón y di la contraseña secreta para entrar</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Botón de voz ---
st.write("🎙️ Toca el botón y habla la contraseña:")

stt_button = Button(label="🎤 Hablar", width=200)
stt_button.js_on_event("button_click", CustomJS(code="""
    var recognition = new webkitSpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'es-ES';
    recognition.onresult = function (e) {
        var value = "";
        for (var i = e.resultIndex; i < e.results.length; ++i) {
            if (e.results[i].isFinal) {
                value += e.results[i][0].transcript;
            }
        }
        if (value != "") {
            document.dispatchEvent(new CustomEvent("GET_TEXT", {detail: value}));
        }
    }
    recognition.start();
"""))

result = streamlit_bokeh_events(
    stt_button,
    events="GET_TEXT",
    key="listen",
    refresh_on_update=False,
    override_height=75,
    debounce_time=0
)

# --- Lógica de contraseña ---
CONTRASENA = "hola"

if result:
    if "GET_TEXT" in result:
        texto = result.get("GET_TEXT").strip().lower()
        st.write(f"🗣️ Escuché: **{texto}**")

        if texto == CONTRASENA:
            st.success("✅ ¡Contraseña correcta! Abriendo el Creador de Fábulas...")
            st.switch_page("pages/2_Fabula.py")
        else:
            st.error("❌ Contraseña incorrecta. No puedes entrar.")
