import subprocess
from concurrent.futures import ThreadPoolExecutor

class IPScanner:
    def __init__(self, network_prefix="192.168.1"):
        self.network_prefix = network_prefix
        self.active_ips = []

    def ping_ip(self, ip):
        """Verifica si una IP está activa usando ping."""
        try:
            param = "-n" if subprocess.os.name == "nt" else "-c"
            subprocess.run(
                ["ping", param, "1", ip],
                timeout=1,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            return ip
        except:
            return None

    def discover_ips(self, start=1, end=254, max_threads=50):
        """Descubre IPs activas en el rango especificado."""
        print(f"[*] Escaneando IPs en {self.network_prefix}.X...")
        
        with ThreadPoolExecutor(max_threads) as executor:
            ips = [f"{self.network_prefix}.{i}" for i in range(start, end + 1)]
            results = executor.map(self.ping_ip, ips)
        
        self.active_ips = [ip for ip in results if ip is not None]
        # print(f"[+] IPs activas encontradas: {self.active_ips}")
        return self.active_ips