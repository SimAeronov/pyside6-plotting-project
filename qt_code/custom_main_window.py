from os import path

from PySide6.QtWidgets import QMainWindow, QButtonGroup, QGroupBox, QHBoxLayout

from qt_designer.ui_plotting_tool import Ui_MainWindow

from qt_code.buttons_functionality import browse_file_button_clicked, plot_data_button_clicked, integrate_button_clicked

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent_app) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = parent_app

        styles_path = path.join("resources", "styles", "qstiles.css")
        with open(styles_path, "r") as stiles_file:
            self.setStyleSheet(stiles_file.read())

        self.button_group = QButtonGroup()
        self.button_group.setExclusive(True)
        self.button_group.addButton(self.plot_scatter_checkbox)
        self.button_group.addButton(self.plot_line_checkbox)

        self.browse_file_button.clicked.connect(self.browse_file_button_clicked)
        self.plot_data_button.clicked.connect(self.plot_data_button_clicked)
        self.integrate_button.clicked.connect(self.integrate_button_clicked)

    
    def browse_file_button_clicked(self):
        browse_file_button_clicked(parent_widget=self)

    def plot_data_button_clicked(self):
        plot_data_button_clicked(parent_widget=self)

    def integrate_button_clicked(self):
        integrate_button_clicked(parent_widget=self)

