import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, font
import os
import sys
if getattr(sys, 'frozen', False):
    # If the application is run as a bundle/compiled executable
    base_path = sys._MEIPASS
else:
    # If the script is run as a standard Python script
    base_path = ''

icon_path = os.getenv('PATH_FOR_PY_LAB6')

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")
        self.root.geometry("400x300")
        self.file_path = None
        self.current_font_size = 12
        self.min_font_size = 8
        self.max_font_size = 20

        self.create_main_menu()

    def create_main_menu(self):
        self.clear_widgets()

        # Main Menu Buttons
        btn_open = tk.Button(self.root, text="Open file", command=self.open_file, bg="orange", height=3, width=25)
        btn_open.pack(pady=10)

        btn_edit = tk.Button(self.root, text="Edit file", command=self.edit_file, bg="orange", height=3, width=25)
        btn_edit.pack(pady=10)

        # btn_save = tk.Button(self.root, text="Save file", command=self.save_file, bg="orange", height=3, width=25)
        # btn_save.pack(pady=10)

        btn_exit = tk.Button(self.root, text="Exit", command=self.exit_app, bg="firebrick", height=3, width=25)
        btn_exit.pack(pady=10)
        
        btn_tasks = tk.Button(self.root, text="Tasks", command=self.open_tasks, bg="orange", height=2, width=10)
        btn_tasks.pack(side=tk.LEFT, anchor='sw', padx=10, pady=10)
        
    def open_tasks(self):
        # Open Task1 Window
        task1_window = tk.Toplevel(self.root)
        task1_window.title("Task 1")
        task1_window.geometry("400x200")
        tk.Label(task1_window, text="1. Створіть простий текстовий редактор з GUI, який дозволяє користувачам відкривати, редагувати та зберігати тексти у текстовому форматі.", wraplength=350).pack(pady=20)
        tk.Button(task1_window, text="Close", command=task1_window.destroy).pack(pady=10)

        # Open Task2 Window
        task2_window = tk.Toplevel(self.root)
        task2_window.title("Task 2")
        task2_window.geometry("400x200")
        tk.Label(task2_window, text="2. Додайте функціонал для відкриття і збереження файлів.", wraplength=350).pack(pady=20)
        tk.Button(task2_window, text="Close", command=task2_window.destroy).pack(pady=10)

    def open_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if self.file_path:
            file_name = os.path.basename(self.file_path)
            messagebox.showinfo("File opened", f"File opened: {file_name}")

    def edit_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file opened to edit")
            return
        
        self.root.geometry("800x600")
        self.clear_widgets()

        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, undo=True, font=("Helvetica", self.current_font_size))
        self.text_area.pack(expand=1, fill='both')

        with open(self.file_path, 'r') as file:
            self.text_area.insert(tk.INSERT, file.read())

        # Text Formatting Buttons
        frame = tk.Frame(self.root)
        frame.pack()

        btn_bold = tk.Button(frame, text="Bold", command=self.bold_text, bg="orange")
        btn_bold.pack(side=tk.LEFT)

        btn_underline = tk.Button(frame, text="Underline", command=self.underline_text, bg="orange")
        btn_underline.pack(side=tk.LEFT)

        btn_italic = tk.Button(frame, text="Italic", command=self.italic_text, bg="orange")
        btn_italic.pack(side=tk.LEFT)

        btn_increase_font = tk.Button(frame, text="Increase Font", command=self.increase_font, bg="orange")
        btn_increase_font.pack(side=tk.LEFT)

        btn_decrease_font = tk.Button(frame, text="Decrease Font", command=self.decrease_font, bg="orange")
        btn_decrease_font.pack(side=tk.LEFT)

        btn_undo = tk.Button(frame, text="Undo", command=self.text_area.edit_undo, bg="orange")
        btn_undo.pack(side=tk.LEFT)

        btn_redo = tk.Button(frame, text="Redo", command=self.text_area.edit_redo, bg="orange")
        btn_redo.pack(side=tk.LEFT)

        btn_save_edit = tk.Button(frame, text="Save", command=self.save_edited_file, bg="orange")
        btn_save_edit.pack(side=tk.LEFT)

    def save_edited_file(self):
        if not self.file_path:
            messagebox.showerror("Error", "No file opened to save")
            return

        try:
            text_content = self.text_area.get(1.0, tk.END)
            with open(self.file_path, 'w') as file:
                file.write(text_content)
            messagebox.showinfo("Editing saved", "Editing saved!")
            self.root.geometry("400x300")
            self.create_main_menu()
        except Exception as e:
            messagebox.showerror("Editing not saved", f"Editing not saved! Error: {e}")

    def save_file(self):
        pass

    def bold_text(self):
        try:
            current_font = font.Font(self.text_area, self.text_area.cget("font"))
            current_font.configure(weight="bold")
            self.text_area.tag_configure("bold", font=current_font)
            self.text_area.tag_add("bold", "sel.first", "sel.last")
        except tk.TclError:
            pass

    def underline_text(self):
        try:
            current_font = font.Font(self.text_area, self.text_area.cget("font"))
            current_font.configure(underline=True)
            self.text_area.tag_configure("underline", font=current_font)
            self.text_area.tag_add("underline", "sel.first", "sel.last")
        except tk.TclError:
            pass

    def italic_text(self):
        try:
            current_font = font.Font(self.text_area, self.text_area.cget("font"))
            current_font.configure(slant="italic")
            self.text_area.tag_configure("italic", font=current_font)
            self.text_area.tag_add("italic", "sel.first", "sel.last")
        except tk.TclError:
            pass

    def increase_font(self):
        if self.current_font_size < self.max_font_size:
            self.current_font_size += 2
            self.text_area.config(font=("Helvetica", self.current_font_size))

    def decrease_font(self):
        if self.current_font_size > self.min_font_size:
            self.current_font_size -= 2
            self.text_area.config(font=("Helvetica", self.current_font_size))

    def exit_app(self):
        self.root.quit()

    def clear_widgets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()
