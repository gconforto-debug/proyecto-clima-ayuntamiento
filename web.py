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
            /* 1. Ocultar todos los iconos de la barra superior excepto los 3 puntos */
            /* Buscamos el contenedor de acciones y lo eliminamos */
            div[data-testid="stToolbarActions"] {
                display: none !important;
            }
            
            /* 2. Ajuste de la Sidebar */
            [data-testid="stSidebar"] { width: 300px !important; }
            
            /* 3. Títulos en Azul SkyCast */
            h1, h2, h3 { color: #58a6ff !important; }

            /* 4. Tarjetas de métricas */
            div[data-testid="stMetric"] {
                border: 1px solid rgba(128, 128, 128, 0.3);
                border-radius: 12px;
                padding: 15px;
            }
            
            /* 5. Ocultar el pie de página y la decoración superior innecesaria */
            footer { visibility: hidden !important; }
            header { background-color: rgba(0,0,0,0) !important; }
        </style>
    """, unsafe_allow_html=True)

aplicar_estilos()

# Inicializar el gestor de datos
gestor = datos_csv.GestorDatosClima()

# --- 3. LÓGICA DE AUTENTICACIÓN ---
if 'conectado' not in st.session_state:
    st.session_state.conectado = False

if not st.session_state.conectado:
    st.write("##") # Espacio superior
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.title("☀️ SkyCast Login")
        with st.form("login_form"):
            u = st.text_input("Usuario").lower().strip()
            p = st.text_input("Contraseña", type="password")
            if st.form_submit_button("Acceder al Sistema"):
                usuarios_db = auth._cargar_usuarios()
                if usuarios_db.get(u) == auth._hash_password(p):
                    st.session_state.conectado = True
                    st.session_state.user = u
                    st.rerun()
                else:
                    st.error("❌ Usuario o contraseña incorrectos")
    st.stop()

# --- 4. INTERFAZ PRINCIPAL ---
# Cargamos el logo solo si el archivo existe en la carpeta
with st.sidebar:
    if os.path.exists('logo.png'):
        # Añadimos un pequeño margen superior para que no pegue al borde
        st.markdown("##") 
        st.image('logo.png', use_container_width=True)
    else:
        st.title("🌤️ SKYCAST")
    
    st.markdown(f"**Usuario:** {st.session_state.user.capitalize()}")
    st.write("---") # Separador visual elegante

opcion = st.sidebar.radio("Navegación", ["📊 Dashboard", "📝 Registrar Datos", "🔍 Historial", "🚪 Cerrar Sesión"])
if opcion == "🚪 Cerrar Sesión":
    st.session_state.conectado = False
    st.rerun()

elif opcion == "📊 Dashboard":
    st.title("🏛️ Panel de Control Climático")
    zona = st.selectbox("Seleccione Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
    
    stats = gestor.obtener_estadisticas_zona(zona)
    
    if stats:
        # 1. Métricas principales en una fila
        c1, c2, c3 = st.columns(3)
        c1.metric("Temperatura Media", f"{stats['media_temp']:.1f} °C")
        c2.metric("Humedad Media", f"{stats['media_hum']:.1f} %")
        c3.metric("Viento Máximo", f"{stats['max_viento']} km/h")
        
        st.write("---") # Línea separadora sutil
        
        # 2. Gráfico de tendencia más pequeño
        # Usamos columnas para "encoger" el gráfico hacia el centro o un lado
        col_grafico, col_info = st.columns([2, 1]) # El gráfico ocupa 2/3 y dejamos 1/3 libre
        
        with col_grafico:
            st.subheader("📈 Tendencia")
            df_zona = pd.DataFrame(gestor.consultar_por_zona(zona))
            if not df_zona.empty:
                # Ordenamos por fecha para que la línea tenga sentido
                df_zona = df_zona.sort_values('fecha')
                # Dibujamos el gráfico con una altura controlada (use_container_width por defecto)
                st.line_chart(df_zona.set_index('fecha')['temperatura'], height=250)
        
        with col_info:
            # Aprovechamos el espacio lateral para un resumen rápido o datos extra
            st.subheader("📋 Resumen")
            st.write(f"Mostrando los últimos **{len(df_zona)}** registros de la zona **{zona}**.")
            if stats['max_viento'] > 50:
                st.warning("⚠️ Ráfagas de viento elevadas detectadas en el periodo.")
                
    else:
        st.info(f"No hay datos registrados para la zona {zona}.")

elif opcion == "📝 Registrar Datos":
    st.title("📝 Nueva Entrada")
    with st.form("registro_datos"):
        f = st.date_input("Fecha", datetime.now())
        z = st.selectbox("Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
        temp = st.number_input("Temperatura (°C)", value=20.0)
        hum = st.slider("Humedad (%)", 0, 100, 50)
        vie = st.number_input("Viento (km/h)", value=0.0)

        if st.form_submit_button("Guardar Datos"):
            datos = {"fecha": str(f), "zona": z, "temperatura": temp, "humedad": hum, "viento": vie}
            errores = validacion.validar_registro(datos)
            if errores:
                for err in errores: st.error(err)
            else:
                avisos = alertas.evaluar_alertas(datos)
                for aviso in avisos: st.warning(aviso)
                if gestor.guardar_en_csv(datos):
                    st.success("✅ Datos guardados correctamente.")

elif opcion == "🔍 Historial":
    st.header("🔍 Registro Histórico")
    if os.path.exists("clima_dataset.csv"):
        df = pd.read_csv("clima_dataset.csv")
        st.dataframe(df, use_container_width=True)