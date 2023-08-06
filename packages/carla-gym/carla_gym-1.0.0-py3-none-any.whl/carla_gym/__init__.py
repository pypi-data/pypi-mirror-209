"""Import all the necessary modules for the Multi Actor Carla package."""
import logging
import os
import sys
from carla_gym.multi_env import (env, parallel_env)
from carla_gym.core.constants import DEFAULT_MULTIENV_CONFIG

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
LOG_DIR = os.path.join(os.getcwd(), "logs")
if not os.path.isdir(LOG_DIR):
    os.mkdir(LOG_DIR)

__version__ = "1.0.0"

# Init and setup the root logger
logging.basicConfig(filename=LOG_DIR + "/carla-gym.log", level=logging.DEBUG)

# Fix path issues with included CARLA API
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "carla/PythonAPI"))
