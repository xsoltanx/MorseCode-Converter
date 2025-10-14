# Morse Code Converter

A beautiful and interactive desktop application for converting text to Morse code and vice versa, built with Python and Tkinter.


![Python](https://img.shields.io/badge/Python-3.6%252B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-white)


## ✨ Features

| Feature | Description |
|---------|-------------|
| 🔤  **Text to Morse Conversion** | Convert English text to International Morse Code |
| 📝  **Morse to Text Conversion** | Decode Morse code back to readable text |
| 🎵  **Audio Playback** | Hear your Morse code with beep sounds |
| 🌓  **Theme Switching** | Toggle between dark and light modes |
| 🌐  **Bilingual Interface** | Available in both English and Persian |
| 📋  **Copy to Clipboard** | Easily copy results with one click |
| 💫  **Smooth Animations** | Enjoy beautiful transitions and typing effects |
| ⚡  **Auto-Install Dependencies** | Automatic package installation on first run |

## 🚀 Quick Start

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)


### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/morse-code-converter.git
   cd morse-code-converter
   ```

2.   **Run the application**

```bash
python Morse_Code_Converter.py
```
The application will automatically install any required dependencies on first run!

## 🎯 Usage
**Text to Morse Code**
|Step | |
|-----|-------------------|
|1|Select "Text to Morse" from the main menu|
|2|Enter your English text in the input field|
|3|Click "Convert" to generate Morse code|
|4|Use "Play Sound" to hear the Morse code|
|5|Copy the result with the "Copy" button|

**Morse Code to Text**
|Step | |
|-----|-------------------|
|1|Select "Morse to Text" from the main menu|
|2|Enter Morse code using dots (`.`) and dashes (`-`)|
|3|Use space between letters and "`/`" between words|
|4|Click "Convert" to decode back to text|

### Morse Code Format
- **Letters:** Separated by single spaces
- **Words:** Separated by "`/`"
- **Example:** HELLO WORLD = `.... . .-.. .-.. --- / .-- --- .-. .-.. -..`


## 🛠️ Technical Details
#### **Built With**
- **Python** - Core programming language
- **Tkinter** - GUI framework
- **NumPy** - Audio signal processing
- **SimpleAudio** - Cross-platform audio playback
- **Winsound** - Windows audio support

#### **Supported Platforms**
- ✅ Windows

- ✅ Linux

- ✅ macOS

### Morse Code Dictionary

 **The application supports:**

- All English letters (A-Z)

- Numbers (0-9)

- Space character

## 📸 Screenshots

|*Main Menu | Text Conversion |	Morse Decoding* |
|-----------|-----------------|------------------|
|![Screenshot of a comment on a GitHub issue showing an image, added in the Markdown, of an Octocat smiling and raising a tentacle.]((https://github.com/xsoltanx/MorseCode-Converter/blob/main/assets/ScreenShots/Shot-1.png))|

### 🎨 Features in Detail
#### Smart Installation

- Automatic dependency checking
- Visual installation progress
- Error handling for failed installations

#### User Experience
- Animated text output
- Smooth theme transitions
- Input validation with visual feedback
- Persistent settings (language & theme)

#### Audio Implementation
- Windows: Uses built-in winsound module
- Other OS: Uses numpy and simpleaudio for cross-platform support
- Customizable frequency and duration settings

## 🔧 Customization
You can modify these constants in the code:

```python
unit = 150    # Duration unit in milliseconds
freq = 750    # Beep frequency in Hz
```

#### 🙏 Acknowledgments
- International Morse Code standards
- Python community for excellent libraries
- Contributors and testers



### 📝 License
**This project is licensed under the MIT License - see the [LICENSE](./main/LICENSE) file for details.**

###
**⭐ Star this repo if you find it helpful!**

Made with ❤️
