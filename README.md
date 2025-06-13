# 🧰 Nathan's Toggler

Nathan's Toggler is a friendly Windows utility that allows you to toggle quickly **Windows Defender**, control **internet access**, and manage folder-based firewall and Defender exclusions—all from a simple Python GUI.

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
- Remove unused imports or features to refine the code further.
- If a small file is crucial, distribute the `.py` script and required assets instead.

### 3. **(Optional) Batch & PowerShell Launchers**
- Included `.bat` and `.ps1` files to help with admin elevation and easy launching if preferred.

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

**Q: Is this safe?**
A: Yes. The source code is provided, utilizes open-source repositories, and is publicly available for review.

**Q: Will this tool harm my computer or files?**
A: No. The tool is designed to automate system tasks safely and only makes changes you explicitly request. All changes are documented and can be reversed.

**Q: Is my data private?**
A: Yes. The tool does not collect or transmit your personal data. All actions are performed locally on your machine.

**Q: Do I need to pay for this?**
A: No. This project is open-source and available for unrestricted use. You can donate to my PayPal if you would like. 

**Q: Can I suggest features or report bugs?**
A: Absolutely! Contributions, feedback, and issue reports are welcome. Please use the Issues section on GitHub.

**Q: What operating systems are supported?**
A: Currently, this tool is developed for Windows operating systems. Compatibility with other systems can be added through community updates.

**Q: How do I uninstall or remove changes made by the tool?**
A: You can reverse firewall and Defender exclusions from within the tool or manually remove rules via Windows settings. Detailed instructions are available in the documentation.

**Q: Who can I contact for help?**
A: For support, open an issue on GitHub or use the contact information in the repository.

**Q: How do I update to the latest version?**
A: Simply download the newest release from GitHub and follow the update instructions in the README.

---

## 📝 Attribution & About

**Nathan398** – Author, director, and proud father of three.  
See [my website](https://nathanvarner.wixsite.com/nvport) and [GitHub](https://github.com/Nathan398) for more.

---

## ⚠️ Disclaimer

- **Tamper Protection** must be off to disable Defender.
- **Admin rights** are required for most features.
- Use responsibly—this tool modifies security settings.
