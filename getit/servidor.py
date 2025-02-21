from flask import Flask, render_template_string, request, redirect
import views
from utils import load_data


app = Flask(__name__, template_folder='static/templates')


app.static_folder = 'static'

@app.route('/')
def index():
    return render_template_string(views.index())  
 
@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')
    detalhes = request.form.get('detalhes')
    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<int:id>', methods=['GET'])
def delete(id):
    views.delete_nota(id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)