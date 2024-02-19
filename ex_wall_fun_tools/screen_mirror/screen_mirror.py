import time
from PIL import ImageEnhance
from ex_wall_frame_transmitter.constants import WIDTH, HEIGHT
import numpy as np
from ex_wall_frame_transmitter import FrameTransmitter
import logging

from ex_wall_fun_tools.screen_mirror.capture_screen import capture_screenshot

# logging.basicConfig(level=logging.DEBUG)


def get_frame() -> np.array:
    """
    This is the main call that returns a frame of the GIF
    """
    image = capture_screenshot()

    converter = ImageEnhance.Color(image)
    # image = converter.enhance(3)
    frame = image.resize((WIDTH, HEIGHT))
    image_array = np.array(frame)
    return image_array


def main():
    from decouple import config
    transmitter = FrameTransmitter(destination_uri=config("DESTINATION_URI"))
    transmitter.start()
    cont = True
    while cont:
        transmitter.send_numpy_frame(pid_gain=30, np_frame=get_frame())
        time.sleep(1 / 30)
    transmitter.stop()


if __name__ == "__main__":
    main()
