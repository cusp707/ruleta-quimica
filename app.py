import streamlit as st
import random
import time

# Configuración de la página (título e icono del navegador)
st.set_page_config(page_title="Tómbola Química Interactiva", page_icon="🎰")

# --- LISTAS DE COMPUESTOS (EXTENDIDAS) ---
hidroxidos = ["LiOH", "NaOH", "KOH", "Mg(OH)₂", "Ca(OH)₂", "Al(OH)₃", "Fe(OH)₂", "Fe(OH)₃", "CuOH", "Cu(OH)₂"]
hidruros = ["LiH", "NaH", "CaH₂", "AlH₃", "FeH₂", "FeH₃", "CuH", "CuH₂"]
oxidos = ["Li₂O", "Na₂O", "MgO", "CaO", "Al₂O₃", "FeO", "Fe₂O₃", "CO₂", "SO₂", "SO₃"]
oxacidos = ["HClO", "HClO₂", "HClO₃", "HClO₄", "H₂SO₃", "H₂SO₄", "HNO₂", "HNO₃", "H₃PO₄"]
todos_los_compuestos = hidroxidos + hidruros + oxidos + oxacidos

sistemas = ["Tradicional", "Stock", "Sistemática (IUPAC)"]

# --- DISEÑO Y ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
<style>
    /* Fondo principal */
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Título principal */
    .titulo-tombola {
        font-size: 3rem;
        font-weight: bold;
        color: #1a5c7c;
        text-align: center;
        margin-bottom: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }

    /* Subtítulo */
    .subtitulo {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-top: -10px;
        margin-bottom: 2rem;
    }

    /* Caja de la Tómbola */
    .tombola-caja {
        background-color: white;
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 2rem;
    }

    /* El "Pergamino/Papelito" */
    .pergamino {
        background: radial-gradient(circle, #fff9e6 0%, #f7e6c4 100%);
        border: 2px solid #b38f36;
        border-radius: 15px;
        padding: 25px;
        margin: 20px auto;
        max-width: 600px;
        box-shadow: 0 15px 35px rgba(179,143,54,0.3);
        transform: rotate(-1deg);
        display: none; /* Oculto por defecto */
        position: relative;
    }

    .pergamino::after {
        content: '';
        position: absolute;
        top: -10px; right: 10px;
        width: 30px; height: 30px;
        background: url('https://raw.githubusercontent.com/FortAwesome/Font-Awesome/master/svgs/solid/hand-holding-dollar.svg') no-repeat;
    }

    .pergamino-titulo {
        font-size: 1.8rem;
        color: #b38f36;
        font-weight: bold;
        margin-bottom: 1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .dato-reto {
        font-size: 2.2rem;
        font-weight: bold;
        color: #333;
        margin: 10px 0;
    }

    .sub-dato {
        font-size: 1.2rem;
        color: #777;
    }
</style>
""", unsafe_allow_with_html=True)

# --- CABECERA ---
st.markdown('<p class="titulo-tombola">🎰 Tómbola Química</p>', unsafe_allow_with_html=True)
st.markdown('<p class="subtitulo">Gira la tómbola para obtener un reto para tus estudiantes</p>', unsafe_allow_with_html=True)

# --- PANEL DE CONTROL ---
with st.expander("📂 Configurar el Repaso", expanded=True):
    opcion = st.selectbox("Elige el tema a evaluar:", ["Hidróxidos", "Hidruros", "Óxidos", "Oxácidos", "Repaso General"])

    # Asignar la lista activa
    if opcion == "Hidróxidos": lista_activa = hidroxidos
    elif opcion == "Hidruros": lista_activa = hidruros
    elif opcion == "Óxidos": lista_activa = oxidos
    elif opcion == "Oxácidos": lista_activa = oxacidos
    else: lista_activa = todos_los_compuestos

    st.write(f"**Tema actual:** {opcion.upper()}")

# --- ÁREA DE LA TÓMBOLA ---
st.markdown('<div class="tombola-caja">', unsafe_allow_with_html=True)

# Usamos st.empty para la animación
# Contenedor para el contador visual (Tómbola)
area_tombola = st.empty()

# Contenedor para el resultado final (Pergamino)
area_pergamino = st.empty()

# Botón para girar
gira_tombola = st.button("🎲 ¡GIRAR TÓMBOLA!")

if gira_tombola:
    
    # 1. Animación de "Giro"
    # Usamos JavaScript para un contador rápido sin refrescar la página
    js_contador = f"""
    <script>
    var list = {lista_activa};
    var sist = {sistemas};
    var area = document.getElementById('area_tombola');
    var count = 0;
    var max_count = 35;
    var interval = 30; // Velocidad del contador (más bajo = más rápido)
    
    // Crear el elemento si no existe
    if (!area) {{
        area = document.createElement('div');
        area.id = 'area_tombola';
        document.body.appendChild(area);
    }}

    var intervalId = setInterval(function() {{
        var c_temp = list[Math.floor(Math.random() * list.length)];
        var s_temp = sist[Math.floor(Math.random() * sist.length)];
        area.innerHTML = '<div style="font-size: 3rem; font-weight:bold; color:#f0f2f6;">🔄 ' + c_temp + ' + ' + s_temp + '</div>';
        count++;
        if (count >= max_count) {{
            clearInterval(intervalId);
            area.innerHTML = ''; // Limpiar la animación
        }}
    }}, interval);
    </script>
    """
    
    # Insertar el JavaScript para que corra
    st.components.v1.html(js_contador, height=100)
    
    # Pausa en Python para esperar a que termine la animación JS
    time.sleep(1.5)
    
    # 2. Selección del Ganador
    ganador_c = random.choice(lista_activa)
    ganador_s = random.choice(sistemas)
    
    # 3. Mostrar el Pergamino Final (HTML/CSS)
    pergamino_html = f"""
    <div class="pergamino" style="display: block;">
        <div class="pergamino-titulo">✨ ¡DING DING DING! ✨</div>
        <p class="sub-dato">NUEVO RETO PARA LA CLASE</p>
        <p class="sub-dato">CATEGORÍA: {opcion.upper()}</p>
        <div class="dato-reto">{ganador_c}</div>
        <p class="sub-dato">por nomenclatura</p>
        <div class="dato-reto">{ganador_s}</div>
    </div>
    """
    
    # Ocultar la animación y mostrar el pergamino
    area_tombola.empty()
    area_pergamino.markdown(pergamino_html, unsafe_allow_with_html=True)
    
    # Efecto sonoro visual (esto no reproduce sonido real, es solo para el efecto visual)
    st.balloons()
