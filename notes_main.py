from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout


import json


app = QApplication([])


'''Заметки в json'''
notes = {
    "Добро пожаловать!" :{
        "текст" : "Это сомое лучшее приложениедля заметок в мире!" ,
        "теги" : ["добро", "инструкция"]
    }
}
with open("notes_data.json", "w") as file:
    json.dump(notes, file)

'''Интерфейс'''
#параментры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)


#виджеты окна приложения 
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')


button_note_create = QPushButton('Создать заметку') # появляется окно с полем
button_note_del = QPushButton('Удалисть заметку')
button_note_save = QPushButton('Сохранить заметку')


field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Спиосок тегов')


#расположение виджетов по лейаутом
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)
row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2.addLayout(row_1)
row_2.addLayout(row_2)



col_2.addWidget(list_tags_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3 = QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)


col_2.addLayout(row_3)
col_2.addLayout(row_4)


layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)

'''Работа с текстом заметки'''
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, "Добавить заметку", "Название заметки:")
    if ok and note_name !="":
        notes[note_name] = {"текст" : "", "теги" : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[key]["теги"])

'''Функционал приложения'''  
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(Key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
    list_tags.addItems(notes[key]["теги"])

def save_note():
    if list_notect.selestedItems():
        key = list_notes.selestedItems()[0].text()
        notes[key]["Текст"] = field_text.toPlainText()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Заметка для сохрания не выбрана!")

'''Работа с тегами заметки'''
def add_tag():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = field_tag.text()
        if not tag in notes[key]["теги"]:
            notes[key]["теги"].append(tag)
            list_tags.addItem(tag)
            field_tag.clear()
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для добавления тега не виыброна!') 


def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        list_tags.clear()
        list_tags.selectedItems(notes[key]["теги"])
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    else:
        print("Тег для удаление не вибран")

def sreach_tag():
    print(button_tag_search.text())
    tag = field_tag.text()
    if button_tag.text() == "Искать заметки по тегу":
        print(tag)
        notes_filtered = {}
        for note in notes:
            if tag in notes[note]["теги"]:
                notes_filtered[note]=notes[note]
        button_tag_search.setText("Сюросить поиск")
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes_filtered)
        print(button_tag_search.text())
    elif button_tag_search.text() == "Сбросить поиск":
        field_tag.clear()
        list_notes.clear()
        list_tags.clear()
        list_notes.addItems(notes)
        button_tag_search.setText("Искать заметки по тегу")
        print(button_tag_search.text())
    else:
        pass



''' Запуск приложения'''
list_notes.itemClicked.connect(show_note)
notes_win.show()

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)
app.exec_()
