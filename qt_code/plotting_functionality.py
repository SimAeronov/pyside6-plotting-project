from os import path

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure
from PySide6.QtWidgets import (
    QSizePolicy,
    QPushButton,
    QDialog,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtCore import QTimer

from pandas import read_csv


class CustomNavigationToolbar(NavigationToolbar2QT):
    def __init__(self, canvas, parent=None, coordinates=True, current_index=0):
        super().__init__(canvas, parent, coordinates)

        self.current_index = current_index

        self.view_canvas_button = QPushButton("View")
        self.overlay_canvas_button = QPushButton("Add Overlay Plot")
        self.delete_canvas_button = QPushButton("Delete")

        self.view_canvas_button.setStyleSheet("background-color: #898888; padding: 5px;")
        self.overlay_canvas_button.setStyleSheet("background-color: #898888; padding: 5px;")
        self.delete_canvas_button.setStyleSheet("background-color: #898888; padding: 5px;")


        self.addWidget(self.view_canvas_button)
        self.addWidget(self.overlay_canvas_button)
        self.addWidget(self.delete_canvas_button)


def count_figure_canvases(parent_app):
    count = 0
    for index_of_widget in range(parent_app.central_widget_vertical_layout.count()):
        widget = parent_app.central_widget_vertical_layout.itemAt(
            index_of_widget
        ).widget()
        if isinstance(widget, FigureCanvasQTAgg):
            count += 1
    return count


def generate_plot(parent_widget, file_path):

    if count_figure_canvases(parent_app=parent_widget) >= 2:
        parent_widget.statusBar().setStyleSheet("color: red")
        parent_widget.statusBar().showMessage(
            "Cannot generate plot: Maximum number of plots reached."
        )
        QTimer.singleShot(5000, lambda: parent_widget.statusBar().clearMessage())
        return

    if file_path:
        dataframe = read_csv(file_path)
        x_column = dataframe.columns[0]
        y_column = dataframe.columns[1]

        figure = Figure()

        # Set color and set title = file name without extension
        figure.patch.set_facecolor("#7A7A7A")
        
        figure.patch.set_edgecolor("red")  # Add border color
        figure.patch.set_linewidth(3)  # Add border width

        figure.suptitle(path.splitext(path.basename(file_path))[0])
        axis = figure.add_subplot()
        if parent_widget.plot_scatter_checkbox.isChecked():
            axis.scatter(
                dataframe[x_column].to_list(),
                dataframe[y_column].to_list(),
                label=path.splitext(path.basename(file_path))[0],
            )
        else:
            axis.plot(
                dataframe[x_column].to_list(),
                dataframe[y_column].to_list(),
                label=path.splitext(path.basename(file_path))[0],
            )

        if parent_widget.plot_grid_checkbox.isChecked():
            axis.grid(True)

        axis.set_xlabel(x_column)
        axis.set_ylabel(y_column)

        canvas = FigureCanvasQTAgg(figure)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        index_of_horizontal_spacer = (
            parent_widget.central_widget_vertical_layout.indexOf(
                parent_widget.plot_horizontal_spacer
            )
        )
        parent_widget.central_widget_vertical_layout.insertWidget(
            index_of_horizontal_spacer, canvas
        )

        toolbar = CustomNavigationToolbar(
            canvas=canvas,
            parent=parent_widget,
            current_index=index_of_horizontal_spacer,
        )

        toolbar.view_canvas_button.clicked.connect(
            lambda: view_canvas_fullscreen(parent_widget, canvas)
        )
        toolbar.overlay_canvas_button.clicked.connect(
            lambda: overlay_plot(parent_widget, canvas)
        )
        toolbar.delete_canvas_button.clicked.connect(
            lambda: delete_plot(canvas, toolbar)
        )
        parent_widget.central_widget_vertical_layout.insertWidget(
            index_of_horizontal_spacer, toolbar
        )


def overlay_plot(parent_widget, canvas):
    file_path = parent_widget.file_path_line_edit.text()
    if file_path:
        dataframe = read_csv(file_path)
        x_column = dataframe.columns[0]
        y_column = dataframe.columns[1]
        axis = canvas.figure.axes[0]
        if parent_widget.plot_scatter_checkbox.isChecked():
            axis.scatter(
                dataframe[x_column].tolist(),
                dataframe[y_column].tolist(),
                label=path.splitext(path.basename(file_path))[0],
            )
        else:
            axis.plot(
                dataframe[x_column].tolist(),
                dataframe[y_column].tolist(),
                label=path.splitext(path.basename(file_path))[0],
            )
        axis.set_xlabel(x_column)
        axis.set_ylabel(y_column)

        axis.legend(loc="upper right")
        canvas.draw()


def delete_plot(canvas, toolbar):
    canvas.deleteLater()
    toolbar.deleteLater()


class FullScreenDialog(QDialog):
    def __init__(self, parent_app, canvas):
        super().__init__()
        self.setWindowTitle("Full Screen View")
        self.parent_app = parent_app

        # Create a new canvas widget with the shared figure
        self.canvas = canvas
        self.toolbar_fullscreen = NavigationToolbar2QT(canvas=self.canvas, parent=self)

        layout = QVBoxLayout()
        layout.addWidget(self.toolbar_fullscreen)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        self.showFullScreen()

    def hideEvent(self, event):
        self.canvas.setParent(self.parent_app)
        self.toolbar_fullscreen.setParent(self.parent_app)
        super().hideEvent(event)
        self.close()


def view_canvas_fullscreen(parent_app, canvas):
    fullscreen_dialog = FullScreenDialog(parent_app, canvas)
    fullscreen_dialog.destroyed.connect(
        lambda: refresh_main_window(parent_app=parent_app, canvas=canvas)
    )
    fullscreen_dialog.exec_()


def refresh_main_window(parent_app, canvas):
    canvas_size = canvas.size()
    fig = canvas.figure
    fig.set_size_inches(
        canvas_size.width() * 1.3 / fig.dpi, canvas_size.height() * 1.24 / fig.dpi
    )
    canvas.draw()
    toolbars = parent_app.findChildren(CustomNavigationToolbar)
    # Note: Here canvas_loc_index + 1 is to account for the fact that the toolbar is inserted before the canvas
    for toolbar in toolbars:
        if toolbar.canvas == canvas:
            canvas_loc_index = (
                parent_app.central_widget_vertical_layout.indexOf(toolbar) + 1
            )
            parent_app.central_widget_vertical_layout.insertWidget(
                canvas_loc_index, canvas
            )
            break
