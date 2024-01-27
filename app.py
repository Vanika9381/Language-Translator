import tkinter as tk
from googletrans import Translator
import pyperclip

class LanguageTranslatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Translator")
        self.geometry("400x400")
        self.configure(bg="#F0F0F0")

        self.translated_text_for_copy = ""

        self.create_widgets()

    def create_widgets(self):
        input_label = tk.Label(self, text="Enter text to translate:", font=("Helvetica", 12), bg="#F0F0F0")
        input_label.pack(pady=(20, 5))

        self.input_entry = tk.Entry(self, width=40, font=("Helvetica", 12))
        self.input_entry.pack()

        target_label = tk.Label(self, text="Enter the target language (e.g., 'fr' for French):", font=("Helvetica", 12), bg="#F0F0F0")
        target_label.pack(pady=(10, 5))

        self.target_entry = tk.Entry(self, width=10, font=("Helvetica", 12))
        self.target_entry.pack()

        translate_button = tk.Button(self, text="Translate", command=self.translate_text, bg="#4CAF50", fg="white", font=("Helvetica", 12))
        translate_button.pack(pady=(20, 10))

        copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_translated_text, bg="#008CBA", fg="white", font=("Helvetica", 12))
        copy_button.pack(pady=(0, 20))

        self.translated_text_label = tk.Label(self, text="", font=("Helvetica", 14), wraplength=400, bg="#F0F0F0")
        self.translated_text_label.pack()

        self.copy_status_label = tk.Label(self, text="", font=("Helvetica", 12), fg="green", bg="#F0F0F0")
        self.copy_status_label.pack()

    def translate_text(self):
        input_text = self.input_entry.get()
        target_language = self.target_entry.get()

        translator = Translator()
        translated_text = translator.translate(input_text, dest=target_language)

        self.translated_text_label.config(text="Translated text: " + translated_text.text)
        self.translated_text_for_copy = translated_text.text

    def copy_translated_text(self):
        self.copy_to_clipboard(self.translated_text_for_copy)
        self.copy_status_label.config(text="Text copied to clipboard")

    @staticmethod
    def copy_to_clipboard(text):
        pyperclip.copy(text)

if __name__ == "__main__":
    app = LanguageTranslatorApp()
    app.mainloop()
