from os import path

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import QSizePolicy, QPushButton, QDialog, QVBoxLayout, QMainWindow
from PySide6.QtCore import QSize, Signal

from pandas import read_csv

class CustomNavigationToolbar(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None, coordinates=True):
        super().__init__(canvas, parent, coordinates)

        self.view_canvas_button = QPushButton("View")
        self.overlay_canvas_button = QPushButton("Add Overlay Plot")
        self.delete_canvas_button = QPushButton("Delete")

        self.view_canvas_button.setStyleSheet("margin: 5px; padding: 5px;")
        self.overlay_canvas_button.setStyleSheet("padding: 5px;")
        self.delete_canvas_button.setStyleSheet("padding: 5px;")

        self.addWidget(self.view_canvas_button)
        self.addWidget(self.overlay_canvas_button)
        self.addWidget(self.delete_canvas_button)

def generate_plot(parent_widget, file_path):

    if file_path:
        dataframe = read_csv(file_path)
        x_column = dataframe.columns[0]
        y_column = dataframe.columns[1]

        figure = Figure()

        # Set color and title as file name without extension
        figure.patch.set_facecolor("#918e8e")
        figure.suptitle(path.splitext(path.basename(file_path))[0])
        axis = figure.add_subplot()
        if parent_widget.plot_scatter_checkbox.isChecked():
            axis.scatter(dataframe[x_column].to_list(), dataframe[y_column].to_list(), label=path.splitext(path.basename(file_path))[0])
        else:
            axis.plot(dataframe[x_column].to_list(), dataframe[y_column].to_list(), label=path.splitext(path.basename(file_path))[0])
        
        if parent_widget.plot_grid_checkbox.isChecked():
            axis.grid(True)
        
        axis.set_xlabel(x_column)
        axis.set_ylabel(y_column)
        
        canvas = FigureCanvasQTAgg(figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        index_of_horizontal_spacer = parent_widget.central_widget_vertical_layout.indexOf(parent_widget.plot_horizontal_spacer)
        parent_widget.central_widget_vertical_layout.insertWidget(index_of_horizontal_spacer, canvas)

        toolbar = CustomNavigationToolbar(canvas=canvas, parent=parent_widget)

        toolbar.view_canvas_button.clicked.connect(lambda: view_canvas_fullscreen(canvas))
        toolbar.overlay_canvas_button.clicked.connect(lambda: overlay_plot(canvas, parent_widget))
        toolbar.delete_canvas_button.clicked.connect(lambda: delete_plot(canvas, toolbar))
        parent_widget.central_widget_vertical_layout.insertWidget(index_of_horizontal_spacer, toolbar)

def overlay_plot(canvas, parent_widget):
    file_path = parent_widget.file_path_line_edit.text()
    if file_path:
        dataframe = read_csv(file_path)
        x_column = dataframe.columns[0]
        y_column = dataframe.columns[1]
        axis = canvas.figure.axes[0]
        if parent_widget.plot_scatter_checkbox.isChecked():
            axis.scatter(dataframe[x_column].tolist(), dataframe[y_column].tolist(), label=path.splitext(path.basename(file_path))[0])
        else:
            axis.plot(dataframe[x_column].tolist(), dataframe[y_column].tolist(), label=path.splitext(path.basename(file_path))[0])
        axis.set_xlabel(x_column)
        axis.set_ylabel(y_column)

        axis.legend(loc='upper right')
        canvas.draw()

def delete_plot(canvas, toolbar):
    canvas.deleteLater()
    toolbar.deleteLater()


class FullScreenDialog(QDialog):

    closed = Signal()

    def __init__(self, figure):
        super().__init__()
        self.setWindowTitle("Full Screen View")
        
        # Create a new canvas widget with the shared figure
        self.canvas = FigureCanvasQTAgg(figure)
        
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.showFullScreen()
    
    def closeEvent(self, event):
        self.closed.emit()

def view_canvas_fullscreen(canvas):
    fullscreen_dialog = FullScreenDialog(canvas.figure)
    fullscreen_dialog.closed.connect(lambda: refresh_main_window(canvas=canvas))
    fullscreen_dialog.exec_()

def refresh_main_window(canvas):
    parent = canvas.parentWidget()
    while parent:
        if isinstance(parent, QMainWindow):
            return parent
        parent = parent.parentWidget()
    current_size = parent.size()
    new_size = QSize(current_size.width() + 1, current_size.height() + 1)
    parent.resize(new_size)