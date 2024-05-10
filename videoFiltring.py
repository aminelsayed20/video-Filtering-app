import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

class VideoFilter:
    def __init__(self, input_video):
        self.cap = cv2.VideoCapture(input_video)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)

        # Create the Tkinter window
        self.root = tk.Tk()
        self.root.title("Video Filter")

        # Create the buttons
        self.color_correction_btn = ttk.Button(self.root, text="Color Correction", command=self.apply_color_correction)
        self.noise_reduction_btn = ttk.Button(self.root, text="Noise Reduction", command=self.apply_noise_reduction)
        self.sharpening_btn = ttk.Button(self.root, text="Sharpening", command=self.apply_sharpening)
        self.blurring_btn = ttk.Button(self.root, text="Blurring", command=self.apply_blurring)
        self.distortion_btn = ttk.Button(self.root, text="Distortion", command=self.apply_distortion)
        self.quit_btn = ttk.Button(self.root, text="Quit", command=self.root.quit)

        # Arrange the buttons in the window
        self.color_correction_btn.grid(row=0, column=0, padx=10, pady=10)
        self.noise_reduction_btn.grid(row=0, column=1, padx=10, pady=10)
        self.sharpening_btn.grid(row=1, column=0, padx=10, pady=10)
        self.blurring_btn.grid(row=1, column=1, padx=10, pady=10)
        self.distortion_btn.grid(row=2, column=0, padx=10, pady=10)
        self.quit_btn.grid(row=2, column=1, padx=10, pady=10)

    def apply_color_correction(self):
        self.apply_filters(self.color_correction, brightness=60, contrast=1.2)

    def apply_noise_reduction(self):
        self.apply_filters(self.noise_reduction)

    def apply_sharpening(self):
        self.apply_filters(self.sharpening)

    def apply_blurring(self):
        self.apply_filters(self.blurring, kernel_size=(9, 9))

    def apply_distortion(self):
        self.apply_filters(self.distortion, distortion_factor=0.5)

    def apply_filters(self, filter_func, **kwargs):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break


            filtered_frame = filter_func(frame, **kwargs)
            cv2.imshow('Filtered Video', filtered_frame)

            # Delay the frame display to maintain the original frame rate
            delay = int(100 / self.fps)
            if cv2.waitKey(delay) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def color_correction(self, frame, brightness, contrast):
        adjusted = np.int16(frame)
        adjusted = (adjusted * contrast) + brightness
        adjusted = np.clip(adjusted, 0, 255)
        return np.uint8(adjusted)

    def noise_reduction(self, frame):
        denoised = cv2.fastNlMeansDenoisingColored(frame, None, 10, 10, 7, 21)
        return denoised

    def sharpening(self, frame):
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        sharpened = cv2.filter2D(frame, -1, kernel)
        return sharpened

    def blurring(self, frame, kernel_size):
        blurred = cv2.GaussianBlur(frame, kernel_size, 0)
        return blurred

    def distortion(self, frame, distortion_factor):
        rows, cols, _ = frame.shape
        map_x = np.ndarray(shape=(rows, cols, 1), dtype='float32')
        map_y = np.ndarray(shape=(rows, cols, 1), dtype='float32')

        for i in range(rows):
            for j in range(cols):
                map_x[i, j] = j + distortion_factor * j * (rows // 2 - i) / (rows // 2)
                map_y[i, j] = i

        distorted = cv2.remap(frame, map_x, map_y, cv2.INTER_LINEAR)
        return distorted

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    video_filter = VideoFilter('received_video.mp4')
    video_filter.run()
