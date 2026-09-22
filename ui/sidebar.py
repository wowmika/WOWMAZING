import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master,width=220)

        self.pack_propagate(False)

        self.callback=None

        title=ctk.CTkLabel(
            self,
            text="WOWMAZING",
            font=("Segoe UI",24,"bold")
        )

        title.pack(pady=30)

        self.make_button("🏠 Home","home")
        self.make_button("⬇ Download","download")
        self.make_button("🎵 Library","library")
        self.make_button("⚙ Settings","settings")

    def set_callback(self,callback):

        self.callback=callback

    def make_button(self,text,page):

        btn=ctk.CTkButton(
            self,
            text=text,
            height=45,
            command=lambda:self.callback(page)
        )

        btn.pack(fill="x",padx=20,pady=8)