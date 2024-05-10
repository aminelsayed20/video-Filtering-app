# This project is a video filter application built using Python and the OpenCV library.
# The application allows users to apply various filters to a video, including color correction, noise reduction, sharpening, blurring, and distortion.

Here's a breakdown of the key components of the project:

VideoFilter Class: This is the main class that handles the video processing and the Tkinter-based user interface.

Video Capture: The __init__ method initializes a cv2.VideoCapture object with the input video file. It also retrieves the video's width, height, and frames per second (FPS) properties.

Tkinter UI: The class creates a Tkinter window with several buttons, each corresponding to a different video filter. The buttons are arranged using the grid layout.

Filter Application: Each button's command method (e.g., apply_color_correction, apply_noise_reduction) calls the apply_filters method, which reads frames from the video capture and applies the corresponding filter function to each frame.

Filter Functions: The class defines several filter functions, such as color_correction, noise_reduction, sharpening, blurring, and distortion. These functions take the video frame as input and apply the desired filter, returning the modified frame.

Frame Display: The apply_filters method displays the filtered frames in a new window using cv2.imshow. It also adds a delay to maintain the original video frame rate.

The project demonstrates the integration of OpenCV's image processing capabilities with a Tkinter-based graphical user interface. Users can interact with the application by clicking on the different filter buttons, and the video filters are applied in real-time.

This project can be a useful starting point for anyone interested in developing video processing applications or exploring the combination of OpenCV and Tkinter for creating interactive media-related tools.
