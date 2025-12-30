import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL_TEXT = "gemini-3-flash-preview"
MODEL_IMAGE = "gemini-3-pro-image-preview"

PATHS = {
    "data": "./data",
    "knowledge": "./knowledge",
    "output": "./output"
}

IMAGE_CONFIG = {
    "aspect_ratio": "16:9",
    "resolution": "2K"
}
