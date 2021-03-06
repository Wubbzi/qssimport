from pathlib import Path


class StyleSheet:
    def __init__(self, base_dir, import_def_file, main_stylesheet=None):
        self.base_dir = Path(base_dir)
        self.base_stylesheet = import_def_file
        self.main_stylesheet = main_stylesheet
        self.__lines = []

        if not main_stylesheet:
            self.main_stylesheet = 'StyleSheet.qss'
        self.__extract_imports(self.base_stylesheet)

    def __extract_imports(self, file):
        root = self.base_dir
        path = root / file
        if path.exists():
            with open(path) as base_stylesheet:
                for line in base_stylesheet:
                    if line.startswith('@'):
                        line = line.strip('@import url')
                        css_file = line.strip('";()\r\n')
                        self.__read_stylesheet(root / css_file)

    def __read_stylesheet(self, file):
        with open(file, 'r') as stylesheet:
            stylesheet = stylesheet.read()
            self.__lines.append(stylesheet)

    def __create_stylesheet(self):
        if self.__lines:
            root = self.base_dir
            path = root / self.main_stylesheet
            with open(path, 'w+') as file:
                file.writelines(f"{item}\n" for item in self.__lines)

    def style_widget(self, widget):
        self.__create_stylesheet()
        with open(self.base_dir / self.main_stylesheet) as f:
            widget.setStyleSheet(f.read())
        return widget
