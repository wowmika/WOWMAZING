import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.home import HomePage
from ui.download import DownloadPage
from ui.library import LibraryPage
from ui.settings import SettingsPage


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class WOWMAZING(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("WOWMAZING")
        self.geometry("1400x800")

        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        self.content = ctk.CTkFrame(self, fg_color="transparent")
        self.content.pack(fill="both", expand=True)

        self.pages = {
            "home": HomePage(self.content),
            "download": DownloadPage(self.content),
            "library": LibraryPage(self.content),
            "settings": SettingsPage(self.content)
        }

        self.show_page("home")

        self.sidebar.set_callback(self.show_page)

    def show_page(self, name):

        for page in self.pages.values():
            page.pack_forget()

        self.pages[name].pack(fill="both", expand=True)


app = WOWMAZING()
app.mainloop()