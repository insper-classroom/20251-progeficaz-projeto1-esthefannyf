from utils import load_data, load_template, add_new, delete_note, edit_note, get_note_by_id



def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'], id=dados['id'])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)


def submit(titulo, detalhes):
    new_note = {'titulo': titulo, 'detalhes': detalhes}
    add_new(new_note)


def delete_nota(id):
    nota_id = id
    delete_note(nota_id)


def edit(id, titulo, detalhes):
    updated_note = {'titulo': titulo, 'detalhes': detalhes}
    edit_note(id, updated_note)

