import time

import numpy as np
from ex_wall_frame_transmitter.constants import WIDTH, HEIGHT
from ex_wall_frame_transmitter import FrameTransmitter
from decouple import config

off_frame = np.array([[(0, 0, 0) for _ in range(WIDTH)] for _ in range(HEIGHT)])

transmitter = FrameTransmitter(destination_uri=config("DESTINATION_URI"))
transmitter.start()

transmitter.send_numpy_frame(off_frame)
time.sleep(1)
transmitter.stop()
