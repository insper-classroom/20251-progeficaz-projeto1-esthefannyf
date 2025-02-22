from flask import Flask, render_template_string, request, redirect, render_template
import views
from utils import load_data, get_note_by_id, edit_note


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


@app.route('/edit/<int:id>', methods=['GET'])
def edit_note_page(id):
    note = get_note_by_id(id)
    if note:
        return render_template('edit.html', id=note['id'], titulo=note['titulo'], detalhes=note['detalhes'])
    return redirect('/')
    
@app.route('/save_edit', methods=['POST'])
def save_edit():
    note_id = request.form['id']
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']
    uptaded_note = {'titulo': titulo, 'detalhes': detalhes}
    views.edit(note_id, uptaded_note)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update_note():
    note_id = request.form['id']
    titulo = request.form['titulo']
    detalhes = request.form['detalhes']
    updated_note = {'titulo': titulo, 'detalhes': detalhes}
    edit_note(note_id, updated_note)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)