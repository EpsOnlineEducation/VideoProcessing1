import cv2
from PySide2.QtCore import  Qt
from PySide2.QtGui import QPixmap, QImage
import numpy as np


class FilterFunction():

    ################################# SKETCH ######################################
    def divide_sobel_sketch_Filter(self, frame):
        # Filter sharpens images by sobel filter
        Sobel_kernel_sharpening = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])
        frame = cv2.filter2D(frame, -1, Sobel_kernel_sharpening)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        invertImage = 255 - gray

        # Blur image and remove noise with Gaussian filter
        blurred = cv2.GaussianBlur(invertImage, (15, 15), 0)
        invBlurred = 255 - blurred

        # divide each pixel in gray by each corresponding pixel in invBlurred.
        sketch = cv2.divide(gray, invBlurred, scale=256.0)
        sketch_frame_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)

        # Create QImage from the sketch frame
        sketch_image = QImage(sketch_frame_rgb.data, sketch_frame_rgb.shape[1], sketch_frame_rgb.shape[0],
                              QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)


    # Filter sharpens images by Laplacian filter
    def divide_laplacian_sketch_Filter(self, frame):
        laplacian_kernel_sharpening = np.array([[0, -1, 0],
                                      [-1, 5, -1],
                                      [0, -1, 0]])
        frame = cv2.filter2D(frame, -1, laplacian_kernel_sharpening)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        invertImage = 255 - gray

        # Blur image and remove noise with Gaussian filter
        blurred = cv2.GaussianBlur(invertImage, (15, 15), 0)
        invBlurred = 255 - blurred
        # divide each pixel in gray by each corresponding pixel in invBlurred.
        sketch = cv2.divide(gray, invBlurred, scale=256.0)
        sketch_frame_rgb = cv2.cvtColor(sketch, cv2.COLOR_GRAY2RGB)
        frame_rgb = cv2.cvtColor(sketch_frame_rgb, cv2.COLOR_BGR2RGB)
        cartoon_image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(cartoon_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)


    ##################### CARTOON ################################

    # Filter sharpens images by Thresholding
    def adaptiveThreshold1_cartoon_Filter(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 300, 300)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        frame_rgb = cv2.cvtColor(cartoon, cv2.COLOR_BGR2RGB)
        # Create QImage from the sketch frame
        sketch_image = QImage(frame_rgb.data, frame_rgb.shape[1], frame_rgb.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    # Filter sharpens images by stylization
    def stylization_cartoon_Filter(self, frame):
        cartoon_image = cv2.stylization(frame, sigma_s=10, sigma_r=0.25)
        # Create QImage from the sketch frame
        sketch_image = QImage(cartoon_image.data, cartoon_image.shape[1], cartoon_image.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    # Filter sharpens images by adaptiveThreshold
    def adaptiveThreshold2_cartoon_Filter(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 200, 200)

        cartoon_image = cv2.bitwise_and(color, color, mask=edges)
        # Create QImage from the sketch frame
        sketch_image = QImage(cartoon_image.data, cartoon_image.shape[1], cartoon_image.shape[0], QImage.Format_RGB888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    # Split channel Blue
    def Blue(self, frame):
        (h, w) = frame.shape[:2]
        zeros = np.zeros((h, w), dtype="uint8")
        (B, G, R) = cv2.split(frame)
        B = cv2.merge([B, zeros, zeros])
        # Create QImage from the sketch frame
        sketch_image = QImage(B.data, B.shape[1], B.shape[0], QImage.Format_BGR888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)


    # Split channel Green
    def Green(self, frame):
        (h, w) = frame.shape[:2]
        zeros = np.zeros((h, w), dtype="uint8")
        (B, G, R) = cv2.split(frame)
        G = cv2.merge([zeros, G, zeros])
        # Create QImage from the sketch frame
        sketch_image = QImage(G.data, G.shape[1], G.shape[0], QImage.Format_BGR888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)

    # Split channel Red
    def Red(self, frame):
        (h, w) = frame.shape[:2]
        zeros = np.zeros((h, w), dtype="uint8")
        (B, G, R) = cv2.split(frame)
        R = cv2.merge([zeros, zeros, R])
        # Create QImage from the sketch frame
        sketch_image = QImage(R.data, R.shape[1], R.shape[0], QImage.Format_BGR888)
        # Create QPixmap from the QImage
        sketch_pixmap = QPixmap.fromImage(sketch_image)
        # Scale the QPixmap to fit the sketch label's size
        scaled_sketch_pixmap = sketch_pixmap.scaled(self.ui.lblEditVideo.size(), Qt.KeepAspectRatio)
        # Set the QPixmap on the sketch label
        self.ui.lblEditVideo.setPixmap(scaled_sketch_pixmap)


