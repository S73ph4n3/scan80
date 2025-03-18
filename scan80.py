import socket
import threading
import time

def scan_ip(ip, port=80, timeout=1):
    """Tente de se connecter à une IP sur un port donné."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((ip, port))
        sock.close()
        if result == 0:
            return True
        return False
    except Exception:
        return False

def scan_network(network, start=1, end=255):
    """Scanne une plage d'adresses IP dans le réseau."""
    active_hosts = []
    threads = []

    print(f"Scan en cours sur {network}.[{start}-{end}]...")

    def check_host(ip):
        if scan_ip(ip):
            active_hosts.append(ip)
            print(f"[+] Appareil trouvé à {ip}")

    # Créer des threads pour accélérer le scan
    for i in range(start, end + 1):
        ip = f"{network}.{i}"
        thread = threading.Thread(target=check_host, args=(ip,))
        threads.append(thread)
        thread.start()

    # Attendre que tous les threads se terminent
    for thread in threads:
        thread.join()

    return active_hosts

if __name__ == "__main__":
    # Exemple : scanner le réseau local 192.168.1.0/24
    network = "192.168.1"  # Remplacez par votre propre réseau
    start_time = time.time()

    hosts = scan_network(network, start=1, end=255)

    end_time = time.time()
    print("\nScan terminé !")
    print(f"Temps écoulé : {end_time - start_time:.2f} secondes")
    print(f"Appareils trouvés : {len(hosts)}")
    for host in hosts:
        print(f"- {host}")
