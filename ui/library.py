import customtkinter as ctk


class LibraryPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title=ctk.CTkLabel(
            self,
            text="🎵 Library",
            font=("Segoe UI",30,"bold")
        )

        title.pack(pady=40)