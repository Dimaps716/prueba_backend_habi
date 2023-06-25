import os

from dotenv import load_dotenv

load_dotenv()


# > This class is used to store all the environment variables that are used in the application
class Settings:
    BASE_API_PREFIX = "/api"
    MACHINE = os.getenv("MACHINE")

    if MACHINE == "GCP":
        ROOT_PATH = BASE_API_PREFIX
    else:
        ROOT_PATH = ""
