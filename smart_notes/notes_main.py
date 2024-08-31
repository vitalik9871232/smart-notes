# Підключаємо бібліотеки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

#   Вікно програми

app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна
window.setWindowTitle("Smart Notes")
window.resize(main_width,main_height)
window.setStyleSheet('background-color:rgb(235, 231, 255);font-size:15px')

# ------------------------------Словник замітки

notes = {                       # Структура для зберігання заміток в json файл
    "мій день": {
        "text": "example text", 
        "tag": ["tag 1","tag 2"],
    }
}
def write_To_file():
    with open("notes_data.json", "w") as file:    # Записуємо структуру у json файл
        json.dump(notes, file, sort_keys=True)

#---------------------------- Eлементи інтерфейсу

text_editor = QTextEdit()          # Введення тексту замітки
text_editor.setStyleSheet(' background-color: rgb(255,255,0);')
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()         # Список заміток
list_widget_1.setStyleSheet('background-color: rgb(255,255,0);')

list_widget_2 = QListWidget()            # Список (Контактні дані)
list_widget_2.setStyleSheet('background-color: rgb(255,255,0);')

text_searcher = QLineEdit()        # Пошук  по тексту
text_searcher.setPlaceholderText('Введіть текст...')

tag_searcher = QLineEdit()
tag_searcher.setPlaceholderText('Введіть тег...')   # Пошук  по тегу

#Створення кнопок

make_note = QPushButton()
make_note.setStyleSheet('background-color: orange;')
make_note.setText("Створити замітку")                   

delete_note = QPushButton()
delete_note.setStyleSheet('background-color: orange;')
delete_note.setText("Видалити замітку")                  

save_note = QPushButton()
save_note.setStyleSheet('background-color: orange;')
save_note.setText("Зберегти замітку")                  

search_for_text = QPushButton()
search_for_text.setStyleSheet('background-color: orange;')
search_for_text.setText("Шукати замітку за текстом")         

search_for_tag = QPushButton()
search_for_tag.setStyleSheet('background-color: orange;')
search_for_tag.setText("Шукати замітку за тегом")           

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: rgb(255, 255, 0);')
add_to_note.setText("Додати до замітки")                   

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: rgb(255, 255, 0);')
unpin_to_note.setText("Відкріпити від замітки")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet('background-color: rgb(255, 255, 0);')
action_theme_btn.setText("Змінити тему")

#   Розміщення на макет

row1 = QHBoxLayout()              # горизонтальний додати і видалити замітку
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()              # - горизонтальний додати до замітки та відкріпити від замітки
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()              # вертикальний, ввести текст
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
   
col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Ввід данних:"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)

# Нижні 3 кнопки
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addWidget(action_theme_btn)

# Злиття
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

# Макет на екран

window.setLayout(layout_note) 

# Функціонал програми
  # Функції для заміток

def show_notes():           # Функція для роботи з замітками
    global key
    key = list_widget_1.selectedItems()[0].text()
    list_widget_2.clear()
    text_editor.setText(notes[key]["text"])
    list_widget_2.addItems(notes[key]["tag"])

def add_notes():           # Функція для додавання заміток
    name, ok = QInputDialog.getText(window, "Додати замітку", "Нова замітка")
    if name and ok:
        list_widget_1.addItem(name)
        notes[name] = {"text":"", "tag":[]}
    write_To_file()

def delete_notes():        # Функція для видалення заміток
    if list_widget_1.currentItem():    # Якщо вибрана замітка
        if key is notes:               # Якщо ця замітка є в словнику
            notes.pop(key)             # Видалення замітки з словника

            text_editor.clear()         # Очищення редактору, list_widget 1 та 2, та записування
            list_widget_1.clear()
            list_widget_2.clear()
            list_widget_1.addItem(notes)
            write_To_file()

# Функція для збереження заміток
def save_notes():
     if list_widget_1.currentItem():
         key = list_widget_1.currentItem().text()
         notes(key)["text"] = text_editor.toPlainText()
         write_To_file()

list_widget_1.itemClicked.connect(show_notes)
delete_note.clicked.connect(delete_notes)
save_note.clicked.connect(save_notes)
make_note.clicked.connect(add_notes)

with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_widget_1.addItems(notes)

# Закриття програми та показ

window.show()
app.exec_()
