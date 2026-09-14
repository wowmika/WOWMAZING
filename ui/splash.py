"""Branded launch splash for WOWMAZING."""

import customtkinter as ctk


class SplashScreen(ctk.CTkToplevel):
    def __init__(self, master) -> None:
        super().__init__(master)
        self.title("WOWMAZING")
        self.geometry("460x260")
        self.resizable(False, False)
        self.overrideredirect(True)
        self.attributes("-topmost", True)

        ctk.CTkLabel(
            self,
            text="WOWMAZING",
            font=("Segoe UI", 36, "bold"),
            text_color="#22C55E",
        ).pack(pady=(68, 8))
        ctk.CTkLabel(
            self,
            text="Your media. Your vibe.",
            font=("Segoe UI", 16),
        ).pack()
        ctk.CTkLabel(
            self,
            text="Loading your library…",
            font=("Segoe UI", 12),
            text_color="#C5C5C5",
        ).pack(pady=(28, 0))
