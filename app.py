import customtkinter as ctk

from ui.sidebar import Sidebar
from ui.home import HomePage
from ui.download import DownloadPage
from ui.library import LibraryPage
from ui.mini_player import MiniPlayer
from ui.settings import SettingsPage
from ui.splash import SplashScreen
from core.settings import AppSettings, SettingsStore


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class WOWMAZING(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.settings_store = SettingsStore()
        ctk.set_appearance_mode(self.settings_store.settings.theme.lower())
        self.title("WOWMAZING")
        self.geometry("1400x800")
        self.withdraw()

        self.sidebar = Sidebar(self)
        self.sidebar.pack(side="left", fill="y")

        self.main_area = ctk.CTkFrame(self, fg_color="transparent")
        self.main_area.pack(side="left", fill="both", expand=True)

        self.content = ctk.CTkFrame(self.main_area, fg_color="transparent")
        self.content.pack(fill="both", expand=True)

        self.pages = {
            "home": HomePage(self.content),
            "library": LibraryPage(self.content),
            "settings": SettingsPage(
                self.content,
                self.settings_store,
                self.apply_settings,
            )
        }
        self.pages["download"] = DownloadPage(
            self.content,
            on_download_completed=self.pages["library"].load_files,
        )
        self.mini_player = MiniPlayer(self.main_area, self.pages["library"])
        self.mini_player.pack(side="bottom", fill="x")

        self.show_page(self.settings_store.settings.startup_page)

        self.sidebar.set_callback(self.show_page)
        self.splash = SplashScreen(self)
        self.after(2000, self.finish_launch)

    def show_page(self, name):

        for page in self.pages.values():
            page.pack_forget()

        self.pages[name].pack(fill="both", expand=True)

    def apply_settings(self, settings: AppSettings):

        ctk.set_appearance_mode(settings.theme.lower())

    def finish_launch(self):

        if self.splash.winfo_exists():
            self.splash.destroy()
        self.deiconify()


app = WOWMAZING()
app.mainloop()
