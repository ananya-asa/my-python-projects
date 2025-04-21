import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLineEdit, QMessageBox

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 400)

        self.tasks = load_tasks()

        self.layout = QVBoxLayout()

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter your task...")
        self.layout.addWidget(self.task_input)

        self.task_list = QListWidget()
        self.task_list.addItems(self.tasks)
        self.layout.addWidget(self.task_list)

        btn_layout = QHBoxLayout()

        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        btn_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Remove Task")
        self.remove_button.clicked.connect(self.remove_task)
        btn_layout.addWidget(self.remove_button)

        self.layout.addLayout(btn_layout)
        self.setLayout(self.layout)

    def add_task(self):
        task = self.task_input.text().strip()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            save_tasks(self.tasks)
            self.task_input.clear()
        else:
            QMessageBox.warning(self, "Warning", "Please enter a task!")

    def remove_task(self):
        selected = self.task_list.currentRow()
        if selected >= 0:
            task = self.tasks.pop(selected)
            self.task_list.takeItem(selected)
            save_tasks(self.tasks)
        else:
            QMessageBox.warning(self, "Warning", "Please select a task to remove!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
