# 🧰 Nathan's Toggler

Nathan's Toggler is a friendly Windows utility to quickly toggle **Windows Defender**, control **internet access**, and manage folder-based firewall & Defender exclusions—all from a simple Python GUI.

---

## 🚦 How to Use

### 1. **Run the Python Script**
- Requires [Python 3.8+](https://www.python.org/downloads/).
- Install required packages:
pip install pygame pillow playsound

- Run in terminal:
python Nathans_Toggler.py

### 2. **(Optional) Build Your Own EXE**

#### ⚠️ Why is the EXE so big?
- Python `.exe` files made with PyInstaller or similar tools **bundle the entire Python interpreter and all dependencies**. This is normal and can easily result in files **50–100+ MB**.
- The size is not a sign of malware or bloat—just how Python packaging works.

#### 💡 Reducing EXE Size
- Try the `--onefile` flag with PyInstaller:
pyinstaller --onefile --windowed --icon=icon3.ico Nathans_Toggler.py

- For advanced users, tools like **UPX** can compress executables, but savings are often modest.
- Remove unused imports or features to trim further.
- If a small file is crucial, distribute the `.py` script and required assets instead.

### 3. **(Optional) Batch & PowerShell Launchers**
- Included `.bat` and `.ps1` files help with admin elevation and easy launching if preferred.

---

## ⚡️ Quick Install

1. **Install Python:** [python.org](https://www.python.org/downloads/)
2. **Install dependencies:**
pip install pygame pillow playsound

3. **Get this repo:** Download ZIP or use
git clone https://github.com/Nathan398/nathans-toggler.git

4. **Run:**  
python Nathans_Toggler.py

---

## ⚙️ Features

- Toggle **Windows Defender** (Realtime Monitoring) on/off
- Toggle **Internet Adapter** on/off
- Block internet (inbound/outbound) for all `.exe` files in a folder
- Add folders to Windows Defender exclusions
- User-friendly Python GUI

---

## ℹ️ FAQ


**Q: Is this safe?**  
A: Yes. The source code is provided, utilizes open-source repositories, and is publicly available for review.

---

## 📝 Attribution & About

**Nathan398** – Author, director, and proud father of three.  
See [my website](https://nathanvarner.wixsite.com/nvport) and [GitHub](https://github.com/Nathan398) for more.

---

## ⚠️ Disclaimer

- **Tamper Protection** must be off to disable Defender.
- **Admin rights** are required for most features.
- Use responsibly—this tool modifies security settings.
