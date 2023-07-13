import sys
import cv2
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import *

from main_ui import *
from function import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSobel.clicked.connect(self.divide_sobel_sketch_flag)
        self.ui.btnLaplacian.clicked.connect(self.divide_laplacian_sketch_flag)
        self.ui.btnThreshold1.clicked.connect(self.adaptiveThreshold1_cartoon_flag)
        self.ui.btnThreshold2.clicked.connect(self.stylization_cartoon_flag)
        self.ui.btnstylization.clicked.connect(self.madaptiveThreshold2_cartoon_flag)
        self.ui.btnblue.clicked.connect(self.b_flag)
        self.ui.btnGreen.clicked.connect(self.g_flag)
        self.ui.btnred.clicked.connect(self.r_flag)
        self.ui.btnOpen.clicked.connect(self.open_video)

        #self.video_capture = cv2.VideoCapture(0)  Get frame from Webcam

        # Create a timer for updating the video display
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_video)
        self.timer.start(30)
        # Exit
        self.ui.btnExit.clicked.connect(self.close)
        ## SHOW ==> MAIN WINDOW
        self.show()

    def update_video(self):
        # Read the next frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            # Convert the frame to RGB format
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # Create QImage from the frame
            image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
            # Create QPixmap from the QImage
            pixmap = QPixmap.fromImage(image)
            # Scale the QPixmap to fit the labels' size
            scaled_pixmap = pixmap.scaled(self.ui.lblOrVideo.size(), Qt.KeepAspectRatio)
            # Set the QPixmap on the label
            self.ui.lblOrVideo.setPixmap(scaled_pixmap)

    def open_video(self):
        self.filename = QFileDialog.getOpenFileName(filter="AVI(*.avi);;MOV(*.mov);;MP4(*.mp4)")[0]
        self.capture = cv2.VideoCapture(self.filename)
        self.video_capture = self.capture
        self.video_capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)

    def divide_sobel_sketch_flag(self):
        self.timer.timeout.connect(self.divide_sobel_sketch)
        self.timer.start(30)

    def divide_sobel_sketch(self):
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.divide_sobel_sketch_Filter(self,frame)

    def divide_laplacian_sketch_flag(self):
        self.timer.timeout.connect(self.divide_laplacian_sketch)
        self.timer.start(30)

    def divide_laplacian_sketch(self):
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.divide_laplacian_sketch_Filter(self, frame)

    def adaptiveThreshold1_cartoon_flag(self):
        self.timer.timeout.connect(self.tadaptiveThreshold1_cartoon)
        self.timer.start(30)

    def adaptiveThreshold1_cartoon(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.adaptiveThreshold1_cartoon_Filter(self, frame)

    def stylization_cartoon_flag(self):
        self.timer.timeout.connect(self.stylization_cartoon)
        self.timer.start(30)

    def stylization_cartoon(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.stylization_cartoon_Filter(self, frame)

    def madaptiveThreshold2_cartoon_flag(self):
        self.timer.timeout.connect(self.adaptiveThreshold2_cartoon)
        self.timer.start(30)

    def adaptiveThreshold2_cartoon(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.adaptiveThreshold2_cartoon_Filter(self, frame)

    def b_flag(self):
        self.timer.timeout.connect(self.b)
        self.timer.start(30)

    def b(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.Blue(self, frame)

    def r_flag(self):
        self.timer.timeout.connect(self.r)
        self.timer.start(30)

    def r(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.Red(self, frame)

    def g_flag(self):
        self.timer.timeout.connect(self.g)
        self.timer.start(30)

    def g(self):
        # Read the current frame from the video capture
        ret, frame = self.video_capture.read()
        if ret:
            FilterFunction.Green(self, frame)

    def closeEvent(self, event):
        # Release the video capture and stop the timer
        self.video_capture.release()
        self.timer.stop()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())