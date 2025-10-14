import importlib
import os
import platform
import subprocess
import sys
import time
import tkinter as tk
from tkinter import messagebox


# Function to check and install required packages
def install_required_packages():
    required_packages = {
        'numpy': 'numpy',
        'simpleaudio': 'simpleaudio',
        'winsound': 'winsound'  # winsound is part of standard library on Windows
    }
    
    missing_packages = []
    
    # Check which packages are missing
    for package_name, import_name in required_packages.items():
        try:
            importlib.import_module(import_name)
        except ImportError:
            missing_packages.append(package_name)
    
    # If there are missing packages, install them
    if missing_packages:
        # Create installation window
        install_window = tk.Toplevel()
        install_window.title("نصب کتابخانه‌ها")
        install_window.geometry("400x200")
        install_window.configure(bg="#222")
        
        # Add label to show installation progress
        tk.Label(install_window, text="در حال نصب کتابخانه‌های مورد نیاز...", 
                fg="white", bg="#222", font=("Arial", 12)).pack(pady=20)
        
        progress_label = tk.Label(install_window, text="", 
                                 fg="white", bg="#222", font=("Arial", 10))
        progress_label.pack(pady=10)
        
        # Create progress bar
        progress_bar = tk.Canvas(install_window, width=300, height=20, 
                                bg="#444", highlightthickness=0)
        progress_bar.pack(pady=10)
        
        install_window.update()
        
        # Install each missing package
        for i, package in enumerate(missing_packages):
            progress_label.config(text=f"در حال نصب {package}...")
            progress_bar.delete("progress")
            progress_bar.create_rectangle(0, 0, (i/len(missing_packages))*300, 20, 
                                        fill="#4caf50", outline="", tags="progress")
            install_window.update()
            
            try:
                # Use pip to install the package
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            except subprocess.CalledProcessError:
                # Show error message if installation fails
                messagebox.showerror("خطا", f"خطا در نصب {package}\nلطفاً دستی نصب کنید:\npip install {package}")
                install_window.destroy()
                return False
        
        # Show completion message
        progress_label.config(text="نصب کامل شد!")
        progress_bar.create_rectangle(0, 0, 300, 20, fill="#4caf50", outline="", tags="progress")
        install_window.update()
        time.sleep(1)
        install_window.destroy()
        
        messagebox.showinfo("موفق", "کتابخانه‌های مورد نیاز با موفقیت نصب شدند!")
    
    return True

# Check and install packages before proceeding
if not install_required_packages():
    sys.exit(1)

# Morse code dictionary mapping characters to Morse code
MORSE_CODE_DIC = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', ' ': '/'
}

# Reverse dictionary for Morse to text conversion
REVERSE_MORSE_CODE = {v: k for k, v in MORSE_CODE_DIC.items()}

# About text in Persian and English
ABOUT_TEXT_FA = """
📢 درباره برنامه:
این برنامه برای تبدیل متن به کد مورس و برعکس طراحی شده است. 
از آنجایی که کد مورس بین‌المللی برای زبان فارسی وجود ندارد، 
ما در این برنامه فقط زبان انگلیسی را پشتیبانی کرده‌ایم.

✨ راهنمای بخش‌ها:
- "متن به کد مورس": متن انگلیسی شما را به کد مورس تبدیل می‌کند.
- "کد مورس به متن": کد مورس را به متن انگلیسی تبدیل می‌کند.
- "پاک کردن": تمام ورودی و خروجی‌ها را خالی می‌کند.
- "کپی": خروجی را در کلیپ‌بورد شما قرار می‌دهد.
- "پخش صدا": کد مورس تولیدشده را با صدا (بوق کوتاه و بلند) پخش می‌کند.
- "تغییر تم": بین حالت تاریک و روشن جابه‌جا می‌شوید.
- "فارسی / English": زبان محیط برنامه را تغییر می‌دهد.

❓ نکته مهم:
در کد مورس ساخته‌شده توسط برنامه:
- فاصله (space) بین حروف با یک فاصله ساده " " مشخص می‌شود.
- فاصله بین کلمات با "/" نشان داده می‌شود.
این یعنی اگر در خروجی "/" دیدید، یعنی بین دو کلمه فاصله وجود دارد.

🎯 هدف این برنامه:
کمک به یادگیری کد مورس و تبدیل سریع متن و کد مورس به یکدیگر 
با محیطی زیبا و ساده.
"""

ABOUT_TEXT_EN = """
📢 About the Program:
This app is designed to convert text to Morse code and vice versa. 
Since there is no official international Morse code for Persian, 
we only included English support.

✨ Features:
- "Text to Morse": Converts English text into Morse code.
- "Morse to Text": Converts Morse code back to English text.
- "Clear": Clears both input and output fields.
- "Copy": Copies the output to your clipboard.
- "Play Sound": Plays the generated Morse code with short and long beeps.
- "Toggle Theme": Switch between dark and light mode.
- "فارسی / English": Switches the program's interface language.

❓ Important Note:
In the Morse code generated by the program:
- A single space " " separates letters.
- A "/" separates words.
So whenever you see "/", it means there is a space between two words.

🎯 Purpose:
To help you learn Morse code and easily convert text 
and Morse code in a clean and simple interface.
"""

# Language dictionary for UI text in Persian and English
LANGS = {
    "fa": {
        "menu_title": "انتخاب کنید:",
        "btn_text_to_morse": "متن به کد مورس",
        "btn_morse_to_text": "کد مورس به متن",
        "btn_back": "بازگشت به منو",
        "label_input_text": "ورود متن:",
        "label_input_morse": "ورود کد مورس:",
        "label_output_morse": "خروجی کد مورس:",
        "label_output_text": "خروجی متن:",
        "btn_convert": "تبدیل",
        "btn_clear": "پاک کردن",
        "btn_copy": "کپی",
        "btn_play": "پخش صدا",
        "msg_copied": " متن در کلیپ بورد کپی شد",
        "msg_warning_text": " لطفا متنی وارد کنید!",
        "msg_warning_morse": " لطفا کد مورس وارد کنید!",
        "msg_already_empty": " فیلدها از قبل خالی هستند!",
        "msg_nothing_to_copy": " چیزی برای کپی کردن وجود ندارد!",
        "msg_no_morse": " خروجی مورس برای پخش وجود ندارد!",
        "lang_menu": "زبان",
        "btn_dark_mode": "تغییر تم",
        "btn_about": "راهنما"
    },
    "en": {
        "menu_title": "Choose an option:",
        "btn_text_to_morse": "Text to Morse",
        "btn_morse_to_text": "Morse to Text",
        "btn_back": "Back to Menu",
        "label_input_text": "Enter Text:",
        "label_input_morse": "Enter Morse Code:",
        "label_output_morse": "Morse Code Output:",
        "label_output_text": "Text Output:",
        "btn_convert": "Convert",
        "btn_clear": "Clear",
        "btn_copy": "Copy",
        "btn_play": "Play Sound",
        "msg_copied": "Text copied to clipboard!",
        "msg_warning_text": "Please enter some text!",
        "msg_warning_morse": "Please enter Morse code!",
        "msg_already_empty": "Fields are already empty!",
        "msg_nothing_to_copy": "Nothing to copy!",
        "msg_no_morse": "No Morse code to play!",
        "lang_menu": "Language",
        "btn_dark_mode": "Toggle Theme",
        "btn_about": "About"
    }
}

# Settings file to store user preferences
SETTINGS_FILE = "settings.txt"
current_lang = "fa"  # Default language
current_theme = "dark"  # Default theme

# Theme colors for dark and light modes
THEMES = {
    "dark": {"bg": "#222", "fg": "white", "entry_bg": "#333", "entry_fg": "white"},
    "light": {"bg": "#f4f4f4", "fg": "black", "entry_bg": "white", "entry_fg": "black"}
}

# Load user settings from file
def load_settings():
    global current_lang, current_theme
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            data = f.read().splitlines()
            if len(data) >= 2:
                current_lang = data[0].strip()
                current_theme = data[1].strip()

# Save user settings to file
def save_settings():
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        f.write(current_lang + "\n")
        f.write(current_theme + "\n")

# Convert text to Morse code
def text_to_morse(text):
    return ' '.join(MORSE_CODE_DIC.get(char, '?') for char in text.upper())

# Convert Morse code to text
def morse_to_text(morse):
    return ''.join(REVERSE_MORSE_CODE.get(code, '?') for code in morse.split(' '))

# Animate text output character by character
def animate_output(text, widget, delay=50):
    widget.delete("1.0", tk.END)

    def insert_char(i=0):
        if i < len(text):
            widget.insert(tk.END, text[i])
            widget.see(tk.END)
            widget.after(delay, insert_char, i + 1)
    insert_char()

# Convert text to Morse code and display result
def convert_text_to_morse():
    input_text = entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", LANGS[current_lang]["msg_warning_text"])
        entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
        return
    entry.config(highlightthickness=0)
    result = text_to_morse(input_text)
    animate_output(result, output, delay=80)

# Convert Morse code to text and display result
def convert_morse_to_text():
    input_text = entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showerror("Error", LANGS[current_lang]["msg_warning_morse"])
        entry.config(highlightbackground="red", highlightcolor="red", highlightthickness=2)
        return
    entry.config(highlightthickness=0)
    result = morse_to_text(input_text)
    animate_output(result, output, delay=80)

# Clear input and output fields
def clear():
    if not entry.get("1.0", tk.END).strip() and not output.get("1.0", tk.END).strip():
        messagebox.showerror("Error", LANGS[current_lang]["msg_already_empty"])
        return
    entry.delete("1.0", tk.END)
    output.delete("1.0", tk.END)
    entry.config(highlightthickness=0)

# Copy output to clipboard
def copy_to_clipboard():
    text = output.get("1.0", tk.END).strip()
    if not text:
        messagebox.showerror("Error", LANGS[current_lang]["msg_nothing_to_copy"])
        return
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied!", LANGS[current_lang]["msg_copied"])

# Play Morse code as sound
def play_morse_sound():
    morse_code = output.get("1.0", tk.END).strip()
    if not morse_code:
        messagebox.showerror("Error", LANGS[current_lang]["msg_no_morse"])
        return

    unit, freq = 150, 750  # Duration and frequency settings
    
    # Windows implementation using winsound
    if platform.system() == "Windows":
        import winsound
        for symbol in morse_code:
            if symbol == '.':
                winsound.Beep(freq, unit)
            elif symbol == '-':
                winsound.Beep(freq, unit * 3)
            elif symbol == ' ':
                time.sleep(unit / 1000 * 2)
            elif symbol == '/':
                time.sleep(unit / 1000 * 4)
            time.sleep(unit / 1000)
    # Other platforms implementation using numpy and simpleaudio
    else:
        import numpy as np
        import simpleaudio as sa

        def beep(duration):
            t = np.linspace(0, duration / 1000, int(44100 * duration / 1000), False)
            tone = np.sin(freq * t * 2 * np.pi) * 0.3
            audio = (tone * (2**15 - 1)).astype(np.int16)
            play_obj = sa.play_buffer(audio, 1, 2, 44100)
            play_obj.wait_done()

        for symbol in morse_code:
            if symbol == '.':
                beep(unit)
            elif symbol == '-':
                beep(unit * 3)
            elif symbol == ' ':
                time.sleep(unit / 1000 * 2)
            elif symbol == '/':
                time.sleep(unit / 1000 * 4)
            time.sleep(unit / 1000)

# Display about information
def open_about():
    about_text = ABOUT_TEXT_FA if current_lang == "fa" else ABOUT_TEXT_EN
    colors = THEMES[current_theme]

    about_win = tk.Toplevel(root)
    about_win.title(LANGS[current_lang]["btn_about"])
    about_win.geometry("600x500")
    about_win.config(bg=colors["bg"])

    text_widget = tk.Text(
        about_win, wrap=tk.WORD, font=("Arial", 11),
        bg=colors["entry_bg"], fg=colors["entry_fg"]
    )
    text_widget.pack(expand=True, fill="both", padx=10, pady=10)
    text_widget.insert("1.0", about_text)
    text_widget.config(state=tk.DISABLED)

# Display main menu
def open_menu():
    for widget in root.winfo_children():
        widget.destroy()
    colors = THEMES[current_theme]

    tk.Label(
        root, text=LANGS[current_lang]["menu_title"],
        fg=colors["fg"], bg=colors["bg"], font=("Arial", 14)
    ).pack(pady=20)

    tk.Button(root, text=LANGS[current_lang]["btn_text_to_morse"],
              command=open_text_to_morse, bg="#4caf50", fg="white",
              width=20, height=2).pack(pady=10)

    tk.Button(root, text=LANGS[current_lang]["btn_morse_to_text"],
              command=open_morse_to_text, bg="#2196F3", fg="white",
              width=20, height=2).pack(pady=10)

    tk.Button(root, text="فارسی / English",
              command=toggle_language, bg="#777", fg="white",
              width=20, height=2).pack(pady=10)

    tk.Button(root, text=LANGS[current_lang]["btn_dark_mode"],
              command=toggle_theme, bg="#555", fg="white",
              width=20, height=2).pack(pady=10)

    tk.Button(root, text=LANGS[current_lang]["btn_about"],
              command=open_about, bg="#9C27B0", fg="white",
              width=20, height=2).pack(pady=10)

# Open text to Morse converter screen
def open_text_to_morse():
    build_converter_screen(
        LANGS[current_lang]["label_input_text"],
        convert_text_to_morse,
        LANGS[current_lang]["label_output_morse"],
        with_sound=True
    )

# Open Morse to text converter screen
def open_morse_to_text():
    build_converter_screen(
        LANGS[current_lang]["label_input_morse"],
        convert_morse_to_text,
        LANGS[current_lang]["label_output_text"],
        with_sound=False
    )

# Build converter screen with appropriate labels and buttons
def build_converter_screen(input_label, convert_command, output_label, with_sound=False):
    for widget in root.winfo_children():
        widget.destroy()
    colors = THEMES[current_theme]

    tk.Label(root, text=input_label, fg=colors["fg"],
             bg=colors["bg"], font=("Arial", 12)).pack(pady=5)

    global entry
    entry = tk.Text(root, height=5, width=50, font=("Arial", 12),
                    highlightthickness=0, bg=colors["entry_bg"],
                    fg=colors["entry_fg"])
    entry.pack(pady=5)

    frame = tk.Frame(root, bg=colors["bg"])
    frame.pack(pady=10)

    tk.Button(frame, text=LANGS[current_lang]["btn_convert"],
              command=convert_command, bg="#4caf50", fg="white",
              width=12).grid(row=0, column=0, padx=5)

    tk.Button(frame, text=LANGS[current_lang]["btn_clear"],
              command=clear, bg="#f44336", fg="white",
              width=12).grid(row=0, column=1, padx=5)

    tk.Button(frame, text=LANGS[current_lang]["btn_copy"],
              command=copy_to_clipboard, bg="#2196F3", fg="white",
              width=12).grid(row=0, column=2, padx=5)

    if with_sound:
        tk.Button(frame, text=LANGS[current_lang]["btn_play"],
                  command=play_morse_sound, bg="#9C27B0", fg="white",
                  width=12).grid(row=0, column=3, padx=5)

    tk.Label(root, text=output_label, fg=colors["fg"],
             bg=colors["bg"], font=("Arial", 12)).pack(pady=5)

    global output
    output = tk.Text(root, height=6, width=50, font=("Consolas", 12),
                     bg=colors["entry_bg"], fg=colors["entry_fg"])
    output.pack(pady=5)

    tk.Button(root, text=LANGS[current_lang]["btn_back"],
              command=open_menu, bg="#777", fg="white",
              width=15).pack(pady=10)

# Toggle between Persian and English
def toggle_language():
    global current_lang
    current_lang = "en" if current_lang == "fa" else "fa"
    save_settings()
    open_menu()

# Generate intermediate colors for smooth theme transition
def fade_color(start, end, steps=20):
    start_rgb = root.winfo_rgb(start)
    end_rgb = root.winfo_rgb(end)
    for i in range(steps + 1):
        r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / steps)
        g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / steps)
        b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / steps)
        yield f"#{r // 256:02x}{g // 256:02x}{b // 256:02x}"

# Toggle between dark and light themes with animation
def toggle_theme():
    global current_theme
    new_theme = "light" if current_theme == "dark" else "dark"
    start_bg = THEMES[current_theme]["bg"]
    end_bg = THEMES[new_theme]["bg"]

    def step(colors):
        try:
            color = next(colors)
            root.config(bg=color)
            root.after(30, step, colors)
        except StopIteration:
            global current_theme
            current_theme = new_theme
            save_settings()
            open_menu()

    step(fade_color(start_bg, end_bg))

# Load settings and initialize application
load_settings()
root = tk.Tk()
root.title("Morse Code Converter")
root.geometry("600x500")
root.config(bg=THEMES[current_theme]["bg"])
root.resizable(False, False)

# Try to load application icon
try:
    icon_image = tk.PhotoImage(file="morse.png")
    root.iconphoto(True, icon_image)
except:
    pass

# Start with main menu
open_menu()
root.mainloop()