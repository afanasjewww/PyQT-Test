import sys
import os

from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QLineEdit, QHBoxLayout, QDialog, QDesktopWidget, QMessageBox
)

from Classes.User import User
from Classes.UserManager import UserManager

pass


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        #region Components Main Window
        self.setWindowTitle("ASML Testing App")
        self.setGeometry(100,100,800,600)
        self.center_main_window()

        self.setStyleSheet("background-color: #313338;")

        self.text_login_input = QLineEdit(self)
        self.text_login_input.setFixedSize(250,40)
        self.text_login_input.setPlaceholderText("Login")
        self.text_login_input.setStyleSheet("""
                        QLineEdit {
                            border: 0px solid white;
                            border-radius: 5px;    
                            color: #DADADA;
                            font-size: 12px;
                            font-weight: 900;
                            background-color: #383A40;
                        }
                        """)

        self.text_password_input = QLineEdit(self)
        self.text_password_input.setFixedSize(250,40)
        self.text_password_input.setPlaceholderText("Password")
        self.text_password_input.setEchoMode(QLineEdit.Password)
        self.text_password_input.setStyleSheet("""
                                QLineEdit {
                                    border: 0px solid white;
                                    border-radius: 5px;    
                                    color: #DADADA;
                                    font-size: 12px;
                                    font-weight: 900;
                                    background-color: #383A40;
                                }
                                """)

        self.button_login = QPushButton('Log In', self)
        self.button_login.setFixedSize(250,40)
        self.button_login.clicked.connect(self.submit_login)
        self.button_login.setStyleSheet("""
                    QPushButton {
                        background-color: #1E1F22;
                        color: white;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #2B2D31;
                    }
                """)

        self.button_register = QPushButton('Register', self)
        self.button_register.setFixedSize(250, 40)
        self.button_register.clicked.connect(self.open_register_window)
        self.button_register.setStyleSheet("""
                    QPushButton {
                        background-color: #1E1F22;
                        color: white;
                        border-radius: 5px;
                    }
                    QPushButton:hover {
                        background-color: #2B2D31;
                    }
                """)
        #endregion

        #region Main Window
        h_layout_text = QHBoxLayout()
        h_layout_text.addStretch(1)
        h_layout_text.addWidget(self.text_login_input)
        h_layout_text.addStretch(1)

        h_layout_password = QHBoxLayout()
        h_layout_password.addStretch(1)
        h_layout_password.addWidget(self.text_password_input)
        h_layout_password.addStretch(1)

        h_layout_button_login = QHBoxLayout()
        h_layout_button_login.addStretch(1)
        h_layout_button_login.addWidget(self.button_login)
        h_layout_button_login.addStretch(1)

        h_layout_button_register = QHBoxLayout()
        h_layout_button_register.addStretch(1)
        h_layout_button_register.addWidget(self.button_register)
        h_layout_button_register.addStretch(1)

        layout = QVBoxLayout()
        layout.addStretch(1)
        layout.addLayout(h_layout_text)
        layout.addLayout(h_layout_password)
        layout.addLayout(h_layout_button_login)
        layout.addLayout(h_layout_button_register)
        layout.addStretch(1)

        self.setLayout(layout)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = os.path.join(current_dir, 'resources')
        file_path = os.path.join(resources_dir, 'users.json')

        if not os.path.exists(resources_dir):
            os.makedirs(resources_dir)

        self.user_manager = UserManager(file_path)
        #endregion


    def center_main_window(self):
        screen_size = QDesktopWidget().availableGeometry()
        window_size = self.frameGeometry()
        window_size.moveCenter(screen_size.center())
        self.move(window_size.topLeft())

    def open_register_window(self):
        self.register_window = RegisterWindow(self)
        self.register_window.exec_()

    def submit_login(self):
        login = self.text_login_input.text()
        password = self.text_password_input.text()

        if login == "":
            self.show_error_message("Please Enter Login")
            return
        elif password == "":
            self.show_error_message("Please Enter Password")
            return


        if self.user_manager.validate_user(login,password):
            self.show_success_message(f"Welcome, {login}!")
            self.text_login_input.clear()
            self.text_password_input.clear()
        else:
            self.show_error_message("Invalid login or password. Please try again.")




    def show_success_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Login Successful")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Login Failed")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()



class RegisterWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        #region Components Register Window
        self.setWindowTitle("Register New User")
        self.setGeometry(100,100,400,300)
        self.center_register_window()

        self.label = QLabel()
        self.label.setText("Register a New User")
        self.label.setStyleSheet('''font-size: 20px; font-weight: 700;''')

        self.text_login = QLineEdit(self)
        self.text_login.setPlaceholderText("Login")
        self.text_login.setFixedSize(250,30)
        self.text_login.setStyleSheet("""
                                        QLineEdit {
                                            border: 0px solid white;
                                            border-radius: 5px;    
                                            color: #DADADA;
                                            font-size: 12px;
                                            font-weight: 900;
                                            background-color: #383A40;
                                        }
                                        """)

        self.text_password = QLineEdit(self)
        self.text_password.setPlaceholderText("Password")
        self.text_password.setEchoMode(QLineEdit.Password)
        self.text_password.setFixedSize(250,30)
        self.text_password.setStyleSheet("""
                                        QLineEdit {
                                            border: 0px solid white;
                                            border-radius: 5px;    
                                            color: #DADADA;
                                            font-size: 12px;
                                            font-weight: 900;
                                            background-color: #383A40;
                                        }
                                        """)

        self.text_name = QLineEdit(self)
        self.text_name.setPlaceholderText("Name")
        self.text_name.setFixedSize(250,30)
        self.text_name.setStyleSheet("""
                                        QLineEdit {
                                            border: 0px solid white;
                                            border-radius: 5px;    
                                            color: #DADADA;
                                            font-size: 12px;
                                            font-weight: 900;
                                            background-color: #383A40;
                                        }
                                        """)

        self.text_surname = QLineEdit(self)
        self.text_surname.setPlaceholderText("Surname")
        self.text_surname.setFixedSize(250,30)
        self.text_surname.setStyleSheet("""
                                        QLineEdit {
                                            border: 0px solid white;
                                            border-radius: 5px;    
                                            color: #DADADA;
                                            font-size: 12px;
                                            font-weight: 900;
                                            background-color: #383A40;
                                        }
                                        """)

        self.button_submit = QPushButton("Submit", self)
        self.button_submit.clicked.connect(self.submit_registration)
        self.button_submit.setFixedSize(250,40)
        self.button_submit.setStyleSheet("""
                            QPushButton {
                                background-color: #1E1F22;
                                color: white;
                                border-radius: 5px;
                            }
                            QPushButton:hover {
                                background-color: #2B2D31;
                            }
                        """)
        #endregion

        #region Layout for Registration Window
        h_layout_label = QHBoxLayout()
        h_layout_label.addStretch(1)
        h_layout_label.addWidget(self.label)
        h_layout_label.addStretch(1)

        h_layout_login = QHBoxLayout()
        h_layout_login.addStretch(1)
        h_layout_login.addWidget(self.text_login)
        h_layout_login.addStretch(1)

        h_layout_password = QHBoxLayout()
        h_layout_password.addStretch(1)
        h_layout_password.addWidget(self.text_password)
        h_layout_password.addStretch(1)

        h_layout_name = QHBoxLayout()
        h_layout_name.addStretch(1)
        h_layout_name.addWidget(self.text_name)
        h_layout_name.addStretch(1)

        h_layout_surname = QHBoxLayout()
        h_layout_surname.addStretch(1)
        h_layout_surname.addWidget(self.text_surname)
        h_layout_surname.addStretch(1)

        h_layout_button = QHBoxLayout()
        h_layout_button.addStretch(1)
        h_layout_button.addWidget(self.button_submit)
        h_layout_button.addStretch(1)

        layout = QVBoxLayout()
        layout.addStretch(1)  # Add stretch to push everything down a bit
        layout.addLayout(h_layout_label)
        layout.addSpacing(25)
        layout.addLayout(h_layout_login)
        layout.addLayout(h_layout_password)
        layout.addLayout(h_layout_name)
        layout.addLayout(h_layout_surname)
        layout.addLayout(h_layout_button)
        layout.addStretch(1)  # Add stretch to push everything up a bit

        self.setLayout(layout)
        #endregion

    def submit_registration(self):
        name = self.text_name.text()
        surname = self.text_surname.text()
        login = self.text_login.text()
        password = self.text_password.text()

        new_user = User(login, password, name, surname)

        current_dir = os.path.dirname(os.path.abspath(__file__))
        resources_dir = os.path.join(current_dir, 'resources')
        file_path = os.path.join(resources_dir, 'users.json')

        if not os.path.exists(resources_dir):
            os.makedirs(resources_dir)

        self.user_manager = UserManager(file_path)

        if self.user_manager.user_exists(login):
            self.show_error_message(f"User with login '{login}' already exists!")
            return

        try:
            self.user_manager.save_user(new_user)
            self.show_success_message(name)
            self.accept()
        except Exception as e:
            self.show_error_message(f"Error saving user: {e}")


    def show_success_message(self, name):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Registration Successful")
        msg.setText(f"User {name} has been successfully registered!")
        msg .setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def show_error_message(self, error_message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        msg.setText(error_message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


    def center_register_window(self):
        screen_size = QDesktopWidget().availableGeometry()
        window_size = self.frameGeometry()
        window_size.moveCenter(screen_size.center())
        self.move(window_size.topLeft())



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())