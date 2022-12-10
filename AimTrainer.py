import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import random
import time
from PyQt5 import QtGui
from PyQt5 import QtCore, QtMultimedia
from PyQt5.QtWidgets import QLineEdit
import ImageProcessing


class Window(QMainWindow):
    # Set up main window and add a title
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(
            200, 100, ImageProcessing.length, ImageProcessing.width)
        self.setWindowTitle('Aim Lab')
        self.initUI()

    # Initialize all the labels, buttons, and necessary variables
    def initUI(self):
        self.second = 40  # Total game time
        self.points = 0  # initialize score
        self.difficulty_level = 1  # initialize difficulty level

        # setting lobby background
        # initialize timer label
        self.label1 = QLabel(self)
        self.label1.setText("Timer")
        self.label1.setFont(QFont('Arial', 20))
        self.label1.setGeometry(
            0, 0, ImageProcessing.length, ImageProcessing.width)
        self.label1.setStyleSheet(
            "background-image : url(Lobby_background.png); border : 0px solid blue")
        self.label1.move(0, 0)

        # initialize initial_countdown label
        self.label2 = QLabel(self)
        self.label2.setText("Initial_countdown")

        # set up background image after game starts
        self.label3 = QLabel(self)
        self.label3.hide()
        self.label3.setGeometry(
            0, 0, ImageProcessing.length, ImageProcessing.width)
        self.label3.setStyleSheet(
            "background-image : url(game_over.png); border : 0px solid blue")
        self.label3.move(0, 0)

        # initialize score label
        self.label4 = QLabel(self)
        self.label4.setText("")
        self.label4.setStyleSheet("color: white")
        self.label4.move(620, 640)
        font = QFont()
        font.setPointSize(24)
        self.label4.setFont(font)
        self.label4.adjustSize()
        self.label4.hide()

        # initialize score label
        self.label5 = QLabel(self)
        self.label5.setText("score:" + str(self.points))
        self.label5.setStyleSheet("color: pink")
        self.label5.move(1350, 0)
        self.label5.setFont(font)
        self.label5.adjustSize()
        self.label5.hide()

        # create start button
        self.b1 = QPushButton(self)
        self.b1.setGeometry(100, 200, 100, 50)
        self.b1.setStyleSheet("border : 0px solid black")
        self.b1.setText("")
        self.b1.setIcon(QtGui.QIcon("startButton.png"))
        self.b1.setIconSize(QtCore.QSize(100, 100))
        self.b1.move(375, 650)
        font.setPointSize(16)
        self.b1.setFont(font)
        self.b1.clicked.connect(self.start)

        # regular cursor
        QApplication.setOverrideCursor(Qt.ArrowCursor)

        # create target
        self.b3 = QPushButton("", self)
        self.b3.setGeometry(200, 150, 50, 50)
        self.b3.setStyleSheet(
            "border-radius : 25; border : 0px solid black")
        self.b3.clicked.connect(self.target)
        self.b3.setIcon(QtGui.QIcon("target.png"))
        self.b3.setIconSize(QtCore.QSize(75, 75))
        self.b3.move(200, 420)
        self.b3.hide()

        # creat 2 game modes
        # Easy mode
        self.b4 = QPushButton(self)
        self.b4.setText("EASY")
        self.b4.move(375, 560)
        self.b4.setFont(font)
        self.b4.clicked.connect(self.easy)

        # Hard mode
        self.b5 = QPushButton(self)
        self.b5.setText("HARD")
        self.b5.move(375, 600)
        self.b5.setFont(font)
        self.b5.clicked.connect(self.hard)

        # Initialize countdown time
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.timer.setInterval(1000)

        # intialize target exist time
        self.timer1 = QTimer()
        self.timer1.timeout.connect(self.target)
        self.timer1.setInterval(1000)

        # Creating a textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 60)
        self.textbox.resize(160, 40)
        self.textbox.setText("Mode Selection: DEFAULT")
        self.textbox.setFont(QFont('Arial', 8))

    # easy mode target size
    def easy(self):
        # easy mode
        self.b3.setIcon(QtGui.QIcon("target.png"))
        self.b3.setIconSize(QtCore.QSize(75, 75))
        self.textbox.setText("Mode Selection: EASY")

    # hard mode target size
    def hard(self):
        # hard mode
        self.b3.setIcon(QtGui.QIcon("target.png"))
        self.b3.setIconSize(QtCore.QSize(45, 45))
        self.textbox.setText("Mode Selection: HARD")

    # show target
    def aim(self):
        self.b3.show()
        self.b3.clicked.connect(self.target2)

    def start(self):
        # change background
        self.label1.setStyleSheet(
            "background-image : url(shooting_range.png); border : 0px solid blue")
        self.label1.move(0, 0)

        # Hidding the start and difficulty mode
        self.b1.hide()
        self.b4.hide()
        self.b5.hide()
        self.textbox.hide()

        # Change cursor:
        QApplication.setOverrideCursor(Qt.CrossCursor)

        # Start the initial countdown and show timer afterwards
        self.initial_countdown(3)
        self.aim()
        self.timer.start()
        self.timer1.start()
        self.label5.show()
        QApplication.processEvents()

    # countdown timer for the game
    def update(self):
        # decrease timer by 1 every second until it hits 0
        self.label1.setText(str(self.second))
        QApplication.processEvents()
        self.second = self.second - 1
        if self.second <= 0:
            self.game_over()

    # move target when target time expires
    def target(self):
        # Move target to a random position
        self.b3.move(random.randint(100, 1400), random.randint(0, 700))
        QApplication.processEvents()

    # Target move the random places after clicked
    def target2(self):
        self.b3.move(random.randint(100, 1400), random.randint(0, 700))
        QApplication.processEvents()
        # update score corresponds to difficulty level
        self.points = self.points + 2**(self.difficulty_level-1)
        self.difficulty()
        self.label5.setText("score:" + str(self.points))
        self.label5.adjustSize()
        QApplication.processEvents()
        self.label5.show()

        # reset the target exist time
        self.timer1.stop()
        self.timer1.start()

        # play gun sound when clicked
        QtMultimedia.QSound.play('gun_sound.wav')

    # initial count down before game starts
    def initial_countdown(self, t):
        # 3 seconds countdown before game start
        while t:
            self.label2.setFont(QFont('Arial', 32))
            self.label2.adjustSize()
            self.label2.move(740, 400)
            self.label2.setText(str(t))
            QApplication.processEvents()
            time.sleep(1)
            t -= 1
        self.label2.setText(" ")

    # change difficulty level depends on the score
    def difficulty(self):
        # decrease target exist time when difficulty level increases
        if self.points >= 3**(self.difficulty_level+1):
            self.difficulty_level = self.difficulty_level + 1
            self.timer1.setInterval(
                ((6-self.difficulty_level)/5) * 1000)  # decrease tarfet time by 0.2s

    # game over screen
    def game_over(self):
        # hide unnecessary labels, buttons, and show game over back ground and final score
        self.label1.hide()
        self.label2.hide()
        self.label3.show()
        self.b1.hide()
        self.b3.hide()
        self.b4.hide()
        self.b5.hide()
        self.textbox.hide()
        QApplication.setOverrideCursor(Qt.ArrowCursor)
        self.label4.setText("Final Score: " + str(self.points))
        self.label4.adjustSize()
        self.label4.show()
        self.label5.hide()

    # play gun sound when clicked
    def mousePressEvent(self, QMouseEvent):
        QtMultimedia.QSound.play('gun_sound.wav')

# initialize window function


def window():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


# call window function
window()

# call window function
window()
