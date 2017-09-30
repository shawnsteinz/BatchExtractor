from PyQt5.QtCore import (Qt)
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import (QGridLayout, QPushButton,
                             QGroupBox, QTreeView, QVBoxLayout,
                             QWidget)

NAME, STATUS = range(2)


class View(QWidget):
    def __init__(self, window):
        super(View, self).__init__()

        self.main_group_box = QGroupBox("Main")

        self.main_view = QTreeView()
        self.main_view.setRootIsDecorated(False)
        self.main_view.setAlternatingRowColors(True)

        self.discover = QPushButton("Discover")
        self.extract = QPushButton("Extract")

        main_layout = QGridLayout()
        main_layout.addWidget(self.main_view, 0, 0, 1, 4)
        main_layout.addWidget(self.extract, 1, 0, 1, 2)
        main_layout.addWidget(self.discover, 1, 2, 1, 2)
        self.main_group_box.setLayout(main_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.main_group_box)
        self.setLayout(main_layout)

        self.setWindowTitle("BatchExtractor")
        self.resize(1200, 600)

        self.model = QStandardItemModel(0, 2, window)

        self.model.setHeaderData(NAME, Qt.Horizontal, "Name")
        self.model.setHeaderData(STATUS, Qt.Horizontal, "Status")

        self.main_view.setModel(self.model)

    def add_file(self, name, status):
        self.model.insertRow(0)
        self.model.setData(self.model.index(0, NAME), name)
        self.model.setData(self.model.index(0, STATUS), status)

    def fill_tree(self, files):
        self.model.removeRows(0, self.model.rowCount())
        for item in files:
            self.add_file(item.display_name, item.status)
