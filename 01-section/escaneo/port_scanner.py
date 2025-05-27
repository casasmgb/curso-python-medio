import socket
from concurrent.futures import ThreadPoolExecutor

class PortScanner:
    def __init__(self):
        self.open_ports = {}  # {ip: [puertos_abiertos]}

    def scan_port(self, ip, port, timeout=1):
        """Escanea un puerto TCP en una IP."""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(timeout)
                s.connect((ip, port))
                return port
        except:
            return None

    def scan_ports(self, ip, ports_to_scan, max_threads=20):
        """Escanea múltiples puertos en una IP."""
        open_ports = []
        with ThreadPoolExecutor(max_threads) as executor:
            results = executor.map(lambda port: self.scan_port(ip, port), ports_to_scan)
        
        open_ports = [port for port in results if port is not None]
        if open_ports:
            self.open_ports[ip] = open_ports
        return open_ports

    def get_results(self):
        """Devuelve los resultados del escaneo."""
        return self.open_ports

    def save_results(self, filename="scan_results.txt"):
        """Guarda los resultados en un archivo."""
        with open(filename, "w") as f:
            f.write("Resultados del escaneo:\n")
            f.write("=" * 30 + "\n")
            for ip, ports in self.open_ports.items():
                f.write(f"{ip}: {ports}\n")
        print(f"\n[+] Resultados guardados en '{filename}'.")