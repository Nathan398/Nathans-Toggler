
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
