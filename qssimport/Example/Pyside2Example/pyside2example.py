from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QGridLayout, QPushButton
from qssimport import stylesheet
import pathlib

stylesheet_directory = f'{pathlib.Path().resolve().parent}/rc/stylesheet'
main_stylesheet = stylesheet_directory + '/MyStyle.qss'
imports_stylesheet = stylesheet_directory + '/import.qss'

stylesheet = stylesheet.StyleSheet(base_dir=stylesheet_directory,
                                   import_def_file=imports_stylesheet,
                                   main_stylesheet=main_stylesheet)
stylesheet.create_stylesheet()

app = QApplication([])

with open(main_stylesheet, 'r') as style:
    app.setStyleSheet(style.read())

widget = QWidget()
layout = QGridLayout()
widget.setLayout(layout)

le = QLineEdit(widget)
le.setText('Some green text...')

bottomButton = QPushButton('Bottom Button')
bottomButton.setObjectName('BottomButton')

layout.addWidget(QPushButton('Push Button'), 0, 0)
layout.addWidget(bottomButton, 1, 0)
layout.addWidget(le, 2, 0)

widget.show()
app.exit(app.exec_())
