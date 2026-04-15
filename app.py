from flask import Flask, render_template, request
import datos_csv
import auth

app = Flask(__name__)
gestor = datos_csv.GestorDatosClima()

@app.route('/')
def home():
    # Carga la página inicial sin datos
    return render_template('index.html', resultados=None, stats=None)

@app.route('/consultar', methods=['POST'])
def consultar():
    zona = request.form.get('zona') # Obtiene la zona del HTML
    if zona:
        zona = zona.title()
        resultados = gestor.consultar_por_zona(zona)
        stats = gestor.obtener_estadisticas_zona(zona)
        return render_template('index.html', resultados=resultados, stats=stats, zona_actual=zona)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)