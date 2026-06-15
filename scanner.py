import socket

target = input("Target IP or Hostname: ")

ports = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    8080: "HTTP-ALT"
}

print(f"\n[+] Scanning target: {target}\n")

for port, service in ports.items():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"[OPEN] {port} ({service})")
    else:
        print(f"[CLOSED] {port} ({service})")

    sock.close()
