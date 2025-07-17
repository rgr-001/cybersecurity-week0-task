
import socket

# Input target
target = input("Enter the target (e.g., scanme.nmap.org or IP address): ")
print(f"\n🔍 Scanning {target} for open ports (1–100)...\n")

# Scan ports 1 to 100
for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)  # timeout for response
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"✅ Port {port} is OPEN")
    
    s.close()
