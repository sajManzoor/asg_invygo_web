import os


class SeleniumConfig:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the directory of this config file
    PROJECT_DIR = os.path.dirname(BASE_DIR)
    CHROME_DRIVER_PATH = os.path.join(BASE_DIR, 'drivers', 'chromedriver')
    BASE_URL = "https://www.invygo.com/en-ae"
