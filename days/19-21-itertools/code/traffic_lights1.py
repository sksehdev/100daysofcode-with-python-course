import itertools
import time
import random

traffic_lights = itertools.cycle("green amber red".split())


def rotate_traffic_lights():
    for color in traffic_lights:
      if color == "amber":
          print("Ready to stop")
          time.sleep(3)
      if color == "red":
          print("Stop")
          time.sleep(random.randint(3,7))
      if color == "green":
          print("Go and keep going")
          time.sleep(random.randint(3,7))



rotate_traffic_lights()