# 🧰 Nathan's Toggler

Nathan's Toggler is a powerful, beginner-friendly Windows tool that lets you toggle **Windows Defender**, control **internet access**, and manage **folder-based firewall & Defender exclusions**—all with an intuitive Python `tkinter` GUI.

Easily block internet for selected folders, add exclusions to Windows Defender, and more. Ideal for anyone who wants simple, unified control over common Windows security settings.

---

## 🚦 How to Run

You have multiple options:

### 1. **Run the Prebuilt EXE (No Python Needed)**
- Download `Nathans_Toggler.exe` from the [Releases](https://github.com/Nathan398/nathans-toggler/releases) page (if provided).
- Double-click the EXE.
- **No Python or extra installs needed.**  
  The EXE auto-prompts for administrator access when required.

### 2. **Run the Python Script Directly**
- Make sure Python and required packages are installed (see Quick Install below).
- Double-click `Nathans_Toggler.py`, **or** run in terminal:
python Nathans_Toggler.py

markdown
Copy
Edit
- You’ll be prompted for administrator access as needed.

### 3. **Compile Your Own Executable**
- Advanced users can use [PyInstaller](https://pyinstaller.org/) to bundle everything into a standalone `.exe`.
- See [Setup: Compiling to EXE](#compiling-to-exe) below for step-by-step instructions.

### 4. **(Optional) Run from Batch or PowerShell Launcher**
- Use `launch_toggler.bat` or `launch_toggler.ps1` for hybrid compatibility or auto-elevation.

---

## ⚡️ Quick Install

If you just want to run the Python script, follow these steps:

1. **Install Python (3.8 or newer):**  
 Download from [python.org](https://www.python.org/downloads/).  
 _Be sure to check “Add Python to PATH” during installation!_

2. **Install required Python packages:**  
 Open Command Prompt or PowerShell and run:
pip install pygame pillow playsound

markdown
Copy
Edit

3. **Get the program files:**  
- Download this repo as a ZIP and extract it,  
  **OR** clone with Git:
  ```
  git clone https://github.com/Nathan398/nathans-toggler.git
  cd nathans-toggler
  ```

4. **Run the program:**  
python Nathans_Toggler.py

yaml
Copy
Edit
_Or double-click the `.py` file if Python is associated with `.py` scripts._

---

## 🔧 Setup (Full Details & Advanced Usage)

### Compiling to EXE

1. **Install PyInstaller:**  
pip install pyinstaller

markdown
Copy
Edit

2. **Build the executable:**  
From your project folder, run:
pyinstaller --onefile --windowed --icon=icon3.ico Nathans_Toggler.py

markdown
Copy
Edit
- This creates a `dist/Nathans_Toggler.exe` file.
- Copy over any needed resources (`music.mp3`, `gifman.jpg`, etc.) to the EXE’s directory.

3. **Run the EXE:**  
Double-click the `.exe` in the `dist` folder.

### Running from Batch or PowerShell

- Use `launch_toggler.bat` (double-click) or `launch_toggler.ps1` (right-click → Run with PowerShell) for automated launching and admin elevation.
- Great for users who want to avoid the terminal or want compatibility scripts.

### Other Requirements & Tips

- **Admin rights:** Most features (firewall, Defender changes) require administrator access.
- **First Run:** You’ll be asked for your network adapter name (e.g., `Wi-Fi` or `Ethernet`). This is saved for future use.
- **Windows only:** This app is designed for Windows 10/11.

---

## ⚙️ Features

- ✅ Toggle **Windows Defender** (Realtime Monitoring) on/off
- 🌐 Toggle **Internet Adapter** on/off
- 📁 Block internet (inbound/outbound) for all `.exe` files in a selected folder
- 🛡️ Add folders to Windows Defender exclusions
- 🧠 Remembers your adapter name across sessions
- 🖼️ Modern, easy-to-use interface (Python `tkinter`)
- 🔐 Auto-elevates to admin when needed

---

## 📜 Attribution / About

**Nathan398**  
Author, comedian, writer, director, editor, ninja, philanthropist, and proud father of three.  
_Call me whatever you want—just not late for dinner._

> Please help me do my laundry. There are too many options on the knob. It's been weeks.

---

## 🔗 Socials

- 🌐 [Website](https://nathanvarner.wixsite.com/nvport)
- 🐙 [GitHub](https://github.com/Nathan398)
- 📹 [YouTube](https://www.youtube.com/c/NathanVarner1)
- 📸 [Instagram](https://www.instagram.com/nathanvarner27/)
- 🐦 [Twitter/X](https://twitter.com/NathanVarner)
- 💼 [LinkedIn](https://www.linkedin.com/in/nathanvarner)

---

## 🎵 Music Credit

**BIOS Music 2.21 (Sega CD Model 2)**  
Composed by Spencer Nilsen, 1993  
[YouTube Link](https://youtu.be/HaQ_DSg6xhs?list=RDHaQ_DSg6xhs)

---

## ⚠️ Disclaimer

- **Tamper Protection** must be disabled in Windows Defender for Defender toggling.
- **Admin rights required** for firewall and Defender exclusion features.
- For educational and convenience purposes only.  
⚠️ Use responsibly!
