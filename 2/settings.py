import os

from customtkinter import CTkImage
from PIL import Image


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
explorer_image = CTkImage(light_image=Image.open(f"{BASE_DIR}/images/explorer.png"), size=(25, 25))
