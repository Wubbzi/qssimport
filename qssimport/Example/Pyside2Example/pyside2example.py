from PySide2.QtCore import QSize
from PySide2.QtWidgets import QWidget, QApplication, QLineEdit, QGridLayout, QPushButton
from qssimport.stylesheet import StyleSheet
import pathlib



if __name__ == '__main__':

    # Path to the stylesheets directory
    stylesheet_directory = pathlib.Path().resolve().parent/'rc/stylesheet'
    # The name of the stylesheet qssimport creates
    main_stylesheet = stylesheet_directory / 'Style.qss'
    # Stylesheet with the import statements
    imports_stylesheet = stylesheet_directory / 'import.qss'
    stylesheet = StyleSheet(base_dir=stylesheet_directory,
                                       import_def_file=imports_stylesheet,
                                       main_stylesheet=main_stylesheet)
    app = QApplication([])
    widget = QWidget()
    stylesheet.style_widget(widget)

    layout = QGridLayout()
    widget.setLayout(layout)
    le = QLineEdit(widget)
    btn = QPushButton('Push Button')
    le.setText('wubalubadubdub')
    size = QSize(116,25)
    le.setFixedSize(size)
    btn.setFixedSize(size)
    layout.addWidget(btn)
    layout.addWidget(le)
    widget.setFixedSize(140,80)

    widget.show()
    app.exit(app.exec_())
