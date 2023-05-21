import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtCore import Qt
import winsound

# 定义音符频率
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523
}

class ElectronicWoodenFish(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("电子木鱼")
        self.setGeometry(100, 100, 400, 400)

    def mousePressEvent(self, event):
        # 鼠标点击事件处理函数
        self.play_sound('C4')

    def play_sound(self, note):
        # 播放音符声音的函数
        frequency = notes[note]
        winsound.Beep(frequency, 1000)  # 使用winsound库播放声音

    def paintEvent(self, event):
        # 绘图事件处理函数
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # 抗锯齿渲染
        painter.setPen(Qt.NoPen)  # 设置无边框
        painter.setBrush(QBrush(Qt.white))  # 设置画刷颜色为白色

        painter.fillRect(event.rect(), QColor(0, 0, 0))  # 绘制黑色背景
        painter.drawEllipse(100, 100, 200, 200)  # 绘制木鱼的椭圆轮廓
        painter.drawLine(200, 150, 200, 250)  # 绘制木鱼的竖线
        painter.drawLine(150, 200, 250, 200)  # 绘制木鱼的横线

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ElectronicWoodenFish()
    window.show()
    sys.exit(app.exec_())
