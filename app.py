import streamlit as st
import random
import time

# Configuración de la página
st.set_page_config(page_title="Tómbola Química", page_icon="🎰")

# --- LISTAS DE COMPUESTOS ---
hidroxidos = ["LiOH", "NaOH", "KOH", "Mg(OH)₂", "Ca(OH)₂", "Al(OH)₃", "Fe(OH)₂", "Fe(OH)₃", "CuOH", "Cu(OH)₂"]
hidruros = ["LiH", "NaH", "CaH₂", "AlH₃", "FeH₂", "FeH₃", "CuH", "CuH₂"]
oxidos = ["Li₂O", "Na₂O", "MgO", "CaO", "Al₂O₃", "FeO", "Fe₂O₃", "CO₂", "SO₂", "SO₃"]
oxacidos = ["HClO", "HClO₂", "HClO₃", "HClO₄", "H₂SO₃", "H₂SO₄", "HNO₂", "HNO₃", "H₃PO₄"]
todos_los_compuestos = hidroxidos + hidruros + oxidos + oxacidos

sistemas = ["Tradicional", "Stock", "Sistemática (IUPAC)"]

# --- CABECERA ---
# ¡Aquí estaba el error del "with" corregido!
st.markdown('<h1 style="text-align: center; color: #1a5c7c; font-size: 3.5rem;">🎰 Tómbola Química</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; color: #555; font-size: 1.2rem;">Gira la tómbola para obtener un reto para tus estudiantes</p>', unsafe_allow_html=True)

# --- PANEL DE CONTROL ---
with st.expander("📂 Configurar el Repaso", expanded=True):
    opcion = st.selectbox("Elige el tema a evaluar:", ["Hidróxidos", "Hidruros", "Óxidos", "Oxácidos", "Repaso General"])

    if opcion == "Hidróxidos": lista_activa = hidroxidos
    elif opcion == "Hidruros": lista_activa = hidruros
    elif opcion == "Óxidos": lista_activa = oxidos
    elif opcion == "Oxácidos": lista_activa = oxacidos
    else: lista_activa = todos_los_compuestos

# --- ESPACIOS PARA LA TÓMBOLA Y EL RESULTADO ---
area_tombola = st.empty()
area_pergamino = st.empty()

# Centrar el botón de girar
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    gira_tombola = st.button("🎲 ¡GIRAR TÓMBOLA!", use_container_width=True)

# --- LÓGICA DE ANIMACIÓN ---
if gira_tombola:
    tiempo_espera = 0.05
    
    # 1. Efecto visual de girar
    for i in range(20):
        c_temp = random.choice(lista_activa)
        s_temp = random.choice(sistemas)
        
        # Mostramos los compuestos pasando rápidamente
        area_tombola.markdown(f"""
        <div style='text-align: center; background-color: white; border-radius: 20px; padding: 30px; box-shadow: 0 10px 25px rgba(0,0,0,0.1); margin-top: 20px;'>
            <h2 style='font-size: 3rem; color: #1a5c7c;'>🔄 {c_temp}</h2>
            <h3 style='color: #888;'>por {s_temp}</h3>
        </div>
        """, unsafe_allow_html=True)
        
        time.sleep(tiempo_espera)
        tiempo_espera += 0.01  # Hace que frene poco a poco
        
    # 2. Selección del Ganador Real
    ganador_c = random.choice(lista_activa)
    ganador_s = random.choice(sistemas)
    
    # 3. Diseño del Pergamino Final
    pergamino_html = f"""
    <div style="background: radial-gradient(circle, #fff9e6 0%, #f7e6c4 100%); border: 2px solid #b38f36; border-radius: 15px; padding: 30px; margin: 20px auto; text-align: center; box-shadow: 0 15px 35px rgba(179,143,54,0.3);">
        <div style="font-size: 2rem; color: #b38f36; font-weight: bold; margin-bottom: 15px; letter-spacing: 2px;">✨ ¡TENEMOS UN RETO! ✨</div>
        <p style="font-size: 1.2rem; color: #777; margin: 0;">CATEGORÍA: <b>{opcion.upper()}</b></p>
        <div style="font-size: 4.5rem; font-weight: bold; color: #222; margin: 15px 0;">{ganador_c}</div>
        <p style="font-size: 1.2rem; color: #777; margin: 0;">Sistema requerido:</p>
        <div style="font-size: 2.5rem; font-weight: bold; color: #1a5c7c; margin-top: 10px;">{ganador_s}</div>
    </div>
    """
    
    # 4. Mostrar resultado y globos
    area_tombola.empty() # Limpia la animación
    area_pergamino.markdown(pergamino_html, unsafe_allow_html=True)
    st.balloons()
