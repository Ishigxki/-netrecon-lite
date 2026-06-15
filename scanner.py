import socket

target = input("Target IP or Hostname: ")

for port in [22, 80, 433, 3306, 5432, 8080]:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result ==0:
        print(f"[OPEN] {port}")


    sock.close()