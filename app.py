import streamlit as st
import random
import time

# Listas de compuestos
hidroxidos = ["LiOH", "NaOH", "KOH", "Mg(OH)₂", "Ca(OH)₂", "Al(OH)₃", "Fe(OH)₂", "Fe(OH)₃", "CuOH", "Cu(OH)₂"]
hidruros = ["LiH", "NaH", "CaH₂", "AlH₃", "FeH₂", "FeH₃", "CuH", "CuH₂", "PbH₂", "PbH₄"]
oxidos = ["Li₂O", "Na₂O", "MgO", "CaO", "Al₂O₃", "FeO", "Fe₂O₃", "CO₂", "SO₂", "SO₃", "Cl₂O₇"]
oxacidos = ["HClO", "HClO₂", "HClO₃", "HClO₄", "H₂SO₃", "H₂SO₄", "HNO₂", "HNO₃", "H₃PO₄"]
todos_los_compuestos = hidroxidos + hidruros + oxidos + oxacidos

sistemas = ["Tradicional", "Stock", "Sistemática (IUPAC)"]

# Diseño de la página web
st.title("🎰 Ruleta Química Interactiva")
st.write("Selecciona una categoría y presiona el botón para generar un reto para tus estudiantes.")

# Menú desplegable
opcion = st.selectbox("📂 Elige el tema a evaluar:", 
                      ["Hidróxidos", "Hidruros", "Óxidos", "Oxácidos", "Repaso General"])

# Asignar la lista según la selección
if opcion == "Hidróxidos":
    lista_activa = hidroxidos
elif opcion == "Hidruros":
    lista_activa = hidruros
elif opcion == "Óxidos":
    lista_activa = oxidos
elif opcion == "Oxácidos":
    lista_activa = oxacidos
else:
    lista_activa = todos_los_compuestos

# Botón para girar
if st.button("🎲 ¡Tirar de la palanca!"):
    
    # Espacio vacío para hacer la animación
    animacion = st.empty()
    tiempo_espera = 0.05
    
    # Animación en la web
    for i in range(20):
        c_temp = random.choice(lista_activa)
        s_temp = random.choice(sistemas)
        animacion.info(f"Girando... \n### 🔄 {c_temp} por {s_temp}")
        time.sleep(tiempo_espera)
        tiempo_espera += 0.01
        
    # Resultado final
    ganador_c = random.choice(lista_activa)
    ganador_s = random.choice(sistemas)
    
    # Borramos la animación y mostramos el ganador en grande
    animacion.empty()
    st.success("✨ ¡NUEVO RETO PARA LA CLASE! ✨")
    st.markdown(f"## 🧪 COMPUESTO: **{ganador_c}**")
    st.markdown(f"## 📝 SISTEMA: **{ganador_s}**")
