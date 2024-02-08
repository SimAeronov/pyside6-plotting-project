from os import path
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import QSizePolicy

from pandas import read_csv

def generate_plot(parent_widget, file_path):

    if file_path:
        dataframe = read_csv(file_path)
        figure = Figure()

        # Set color and title as file name without extension
        figure.patch.set_facecolor("#918e8e")
        figure.suptitle(path.splitext(path.basename(file_path))[0])
        axis = figure.add_subplot()
        if parent_widget.plot_scatter_checkbox.isChecked():
            axis.scatter(dataframe["x"].to_list(), dataframe["y"].to_list())
        else:
            axis.plot(dataframe["x"].to_list(), dataframe["y"].to_list())
        
        canvas = FigureCanvasQTAgg(figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        index_of_horizontal_spacer = parent_widget.central_widget_vertical_layout.indexOf(parent_widget.plot_horizontal_spacer)
        parent_widget.central_widget_vertical_layout.insertWidget(index_of_horizontal_spacer, canvas)

        toolbar = NavigationToolbar2QT(canvas, parent_widget)
        parent_widget.central_widget_vertical_layout.insertWidget(index_of_horizontal_spacer, toolbar)