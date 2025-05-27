from escaneo.ip_scanner import IPScanner
from escaneo.port_scanner import PortScanner

class HerramientaSeguridad:
    def __init__(self):
        self.ip_scanner = IPScanner()
        self.port_scanner = PortScanner()

    def ejecutar_escaneo(self):
        print("=== Iniciando Escaneo Completo ===")
        ips = self.ip_scanner.discover_ips()
        for ip in ips:
            self.port_scanner.scan_ports(ip, [80, 443, 22])
        
        resultados = self.port_scanner.get_results()
        print("\nResumen:")
        for ip, puertos in resultados.items():
            print(f"{ip}: {puertos}")

# Uso desde otro archivo
if __name__ == "__main__":
    herramienta = HerramientaSeguridad()
    herramienta.ejecutar_escaneo()