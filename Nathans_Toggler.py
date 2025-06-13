import ctypes
import subprocess
import pygame
import sys
import time
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext, ttk
from playsound import playsound
import threading
from PIL import Image, ImageTk
import os
import json
import webbrowser
import traceback

APP_TITLE = "Nathan's Toggler"
ADAPTER_FILE = "adapter_name.txt"
IMG_PATH = "gifman.jpg"
RESTORE_FILE = "restore_config.json"
ICON_FILE = "icon3.ico"

THEME = {
    "dark": {
        "bg": "#1e1e1e",
        "fg": "#ffffff",
        "button_bg": "#333333",
        "highlight": "#007acc"
    },
    "light": {
        "bg": "#ffffff",
        "fg": "#000000",
        "button_bg": "#f0f0f0",
        "highlight": "#0066cc"
    }
}

current_theme = "light"

# --- PyInstaller resource helper ---
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

# --- Admin & Config ---
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except Exception:
        return False

def run_as_admin():
    params = " ".join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

def get_or_prompt_adapter():
    adapter_file = resource_path(ADAPTER_FILE)
    if os.path.exists(adapter_file):
        with open(adapter_file, "r") as f:
            return f.read().strip()
    root = tk.Tk()
    root.withdraw()
    if messagebox.askyesno("Detect Adapter", "Open CMD to help detect your network adapter?"):
        subprocess.run("start cmd /k netsh interface show interface", shell=True)
    name = simpledialog.askstring("Enter Adapter Name", "Enter your network adapter name:")
    if name:
        with open(adapter_file, "w") as f:
            f.write(name.strip())
        return name.strip()
    else:
        messagebox.showerror("Missing Info", "You must enter an adapter name.")
        sys.exit(1)

def reset_adapter_name():
    adapter_file = resource_path(ADAPTER_FILE)
    if os.path.exists(adapter_file):
        os.remove(adapter_file)
    confirm = messagebox.askyesno("Confirmation", "Do you want to open Command Prompt to check your adapter name?")
    if confirm:
        subprocess.run("start cmd /k netsh interface show interface", shell=True)
    adapter_name = simpledialog.askstring("Enter Adapter Name", "Enter your network adapter name (e.g., 'Wi-Fi' or 'Ethernet'):")
    if adapter_name:
        with open(adapter_file, "w") as f:
            f.write(adapter_name.strip())
        messagebox.showinfo("Adapter Saved", f"Saved new adapter: {adapter_name}")
    else:
        messagebox.showwarning("Missing Input", "No adapter name entered.")

# --- JSON Restore Handling ---
def load_restore_data():
    restore_file = resource_path(RESTORE_FILE)
    if not os.path.exists(restore_file):
        return {"firewall_blocks": [], "defender_exclusions": []}
    with open(restore_file, "r") as f:
        return json.load(f)

def save_restore_data(data):
    restore_file = resource_path(RESTORE_FILE)
    with open(restore_file, "w") as f:
        json.dump(data, f, indent=2)

restore_data = load_restore_data()

# --- Defender ---
def is_defender_disabled():
    cmd = 'powershell -Command "Get-MpPreference | Select -Expand DisableRealtimeMonitoring"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip().lower() == "true"

def toggle_defender():
    currently_disabled = is_defender_disabled()
    if currently_disabled:
        subprocess.run('powershell -Command "Set-MpPreference -DisableRealtimeMonitoring 0"', shell=True)
    else:
        subprocess.run('powershell -Command "Set-MpPreference -DisableRealtimeMonitoring 1"', shell=True)
    time.sleep(2)
    new_state = is_defender_disabled()
    if new_state == currently_disabled:
        messagebox.showwarning(
            "Defender",
            "Unable to change Defender state.\n\n"
            "This may be due to Tamper Protection being enabled. "
            "Please turn off Tamper Protection in Windows Security settings and try again."
        )
    return new_state

def get_defender_exclusions():
    cmd = 'powershell -Command "(Get-MpPreference).ExclusionPath"'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return [line.strip() for line in result.stdout.strip().splitlines() if line.strip()]

def remove_defender_exclusion(path):
    subprocess.run(f'powershell -Command "Remove-MpPreference -ExclusionPath \\"{path}\\""', shell=True)

def add_defender_exclusion(folder, log):
    subprocess.run(f'powershell -Command "Add-MpPreference -ExclusionPath \\"{folder}\\""', shell=True)
    if folder not in restore_data["defender_exclusions"]:
        restore_data["defender_exclusions"].append(folder)
        save_restore_data(restore_data)
    log(f"✅ Added to Defender exclusions: {folder}")

# --- Firewall ---
def get_adapter_status(name):
    result = subprocess.check_output('netsh interface show interface', shell=True, text=True)
    for line in result.splitlines():
        if name in line:
            return "Enabled" if "Enabled" in line or "Connected" in line else "Disabled"
    return "Unknown"

def toggle_adapter(name):
    status = get_adapter_status(name)
    state = 'disabled' if status == "Enabled" else 'enabled'
    subprocess.run(f'netsh interface set interface "{name}" admin={state}', shell=True)
    time.sleep(1)
    return get_adapter_status(name)

def list_firewall_rules():
    result = subprocess.run("netsh advfirewall firewall show rule name=all", shell=True, capture_output=True, text=True)
    return [line.strip().replace("Rule Name:", "").strip() for line in result.stdout.splitlines() if line.startswith("Rule Name:")]

def delete_firewall_rule(rule_name):
    subprocess.run(f'netsh advfirewall firewall delete rule name="{rule_name}"', shell=True)

def block_exe_network(folder, log):
    count = 0
    for root_dir, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".exe"):
                full_path = os.path.join(root_dir, file)
                rule = os.path.splitext(file)[0].replace(" ", "_")
                for dir in ["in", "out"]:
                    subprocess.run(f'netsh advfirewall firewall delete rule name="{rule}_{dir}"', shell=True)
                    subprocess.run(f'netsh advfirewall firewall add rule name="{rule}_{dir}" dir={dir} action=block program="{full_path}" enable=yes', shell=True)
                if full_path not in restore_data["firewall_blocks"]:
                    restore_data["firewall_blocks"].append(full_path)
                    save_restore_data(restore_data)
                log(f"🚫 Blocked: {full_path}")
                count += 1
    log(f"✅ Done. {count} files blocked." if count else "⚠️ No .exe files found.")

# --- Auto-Restore ---
def auto_restore(log):
    for exe in restore_data.get("firewall_blocks", []):
        rule = os.path.splitext(os.path.basename(exe))[0].replace(" ", "_")
        for dir in ["in", "out"]:
            subprocess.run(f'netsh advfirewall firewall add rule name="{rule}_{dir}" dir={dir} action=block program="{exe}" enable=yes', shell=True)
        log(f"🔁 Restored firewall block: {exe}")
    for path in restore_data.get("defender_exclusions", []):
        subprocess.run(f'powershell -Command "Add-MpPreference -ExclusionPath \\"{path}\\""', shell=True)
        log(f"🔁 Restored Defender exclusion: {path}")

# --- Music Controls ---
def play_theme():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(resource_path("music.mp3"))
        pygame.mixer.music.play(-1)
    except pygame.error as e:
        print("Pygame error:", e)
        try:
            messagebox.showerror("Music Error", f"Could not play music:\n{e}")
        except Exception:
            pass
    except Exception as e:
        print("Other music error:", e)
        try:
            messagebox.showerror("Music Error", f"Could not play music:\n{e}")
        except Exception:
            pass

def stop_theme():
    try:
        pygame.mixer.music.stop()
    except Exception:
        pass

def open_link(url):
    webbrowser.open_new(url)

def launch_gui():
    global current_theme

    root = tk.Tk()
    root.title(APP_TITLE)
    root.geometry("960x750")
    # --- Set window icon using your icon3.ico ---
    try:
        icon_path = resource_path(ICON_FILE)
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Could not set icon: {e}")

    # --- TITLE AND MESSAGES ---
    tk.Label(root, text="Nathan's Toggler", font=("Arial", 28, "bold")).pack(pady=(18,4))
    tk.Label(
        root,
        text="Thank you for downloading this software! Please make sure to rate 5 stars.",
        font=("Arial", 14, "bold"),
        wraplength=900
    ).pack(pady=(0,2))
    tk.Label(root, text="布洛芬 布洛芬 布洛芬", font=("Arial", 10), fg="#888").pack()

    # --- MUSIC TOGGLE (default ON, music auto-plays) ---
    audio_enabled = tk.BooleanVar(value=True)
    def on_audio_toggle():
        if audio_enabled.get():
            play_theme()
        else:
            stop_theme()
    tk.Checkbutton(root, text="🎧 Headphones Mode (Play Music)", variable=audio_enabled, command=on_audio_toggle).pack()
    play_theme()  # <-- auto-starts music

    notebook = ttk.Notebook(root)
    tabs = [tk.Frame(notebook) for _ in range(3)]
    notebook.add(tabs[0], text='Main')
    notebook.add(tabs[1], text='Exclusion Lists')
    notebook.add(tabs[2], text='About')
    notebook.pack(expand=True, fill='both')

    log_box = scrolledtext.ScrolledText(tabs[0], height=10)
    def log(msg):
        log_box.insert(tk.END, msg + "\n")
        log_box.see(tk.END)

    defender_label = tk.Label(tabs[0], text="Defender: ...")
    internet_label = tk.Label(tabs[0], text="Internet: ...")
    for w in [defender_label, internet_label]: w.pack()
    def update_status():
        defender_label.config(text="Defender: OFF ❌" if is_defender_disabled() else "Defender: ON ✅")
        internet_label.config(text=f"Internet: {get_adapter_status(ADAPTER_NAME)}")

    def update_theme_label():
        theme_btn.config(text="White Theme" if current_theme == "dark" else "Black Theme")

    def toggle_theme():
        global current_theme
        current_theme = "dark" if current_theme == "light" else "light"
        apply_theme()
        update_theme_label()

    def apply_theme():
        theme = THEME[current_theme]
        root.configure(bg=theme["bg"])
        def apply_recursive(widget):
            try:
                widget.configure(bg=theme["bg"], fg=theme["fg"])
            except:
                pass
            for child in widget.winfo_children():
                apply_recursive(child)
        apply_recursive(root)

    theme_btn = tk.Button(root, text="Toggle Theme", command=toggle_theme)
    theme_btn.pack(pady=5)
    update_theme_label()

    def on_defender_toggle():
        new_disabled = toggle_defender()
        update_status()
        log("🔁 Defender toggled: " + ("OFF ❌" if new_disabled else "ON ✅"))
    tk.Button(tabs[0], text="Toggle Defender", command=on_defender_toggle).pack()

    tk.Button(tabs[0], text="Toggle Internet", command=lambda: [toggle_adapter(ADAPTER_NAME), update_status(), log("🔁 Internet toggled")]).pack()
    tk.Button(tabs[0], text="Block Folder's Internet", command=lambda: block_exe_network(simpledialog.askstring("Folder", "Path to block"), log)).pack()
    tk.Button(tabs[0], text="Add Folder to Defender Exclusions", command=lambda: add_defender_exclusion(simpledialog.askstring("Folder", "Exclude path"), log)).pack()
    tk.Button(tabs[0], text="Update Saved Adapter Name", command=reset_adapter_name).pack()
    log_box.pack(pady=5, fill='x')

    # --- SECURITY WARNINGS ---
    warning_text = (
        "• Disabling Defender or Tamper Protection reduces your protection. Do so only if you understand the risks!\n"
        "• On most Windows 10/11 systems, Tamper Protection must be turned off manually in Windows Security > Virus & Threat Protection settings.\n"
        "• Admin rights are required for most changes.\n"
        "• Some PCs (especially work/school) may have policies that prevent disabling Defender—this can’t be bypassed by software.\n"
        "• Always turn protection back on when done.\n"
        "• If an action fails, check for error messages or system restrictions."
    )
    tk.Label(
        tabs[0], text=warning_text, justify="left", font=("Segoe UI", 9, "italic"), fg="#ff9800", bg=None, anchor="w", wraplength=900
    ).pack(pady=(4, 0), padx=8, fill="x")
    tk.Label(tabs[0], text="", height=2).pack()

    # EXCLUSION LIST TAB
    rule_list = tk.Listbox(tabs[1], width=70, height=8)
    exclusion_list = tk.Listbox(tabs[1], width=70, height=8)
    for label, box in [("Firewall Rules", rule_list), ("Defender Exclusions", exclusion_list)]:
        tk.Label(tabs[1], text=label).pack()
        box.pack()
    tk.Button(tabs[1], text="Refresh Rules", command=lambda: [rule_list.delete(0, tk.END), [rule_list.insert(tk.END, r) for r in list_firewall_rules()]]).pack()
    tk.Button(tabs[1], text="Remove Selected Rule", command=lambda: [delete_firewall_rule(rule_list.get(i)) for i in rule_list.curselection()]).pack()
    tk.Button(tabs[1], text="Refresh Exclusions", command=lambda: [exclusion_list.delete(0, tk.END), [exclusion_list.insert(tk.END, e) for e in get_defender_exclusions()]]).pack()
    tk.Button(tabs[1], text="Remove Selected Exclusion", command=lambda: [remove_defender_exclusion(exclusion_list.get(i)) for i in exclusion_list.curselection()]).pack()

    # --- ABOUT TAB WITH INFO AND LINKS ---
    try:
        img = Image.open(resource_path(IMG_PATH))
        img.thumbnail((150, 150))
        img_tk = ImageTk.PhotoImage(img)
        root.img_tk = img_tk
        tk.Label(tabs[2], image=img_tk).pack(pady=10)
    except Exception as e:
        tk.Label(tabs[2], text="[Image failed to load]").pack()

    about_text = tk.Text(
        tabs[2], wrap="word",
        bg=THEME[current_theme]["bg"],
        fg=THEME[current_theme]["fg"],
        bd=0, font=("Segoe UI", 10), height=18
    )
    about_text.pack(padx=10, pady=0, fill="both", expand=True)

    about_content = """\
Nathan398 · he/him
Author, comedian, writer, director, editor, ninja, philanthropist, and proud father of three.
Call me whatever you want—just not late for dinner.

please help me do my laundry. there is too many options on the knob and I don't want to mess anything up. it's been weeks now.

Like the program? Buy me a coffee:
"""
    about_text.insert("end", about_content)

    # PayPal link
    about_text.insert("end", "paypal.me/NathanVarner27\n", "paypal")
    about_text.tag_config("paypal", foreground="blue", underline=True)
    about_text.tag_bind("paypal", "<Button-1>", lambda e: open_link("https://paypal.me/NathanVarner27"))

    about_text.insert("end", "\nSocials:\n")
    socials = {
        "Website": "https://nathanvarner.wixsite.com/nvport",
        "GitHub": "https://github.com/Nathan398",
        "YouTube": "https://www.youtube.com/c/NathanVarner1",
        "Instagram": "https://www.instagram.com/nathanvarner27/",
        "Twitter/X": "https://x.com/NathanVarner",
        "LinkedIn": "https://www.linkedin.com/in/nathanvarner/"
    }
    for label, url in socials.items():
        tag = label.lower().replace("/", "").replace(" ", "_")
        about_text.insert("end", f"{label}\n", tag)
        about_text.tag_config(tag, foreground="blue", underline=True)
        about_text.tag_bind(tag, "<Button-1>", lambda e, url=url: open_link(url))

    about_text.insert("end", "\nMusic:\n")
    about_text.insert("end", "BIOS Music 2.21 by Spencer Nilsen (Sega CD Model 2)\n", "music")
    about_text.tag_config("music", foreground="blue", underline=True)
    about_text.tag_bind("music", "<Button-1>", lambda e: open_link("https://youtu.be/HaQ_DSg6xhs?list=RDHaQ_DSg6xhs"))

    about_text.config(state="disabled")

    update_status()
    auto_restore(log)
    apply_theme()
    root.mainloop()

if __name__ == '__main__':
    try:
        # Dependency check
        missing = []
        for mod in ['tkinter', 'pygame', 'PIL', 'playsound']:
            try:
                __import__(mod if mod != 'PIL' else 'PIL.Image')
            except ImportError:
                missing.append(mod)
        if missing:
            print(f"Missing dependencies: {', '.join(missing)}")
            sys.exit(1)
        if not is_admin():
            run_as_admin()
            sys.exit()
        ADAPTER_NAME = get_or_prompt_adapter()
        launch_gui()
    except Exception as e:
        tb = traceback.format_exc()
        try:
            root = tk.Tk(); root.withdraw()
            messagebox.showerror("Fatal Error", f"{e}\n\nDetails:\n{tb}")
        except Exception:
            print("Fatal Error:", e, "\n\nDetails:\n", tb)
        with open("error.log", "w", encoding="utf-8") as f:
            f.write(tb)
        print("⚠️ Crash captured in error.log")
