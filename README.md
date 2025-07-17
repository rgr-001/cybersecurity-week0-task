# 🛡️ Zairza Skill++ @2025 – Week 0 Task

This repository contains my completed **Week 0 task** for the **Zairza Skill++ @2025** program.  
The task involved setting up Kali Linux, running basic network scans (`ping`, `nmap`), creating a Python-based port scanner, and documenting all outputs with screenshots.

---

## 📁 Repository Contents

| File Name                        | Description                                   |
|----------------------------------|-----------------------------------------------|
| `port_scanner.py`               | 🐍 Python script to scan open ports            |
| `Kali Linux Desktop.png`        | 🖥️ Screenshot of Kali Linux running            |
| `ping google.com output.png`    | 📡 Output of network ping test                 |
| `nmap scan result.png`          | 🔍 Output of Nmap scan                         |
| `Python port scanner result.png`| 🐍 Result of the Python port scanner           |
| `README.md`                     | 📝 This documentation file                     |

---

## ✅ Tasks Completed

- 🖥️ Installed and launched Kali Linux using VirtualBox
- 🌐 Verified internet access using `ping`
- 🔍 Used `nmap` to perform a port scan
- 🐍 Built and executed a Python-based port scanner
- 📸 Captured screenshots of each step
- ☁️ Uploaded everything to GitHub

---

## 🧪 Tools Used

- 🐧 Kali Linux (VirtualBox)
- `ping` – to test internet connectivity
- `nmap` – for network port scanning
- Python 3 – custom port scanner with `socket` module

---

## 🖼️ Screenshots

### 🖥️ Kali Linux Desktop
> Kali successfully booted and ready

![Kali Linux Desktop](./Kali%20Linux%20Desktop.png)

---

### 📡 Ping to Google
> Network test using `ping -c 4 google.com`

![Ping Output](./ping%20google.com%20output.png)

---

### 🔍 Nmap Scan Result
> Scanned `scanme.nmap.org` to check for open ports

![Nmap Result](./nmap%20scan%20result.png)

---

### 🐍 Python Port Scanner Output
> Output of the Python script scanning ports 1–100

![Python Scanner Output](./Python%20port%20scanner%20result.png)

---

## 🐍 Python Script

```python
import socket

target = input("Enter the target (e.g., scanme.nmap.org or IP address): ")
print(f"\n🔍 Scanning {target} for open ports (1–100)...\n")

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    s.close()
```

---

## 🔗 Submission

- 📎 GitHub Repo: [https://github.com/rgr-001/cybersecurity-week0-task](https://github.com/rgr-001/cybersecurity-week0-task)
- 📄 A `.docx` report has been prepared including:
  - All screenshots
  - Python code
  - This GitHub link

---

## 👤 Author

- 👨‍💻 Name: **Rittik Gourav Raul**  
- 🆔 Regd. No: **23110799**
- 🎓 Program: **Zairza Skill@2025**  
- 📆 Task Week: **0**  


