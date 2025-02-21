import sqlite3 
import os


def load_template(template_name):
    templates_dir = 'static/templates'
    file_path = os.path.join(templates_dir, template_name)

    with open(file_path, 'r', encoding='UTF-8') as file:
        return file.read()
    

    
def load_data():
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM notes")
    data = cur.fetchall()
    con.close()
    notes = [{'id': row[0], 'titulo': row[1], 'detalhes': row[2]} for row in data]
    return notes

def add_new(new_note):
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute("INSERT INTO notes (titulo, detalhes) VALUES (?, ?)", (new_note['titulo'], new_note['detalhes']))
    con.commit()
    con.close()

def delete_note(id):
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cur.execute("DELETE FROM notes WHERE id = ?", (id,))
    con.commit()
    con.close()








    
