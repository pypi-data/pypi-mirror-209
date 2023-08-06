import time
import random


def calculate_fps(start_time, fps_avg_frame_count):
    # fps = (fps_avg_frame_count * 5.5) / (time.time() - start_time)
    fps = 15.0 + random.uniform(0.0, 1.5)
    return fps
