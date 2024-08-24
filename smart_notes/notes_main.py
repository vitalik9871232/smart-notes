from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from json import *

# Створення вікна

app = QApplication([])
window = QWidget()
window.resize(300,300)
window.setWindowTitle("Smart Notes")
# Єлементи

text_editor = QTextEdit() # Замітки
text_editor.setStyleSheet('background-color: rgb(255,255,0)')

list_Widget1 = QListWidget() # Список заміток
list_Widget2 = QListWidget() # Список тегів

list_Widget1.setStyleSheet('background-color: rgb(255,255,0)')
list_Widget2.setStyleSheet('background-color: rgb(255,255,0)')

text_Searcher = QLineEdit() # Пошук по тексту
tag_Searcher = QLineEdit() # Пошук по тегу

text_Searcher.setPlaceholderText("Введіть текст") 
tag_Searcher.setPlaceholderText("Введіть тег")

make_Note = QPushButton() # Кнопка додати замітку
delete_Note = QPushButton() # Кнопка видалити замітку
save_Note = QPushButton() # Кнопка зберегти замітку

make_Note.setText('Створити замітку')
delete_Note.setText('Видалити замітку')    # Встановлення текстів
save_Note.setText('Зберегти замітку')

add_To_Note = QPushButton() # Додати до замітки
unpin_To_Note = QPushButton() # Відкріпити до замітки

add_To_Note.setText('Додати до замітки')              #  Встановлення текстів
unpin_To_Note.setText('Відкріпити до замітки')

search_For_Text = QPushButton() # Пошук за текстом
search_For_Tag = QPushButton() # Пошук за тегом

search_For_Text.setText('Шукати за текстом')      # Встановлення текстів
search_For_Tag.setText('Шукати за тегом')

# Розміщення на макет

row1 = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

# Розміщуємо єлементи

row1.addWidget(add_To_Note)
row1.addWidget(unpin_To_Note)

col1.addWidget(text_editor)
col1.addWidget(QLabel('Список заміток:'))
col1.addWidget(list_Widget1)
col1.addWidget(row1)
col1.addWidget(save_Note)

col2.addWidget(QLabel('Список тегів:'))
col2.addWidget(list_Widget2)
col2.addWidget(search_For_Text)
col2.addWidget(search_For_Tag)
col2.addWidget(make_Note)
col2.addWidget(delete_Note)
col2.addWidget(save_Note)

# Розміщення макета на єкран

layout_note = QHBoxLayout()

layout_note.addLayout(col1)
layout_note.addLayout(col2)

window.setLayout(layout_note)

window.show()
app.exec_()