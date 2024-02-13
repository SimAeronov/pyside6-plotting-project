from PySide6.QtWidgets import QFileDialog
from os import path

from qt_code.plotting_functionality import generate_plot
from pandas import read_csv
from custom_math.custom_math import simpsons_rule

def browse_file_button_clicked(parent_widget):
    file_path, _ = QFileDialog.getOpenFileName(
        parent=parent_widget,
        caption="Select CSV file",
        dir=path.join(path.curdir, "csv_data"),
        filter="CSV Files (*.csv)",
    )
    parent_widget.file_path_line_edit.setText(file_path)
    parent_widget.file_path_line_edit.setCursorPosition(len(file_path))

def plot_data_button_clicked(parent_widget):
    file_path = parent_widget.file_path_line_edit.text()
    generate_plot(parent_widget, file_path)


def integrate_button_clicked(parent_widget):
    file_path = parent_widget.file_path_line_edit.text()
    if file_path:
        dataframe = read_csv(file_path)
        x_column = dataframe.iloc[:, 0].tolist() 
        y_column = dataframe.iloc[:, 1].tolist()
        integration_result = simpsons_rule(x=x_column, y=y_column)
        parent_widget.integration_label.setText(f"Area under the curve: {integration_result}")