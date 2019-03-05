from pathlib import Path


class StyleSheet:
    def __init__(self, base_dir, import_def_file, main_stylesheet=None):
        self.base_dir = Path(base_dir)
        self.base_stylesheet = import_def_file
        self.main_stylesheet = main_stylesheet

        if not main_stylesheet:
            self.main_stylesheet = 'mainStyle.qss'

        self.__lines = []
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

    def create_stylesheet(self):
        root = self.base_dir
        path = root / self.main_stylesheet
        if self.__lines:
            with open(path, 'w+') as file:
                file.writelines(f"{item}\n" for item in self.__lines)
