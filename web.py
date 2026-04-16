import streamlit as st
import pandas as pd
from datetime import datetime
import os
import csv

# --- IMPORTACIÓN MÓDULOS PROPIOS ---
import datos_csv
import validacion
import alertas
import auth

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="SkyCast Municipal", page_icon="🌤️", layout="wide")

# --- 2. PERSONALIZACIÓN DE DISEÑO (CSS DINÁMICO) ---
def aplicar_estilos():
    st.markdown("""
        <style>
            /* 1. Quitamos el color de fondo fijo (.stApp) para que sea dinámico */
            
            /* 2. Ajustamos el ancho de la sidebar */    
            [data-testid="stSidebar"] { width: 300px !important; }
            
            /* 3. Color azul para los títulos (esto queda bien en ambos modos) */
            h1, h2, h3 { color: #58a6ff !important; }
                
            /* 4. Estilo de las tarjetas de métricas mejorado */
            div[data-testid="stMetric"] {
                background-color: rgba(128, 128, 128, 0.1); /* Fondo sutil traslúcido */
                border: 1px solid #30363d;
                border-radius: 10px;
                padding: 15px;
            }

            /* 5. Ocultar menús innecesarios */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
aplicar_estilos()

# Inicializar el gestor de datos
gestor = datos_csv.GestorDatosClima()

# --- 3. LÓGICA DE AUTENTICACIÓN ---
if 'conectado' not in st.session_state:
    st.session_state.conectado = False

if not st.session_state.conectado:
    # Centrar el formulario de login
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("☀️ SkyCast Login")
        with st.form("login_form"):
            u = st.text_input("Usuario").lower().strip()
            p = st.text_input("Contraseña", type="password")
            if st.form_submit_button("Acceder"):
                usuarios_db = auth._cargar_usuarios()
                if usuarios_db.get(u) == auth._hash_password(p):
                    st.session_state.conectado = True
                    st.session_state.user = u
                    st.rerun()
                else:
                    st.error("❌ Usuario o contraseña incorrectos")
    st.stop()

# --- 4. INTERFAZ PRINCIPAL (Solo si está conectado) ---
st.sidebar.title(f"👤 {st.session_state.user.capitalize()}")
opcion = st.sidebar.radio("Menú de Gestión", ["📊 Dashboard", "📝 Registrar Datos", "🔍 Historial", "🚪 Cerrar Sesión"])

if opcion == "🚪 Cerrar Sesión":
    st.session_state.conectado = False
    st.rerun()

elif opcion == "📊 Dashboard":
    st.title("🏛️ Dashboard Meteorológico Municipal")
    zona = st.selectbox("Seleccione Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
    
    stats = gestor.obtener_estadisticas_zona(zona)
    
    if stats:
        # Fila de métricas grandes (Como en tu captura original)
        c1, c2, c3 = st.columns(3)
        c1.metric("Temperatura Media", f"{stats['media_temp']:.1f} °C")
        c2.metric("Humedad Media", f"{stats['media_hum']:.1f} %")
        c3.metric("Viento Máximo", f"{stats['max_viento']} km/h")
        
        # Gráfico rápido de tendencia
        st.subheader("📈 Tendencia de Temperatura")
        df_zona = pd.DataFrame(gestor.consultar_por_zona(zona))
        if not df_zona.empty:
            df_zona['temperatura'] = df_zona['temperatura'].astype(float)
            st.line_chart(df_zona.set_index('fecha')['temperatura'])
    else:
        st.info(f"No hay datos registrados para la zona {zona}.")

elif opcion == "📝 Registrar Datos":
    st.title("📝 Nuevo Registro")
    with st.form("registro_datos"):
        c1, c2 = st.columns(2)
        f = c1.date_input("Fecha", datetime.now())
        z = c2.selectbox("Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
        
        temp = st.number_input("Temperatura (°C)", value=20.0, step=0.1)
        hum = st.slider("Humedad (%)", 0, 100, 50)
        vie = st.number_input("Viento (km/h)", value=0.0, step=0.5)

        if st.form_submit_button("Guardar en Sistema"):
            datos = {"fecha": str(f), "zona": z, "temperatura": temp, "humedad": hum, "viento": vie}
            
            errores = validacion.validar_registro(datos)
            if errores:
                for err in errores: st.error(err)
            else:
                # Alertas visuales
                avisos = alertas.evaluar_alertas(datos)
                for aviso in avisos: st.warning(aviso)
                
                if gestor.guardar_en_csv(datos):
                    st.success("✅ Registro guardado correctamente.")

elif opcion == "🔍 Historial":
    st.header("🔍 Historial Completo")
    if os.path.exists("clima_dataset.csv"):
        df = pd.read_csv("clima_dataset.csv")
        st.dataframe(df.sort_values(by="fecha", ascending=False), use_container_width=True)
    else:
        st.error("Archivo de datos no encontrado.")