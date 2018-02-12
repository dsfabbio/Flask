from flask import Flask, render_template

# Inicializa a aplicacao instanciando Flask
app = Flask(__name__)

# Atribui uma rota ao hello_world
@app.route('/')
def hello_world():
	return 'Hello World!'
  
  
# Atribui uma rota para acessar consulta.html
@app.route('/consulta')
def pagina_inicial():
    return render_template('consulta.html')

# Roda a aplicacao em: http://localhost:8085
app.run(debug=True,port=8085)
