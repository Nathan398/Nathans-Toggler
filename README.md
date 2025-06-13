
# 🧰 Nathan's Toggler

A powerful, beginner-friendly Windows tool to toggle **Windows Defender**, **Internet access**, and manage **folder-based firewall & Defender exclusions**—all with an intuitive Python `tkinter` GUI.

---

## ⚙️ Features

- ✅ Toggle **Windows Defender (Realtime Monitoring)** on/off  
- 🌐 Toggle **Internet Adapter** on/off  
- 🧠 Remembers your adapter name across sessions  
- 🔐 Auto-elevates to admin when needed  
- 📁 Block internet (inbound & outbound) for all `.exe` files in a folder  
- 🛡️ Add folders to **Windows Defender exclusions**, including:
    - Exclusion paths  
    - Controlled folder access  
    - Threat/real-time process exceptions  
- 🖼️ Modern, easy-to-use interface

---

---

## ⚡️ Quick Install

1. **Install Python (3.8 or newer):**  
   Download from [python.org](https://www.python.org/downloads/).  
   _Make sure to check “Add Python to PATH” during installation!_

2. **Install required Python packages:**  
   Open a Command Prompt or PowerShell window and run:
pip install pygame pillow playsound

3. **Get the program files:**  
- Download this repository as a ZIP and extract it,  
  **OR** clone with Git:
  ```
  git clone https://github.com/Nathan398/nathans-toggler.git
  cd nathans-toggler
  ```

4. **Run the program:**  
Double-click `Nathans_Toggler.py`  
_Or_ run from terminal:
python Nathans_Toggler.py

**Note:**  
- The app will prompt for administrator access when needed.  
- Your adapter name is only asked for once and remembered for future sessions.
- If you want to compile to an `.exe`, see the section “Compiling to EXE” below (if you want to add that).

---

## 🚀 Setup

1. **Install Python:**  
   Get it from [python.org](https://www.python.org/downloads/).  
   ☑️ Be sure to check “Add Python to PATH” during installation.

2. **Clone or Download the Repo:**
   ```bash
   git clone https://github.com/Nathan398/nathans-toggler.git
   cd nathans-toggler
   ```
   Or download and unzip manually.

3. **Run the Script:**  
   - Auto-prompts for administrator rights as needed.  
   - Will ask for your network adapter name once (saved for future runs).

---

## 🔧 Folder-Based Tools

- **Block Internet for Folder:**  
  Blocks inbound & outbound network access for all `.exe` files using Windows Firewall.

- **Allow Folder in Defender:**  
  Adds a folder to Windows Defender exclusions (covers ExclusionPath, ControlledFolderAccessAllowedApplications, and ExclusionProcess).

---

## 🔗 Socials

- 🌐 [Website](https://nathanvarner.wixsite.com/nvport)  
- 📹 [YouTube](https://www.youtube.com/c/NathanVarner1)  
- 📸 [Instagram](https://www.instagram.com/nathanvarner27/)  
- 🐦 [Twitter/X](https://twitter.com/NathanVarner)  
- 💼 [LinkedIn](https://www.linkedin.com/in/nathanvarner)

---

## ⚠️ Disclaimer

- **Tamper Protection** must be disabled in Windows Defender for Defender toggling.
- **Admin rights required** for firewall and Defender exclusion features.
- For educational and convenience purposes only.  
  ⚠️ Use responsibly!
