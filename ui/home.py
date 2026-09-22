import customtkinter as ctk
from core.theme import *

class HomePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        label = ctk.CTkLabel(
    self,
    text="🏠 Home",
    font=("Segoe UI", 30, "bold"),
    text_color=TEXT
)

        label.pack(pady=40)