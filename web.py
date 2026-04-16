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

# --- 2. PERSONALIZACIÓN DE DISEÑO (ESTILO DINÁMICO) ---
def aplicar_estilos():
    st.markdown("""
        <style>
            /* Barra superior: Solo dejamos los 3 puntos */
            div[data-testid="stToolbarActions"] { display: none !important; }
            
            /* Ajuste de Sidebar */
            [data-testid="stSidebar"] { width: 320px !important; }
            
            /* Títulos en Azul SkyCast */
            h1, h2, h3 { color: #58a6ff !important; font-family: 'Segoe UI', sans-serif; }

            /* Tarjetas de métricas (Diseño de la foto) */
            div[data-testid="stMetric"] {
                border: 1px solid rgba(128, 128, 128, 0.3);
                border-radius: 12px;
                padding: 20px;
                background-color: rgba(151, 166, 185, 0.05);
            }
            
            /* Ocultar footer */
            footer { visibility: hidden !important; }
        </style>
    """, unsafe_allow_html=True)

def mostrar_cabecera_login():
    ruta_logo = "docs/skycast_logo_transparent.png"
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(ruta_logo):
            # Centramos el logo con sub-columnas
            c_izq, c_mid, c_der = st.columns([1, 2, 1])
            with c_mid:
                st.image(ruta_logo, use_container_width=True)
        st.markdown("<h1 style='text-align: center; color: #58a6ff;'>SkyCast Login</h1>", unsafe_allow_html=True)

# --- 3. FUNCIÓN PRINCIPAL ---
def main():
    aplicar_estilos()

    if 'autenticado' not in st.session_state:
        st.session_state.autenticado = False

    # --- PANTALLA DE ACCESO ---
    if not st.session_state.autenticado:
        mostrar_cabecera_login()
        col_esp, col_form, col_esp2 = st.columns([1, 2, 1])

        with col_form:
            tab_login, tab_reg = st.tabs(["🔐 Iniciar Sesión", "👤 Crear Cuenta"])

            with tab_login:
                with st.form("l_form"):
                    u = st.text_input("Usuario").lower().strip()
                    p = st.text_input("Contraseña", type="password")
                    if st.form_submit_button("Entrar al Sistema", use_container_width=True):
                        db = auth._cargar_usuarios()
                        if db.get(u) == auth._hash_password(p):
                            st.session_state.autenticado = True
                            st.session_state.usuario = u
                            st.rerun()
                        else:
                            st.error("Credenciales incorrectas")

            with tab_reg:
                with st.form("r_form"):
                    new_u = st.text_input("Nuevo Usuario").lower().strip()
                    new_p = st.text_input("Nueva Contraseña", type="password")
                    conf_p = st.text_input("Confirmar Contraseña", type="password")
                    if st.form_submit_button("Registrar Usuario", use_container_width=True):
                        db = auth._cargar_usuarios()
                        if not new_u or len(new_p) < 4: st.warning("Datos insuficientes.")
                        elif new_u in db: st.error("El usuario ya existe.")
                        elif new_p != conf_p: st.error("Las contraseñas no coinciden.")
                        else:
                            with open("usuarios.csv", "a", newline="", encoding="utf-8") as f:
                                escritor = csv.DictWriter(f, fieldnames=["usuario", "password_hash"])
                                escritor.writerow({"usuario": new_u, "password_hash": auth._hash_password(new_p)})
                            st.success("✅ Cuenta creada.")
        return

    # --- PANTALLA PRINCIPAL (SIDEBAR COMPACTA) ---
    with st.sidebar:
        ruta_logo = "docs/skycast_logo_transparent.png"
        if os.path.exists(ruta_logo):
            st.image(ruta_logo, use_container_width=True)
        
        st.markdown(f"**Usuario:** {st.session_state.usuario.capitalize()}")
        st.markdown('<hr style="margin: 8px 0px;">', unsafe_allow_html=True)
        
        opcion = st.radio("Navegación", ["📈 Dashboard", "📝 Registrar Datos", "🔍 Historial"])
        
        st.write("##") # Espacio antes del botón
        if st.button("🚪 Cerrar Sesión", use_container_width=True, type="primary"):
            st.session_state.autenticado = False
            st.rerun()

    gestor = datos_csv.GestorDatosClima()

    # --- DASHBOARD ---
    if opcion == "📈 Dashboard":
        st.header("📊 Análisis Estadístico")
        zona = st.selectbox("Seleccione Zona", ["Centro", "Norte", "Sur", "Este", "Oeste"])
        stats = gestor.obtener_estadisticas_zona(zona)

        if stats:
            # 1. Métricas superiores
            c1, c2, c3 = st.columns(3)
            c1.metric("Temperatura Media", f"{stats['media_temp']:.1f} °C")
            c2.metric("Viento Máximo", f"{stats['max_viento']} km/h")
            c3.metric("Registros", stats['conteo'])

            st.write("---")
            
            # 2. Gráfica de Tendencia
            st.subheader("📈 Tendencia")
            df = pd.read_csv("clima_dataset.csv")
            df_zona = df[df['zona'] == zona].sort_values('fecha')
            st.line_chart(df_zona.set_index('fecha')['temperatura'], color="#58a6ff", height=300)

            # 3. Resumen de actividad (Ahora va primero)
            # Quitamos la línea gris superior para que se pegue a la gráfica como antes
            st.markdown(f"""
                <div style="margin-top: -40px; margin-bottom: 10px;">
                    <p style="font-size: 15px; margin: 0;">
                        📋 <b>Resumen de actividad:</b> Se han analizado los últimos <b>{stats['conteo']}</b> registros en la demarcación <b>{zona}</b>.
                    </p>
                </div>
            """, unsafe_allow_html=True)
            
            # 4. Avisos Meteorológicos (Ahora van debajo del resumen)
            # Usamos los datos dinámicos del CSV actualizado
            max_temp = df_zona['temperatura'].max()
            min_temp = df_zona['temperatura'].min()
            max_viento = df_zona['viento'].max()
            min_hum = df_zona['humedad'].min()

            if max_viento > 90:
                st.error(f"⚠️ **Aviso Meteorológico:** Ráfagas elevadas de viento ({max_viento} km/h) detectadas.")
            elif max_temp > 40:
                st.error(f"🔥 **Aviso Meteorológico:** Ola de calor extrema detectada ({max_temp} °C).")
            elif min_temp < 0:
                st.info(f"❄️ **Aviso Meteorológico:** Temperaturas bajo cero detectadas ({min_temp} °C).")
            elif min_hum < 20:
                st.warning(f"🔥 **Aviso Meteorológico:** Riesgo extremo de incendio por baja humedad ({min_hum}%).")

        else:
            st.info("ℹ️ No hay datos registrados para esta zona.")


        # --- PANTALLA: REGISTRO DE DATOS ---
    elif opcion == "📝 Registrar Datos":
        st.header("📝 Nuevo Registro")
        
        # 'clear_on_submit=True' vacía los campos automáticamente al dar clic en Guardar
        with st.form("form_reg", clear_on_submit=True):
            col_a, col_b = st.columns(2)
            f = col_a.date_input("Fecha", datetime.now())
            
            # Añadimos "Seleccione Zona" al principio de la lista
            z = col_b.selectbox("Zona", ["Seleccione Zona", "Centro", "Norte", "Sur", "Este", "Oeste"])
            
            # Precision de 0.1 y forzado de punto decimal
            temp = st.number_input("Temperatura (°C)", value=0.0, step=0.1, format="%.1f")
            hum = st.slider("Humedad (%)", 0, 100, 0)
            
            # Precision de 0.5 y forzado de punto decimal
            vie = st.number_input("Viento (km/h)", value=0.0, step=0.5, format="%.1f")

            if st.form_submit_button("Guardar"):
                if z == "Seleccione Zona":
                    st.error("⚠️ Por favor, elige una zona antes de guardar.")
                else:
                    datos = {"fecha": str(f), "zona": z, "temperatura": temp, "humedad": hum, "viento": vie}
                    
                    # Tu lógica original de validación y guardado
                    errores = validacion.validar_registro(datos)
                    if errores:
                        for err in errores: st.error(err)
                    else:
                        avisos = alertas.evaluar_alertas(datos)
                        for aviso in avisos: st.warning(aviso)
                        
                        if gestor.guardar_en_csv(datos):
                            st.success("✅ Datos guardados.")
                            # Al usar clear_on_submit, los widgets se resetean solos aquí

    elif opcion == "🔍 Historial":
        st.header("🔍 Consulta Histórica")
        if os.path.exists("clima_dataset.csv"):
            df_full = pd.read_csv("clima_dataset.csv")
            st.dataframe(df_full.sort_values('fecha', ascending=False), use_container_width=True)

if __name__ == "__main__":
    main()