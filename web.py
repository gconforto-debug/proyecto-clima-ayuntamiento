import streamlit as st
import pandas as pd
from datetime import datetime
import os
from PIL import Image
import csv

# --- IMPORTACIÓN MÓDULOS PROPIOS ---
import datos_csv
import validacion
import alertas
import auth

# --- 1. CONFIGURACIÓN DE PÁGINA Y ESTILOS ---
# Configura el título que se ve en el navegador y el ancho de la web
st.set_page_config(page_title="SkyCast Municipal", page_icon="🌤️", layout="wide")

# --- 2. PERSONALIZACIÓN DE DISEÑO (CSS) ---
def aplicar_estilos():
    st.markdown("""
        <style>
            /* Ancho de la barra lateral*/    
            [data-testid="stSidebar"]{
                width: 350px !important;
            }
                
            /* Color del fondo de toda la app*/
            .stApp { background-color: #0d1117; color: #e6edf3; }
            
            /*Color de los títulos (Azul Skycast)*/
            h1, h2, h3 { color: #58a6ff !important; }
                
            /*Estilo de las tarjetas de métricas*/
            .stMetric { background-color: #161b22; border: 1px solid #30363d; border-radius: 6px; padding: 15px; }
            
            /*Estilo de los botones principales*/    
            .stButton>button { background-color: #1f6feb; color: white; width: 100%; border-radius: 6px; }
            
            /*Campos de entrada de texto*/    
            .stTextInput>div>div>input { background-color: #0d1117; color: white; }
            
            /*Contenedor de pestañas (Login/Registro)*/    
            .stTabs [data-baseweb="tab-list"] { gap: 24px; }
            
            /*Texto pestañas activas*/    
            .stTabs [data-baseweb="tab"] { color: #8b949e; }
            
            /*Línea de resaltado de pestaña activa*/    
            .stTabs [data-baseweb="tab-highlight"] { background-color: #58a6ff; }
        </style>
    """, unsafe_allow_html=True)

def mostrar_cabecera():
    # Usamos un ratio que le de buen espacio al logo
    col_logo, col_titulo = st.columns([1, 2.5]) 
    
    with col_logo:
        if os.path.exists("docs/skycast_logo_transparent.png"):
            # Mantenemos el tamaño que te gustó
            st.image("docs/skycast_logo_transparent.png", width=280)
            
    with col_titulo:
        # TRUCO DE PRECISIÓN: Ajusta el 'padding-top' para subir o bajar el texto
        # 60px suele ser el punto medio para un logo de este tamaño
        st.markdown(f"""
            <div style="padding-top: 60px;">
                <h1 style="color: #58a6ff; font-size: 48px; margin: 0;">
                    MUNICIPAL SKYCAST
                </h1>
            </div>
            """, unsafe_allow_html=True)

# --- 3. FUNCIÓN PRINCIPAL ---
def main():
    aplicar_estilos() #Ejecuta los colores personalizados

    # --- SISTEMA DE SESIÓN ---
    # Inicializar estado de autenticación (sirve para saber si alguien ya se logeo)
    if 'autenticado' not in st.session_state:
        st.session_state.autenticado = False

    # --- PANTALLA DE ACCESO (LOGIN / REGISTRO) ---
    if not st.session_state.autenticado:
        mostrar_cabecera()
        st.divider()

        #Se centra el formulario usando columnas (Espacio | Formulario | Espacio)
        col_espacio, col_form, col_espacio2 = st.columns([1, 2, 1])

        with col_form:
            tab_login, tab_reg = st.tabs(["🔐 Iniciar Sesión", "👤 Crear Cuenta"])

            # --- SUB-FLUJO: INICIO DE SESIÓN ---
            with tab_login:
                u = st.text_input("Usuario", key="l_user")
                p = st.text_input("Contraseña", type="password", key="l_pw")
                if st.button("Entrar al Sistema"):
                    db = auth._cargar_usuarios()
                    #Compara el hash de la contraseña ingresada con el guardado
                    if db.get(u.lower()) == auth._hash_password(p):
                        st.session_state.autenticado = True
                        st.session_state.usuario = u
                        st.rerun() #Recarga la página para mostrar el dashboard
                    else:
                        st.error("Credenciales incorrectas")

            # --- SUB-FLUJO: REGISTRO DE NUEVOS USUARIOS ---
            with tab_reg:
                new_u = st.text_input("Nuevo Usuario", key="r_user")
                new_p = st.text_input("Nueva Contraseña", type="password", key="r_pw")
                conf_p = st.text_input("Confirmar Contraseña", type="password", key="r_pw_c")
                if st.button("Registrar Usuario"):
                    db = auth._cargar_usuarios()

                    #Validación básica de seguridad
                    if not new_u or len(new_p) < 4:
                        st.warning("Datos insuficientes.")
                    elif new_u.lower() in db:
                        st.error("El usuario ya existe.")
                    elif new_p != conf_p:
                        st.error("Las contraseñas no coinciden.")
                    else:
                        #Guarda el usuario con la contraseña cifrada
                        with open("usuarios.csv", "a", newline="", encoding="utf-8") as f:
                            escritor = csv.DictWriter(f, fieldnames=["usuario", "password_hash"])
                            escritor.writerow({"usuario": new_u.lower(), "password_hash": auth._hash_password(new_p)})
                        st.success("✅ Cuenta creada. Ya puedes iniciar sesión.")
        return #Detiene la ejecución para que no se vea la app sin login
    
    # --- PANTALLA PRINCIPAL (TRAS LOGUEARSE) ---
    #Solo se ejecuta si st.session_state.autenticado es True
    st.sidebar.image("docs/skycast_logo_transparent.png", use_container_width=True)
    st.sidebar.title(f"Hola, {st.session_state.usuario}")

    # Menú de navegación lateral
    opcion = st.sidebar.radio("Menú", ["📈 Dashboard", "📝 Registrar Datos", "🔍 Historial"])

    #Botón para salir (borra el estado de la sesión)
    if st.sidebar.button("Cerrar Sesión"):
        st.session_state.autenticado = False
        st.rerun()

    #Se inicializa el gestor de datos (Clase de datos.csv)
    gestor = datos_csv.GestorDatosClima()

    # --- PANTALLA: DASHBOARD ---
    if opcion == "📈 Dashboard":
        st.header("📊 Análisis Estadístico")
        zona = st.selectbox("Seleccione Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
        
        #Se obtienen cálculos de Pandas desde la lógica original
        stats = gestor.obtener_estadisticas_zona(zona)

        if stats:
            #Se muestran las métricas en paralelo
            c1, c2, c3 = st.columns(3)
            c1.metric("Temperatura Media", f"{stats['media_temp']:.1f} °C")
            c2.metric("Viento Máximo", f"{stats['max_viento']} km/h")
            c3.metric("Registros", stats['conteo'])

            #Se dibuja el gráfico de líneas automático usando Pandas
            df = pd.read_csv("clima_dataset.csv")
            df_zona = df[df['zona'] == zona]
            st.line_chart(df_zona.set_index('fecha')['temperatura'], color="#58a6ff")
        else:
            st.info("No hay datos para esta zona.")

    # --- PANTALLA: REGISTRO DE DATOS ---
    elif opcion == "📝 Registrar Datos":
        st.header("📝 Nuevo Registro")
        with st.form("form_reg"):
            col_a, col_b = st.columns(2)
            f = col_a.date_input("Fecha", datetime.now())
            z = col_b.selectbox("Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
            temp = st.number_input("Temperatura (°C)", value=20.0)
            hum = st.slider("Humedad (%)", 0, 100, 50)
            vie = st.number_input("Viento (km/h)", value=0.0)

            if st.form_submit_button("Guardar"):
                datos = {"fecha": str(f), "zona": z, "temperatura": temp, "humedad": hum, "viento": vie}
                
                #Se usa la lógica de validación
                errores = validacion.validar_registro(datos)
                if errores:
                    for err in errores: st.error(err)
                else:
                    # Se usa la lógica de alertas
                    avisos = alertas.evaluar_alertas(datos)
                    for aviso in avisos: st.warning(aviso)
                    
                    #Guardado final en el csv
                    if gestor.guardar_en_csv(datos):
                        st.success("Datos guardados.")

    # --- PANTALLA: HISTORIAL ---
    elif opcion == "🔍 Historial":
        st.header("🔍 Consulta Histórica")
        if os.path.exists("clima_dataset.csv"):
            df_full = pd.read_csv("clima_dataset.csv")
            #Muestra el csv como una tabla interactiva de excel
            st.dataframe(df_full, use_container_width=True)

#Puntero de inicio de Python
if __name__ == "__main__":
    main()
    