# 🧰 Nathan's Toggler

A powerful, beginner-friendly Windows GUI tool to toggle **Windows Defender**, **Internet access**, and now includes advanced **folder-based firewall and Defender exclusion management** — all in one place.

---

## ⚙️ Features

- ✅ Toggle **Windows Defender (Realtime Monitoring)** On/Off  
- 🌐 Toggle **Internet Adapter** On/Off  
- 🧠 **Remembers your adapter name** across sessions  
- 🔐 **Auto-elevates** to Admin when needed  
- 📁 Block **internet access (inbound & outbound)** for all `.exe` files in a selected folder  
- 🛡️ Add folders to **Windows Defender exclusions**, including:
  - Exclusion paths  
  - Controlled folder access  
  - Threat/real-time process exceptions  
- 🖼️ Easy-to-use **Python `tkinter` GUI**

---

## 🚀 Setup

1. **Install Python**  
   Download from [python.org](https://www.python.org/downloads/)  
   ✅ Be sure to check **“Add Python to PATH”** during installation.

2. **Download or Clone the Repo**

   ```bash
   git clone https://github.com/Nathan398/nathans-toggler.git
   cd nathans-toggler
   ```

   Or download the script files manually.

3. **Run the Script**

   - You'll be prompted to run as **Administrator** automatically.  
   - Your **network adapter name** is requested only once and saved for future runs.

---

## 🔧 Folder-Based Tools

### ✅ Block Internet for Folder

- Blocks **inbound & outbound connections** for all `.exe` files in the selected folder.  
- Uses `netsh advfirewall` to create rules.

### 🛡️ Allow Folder in Windows Defender

- Adds folder to:
  - `ExclusionPath`  
  - `ControlledFolderAccessAllowedApplications`  
  - `ExclusionProcess`  

---

## 📜 Attribution / About

**Nathan398**  
Author, comedian, writer, director, editor, ninja, philanthropist, and proud father of three.  
_Call me whatever you want — just not late for dinner._

Annoying Orange parody account.  
💡 Please help me do my laundry. There are too many options on the knob and I don’t want to mess anything up. It’s been weeks now.

---

## 🔗 Socials & Links

- 🌐 [Website](https://nathanvarner.wixsite.com/nvport)  
- 🐙 [GitHub](https://github.com/Nathan398)  
- 📹 [YouTube](https://www.youtube.com/c/NathanVarner1)  
- 📸 [Instagram](https://www.instagram.com/nathanvarner27)  
- 🐦 [Twitter/X](https://twitter.com/NathanVarner)  
- 💼 [LinkedIn](https://www.linkedin.com/in/nathanvarner)

---

## ⚠️ Notes & Disclaimers

- **Tamper Protection** must be disabled in Windows Defender to allow Defender toggling.
- **Admin access is required** for firewall and Defender exclusion features.
- This tool is for **educational and convenience purposes only**.  
  ⚠️ Use responsibly.
