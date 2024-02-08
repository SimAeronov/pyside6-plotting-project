from PySide6.QtWidgets import QFileDialog
from os import path


def browse_file_button_clicked(parent_widget):
    file_path, _ = QFileDialog.getOpenFileName(
        parent=parent_widget,
        caption="Select CSV file",
        dir=path.join(path.curdir, "csv_data"),
        filter="CSV Files (*.csv)",
    )
    parent_widget.file_path_line_edit.setText(file_path)
    parent_widget.file_path_line_edit.setCursorPosition(len(file_path))
