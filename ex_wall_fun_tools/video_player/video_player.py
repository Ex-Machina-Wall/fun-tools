import cv2
import time
from PIL import Image, ImageEnhance
from ex_wall_frame_transmitter.constants import WIDTH, HEIGHT
import numpy as np
from ex_wall_frame_transmitter import FrameTransmitter
import logging

logging.basicConfig(level=logging.CRITICAL)


def get_frame(video_capture) -> np.array:
    """
    This is the main call that returns a frame of the GIF
    """
    success, image = video_capture.read()
    image = Image.fromarray(image)

    converter = ImageEnhance.Color(image)
    image = converter.enhance(3)
    frame = image.resize((WIDTH, HEIGHT))
    image_array = np.array(frame)
    return image_array



def main():
    from decouple import config
    video_capture = cv2.VideoCapture('downloaded_videos/sunset-lamp.mp4')
    transmitter = FrameTransmitter(destination_uri=config("DESTINATION_URI"))
    transmitter.start()
    cont = True
    while cont:
        transmitter.send_numpy_frame(get_frame(video_capture=video_capture))
        time.sleep(1 / 80)
    transmitter.stop()


if __name__ == "__main__":
    main()
