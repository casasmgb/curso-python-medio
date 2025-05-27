from escaneo.ip_scanner import IPScanner
from escaneo.port_scanner import PortScanner

def main():
    # Escaneo de IPs
    ip_scanner = IPScanner(network_prefix="172.16.22")
    active_ips = ip_scanner.discover_ips()

    print(f"[+] IPs activas encontradas: {active_ips}")
    # Escaneo de puertos
    port_scanner = PortScanner()
    ports_to_scan = [21, 22, 80, 443, 3389, 3306, 5432, 5900, 8080]  # Personaliza aquí

    print("\n[*] Escaneando puertos en las IPs activas...")
    for ip in active_ips:
        open_ports = port_scanner.scan_ports(ip, ports_to_scan)
        if open_ports:
            print(f"  - {ip}: Puertos abiertos → {open_ports}")

    # Guardar resultados
    port_scanner.save_results()

if __name__ == "__main__":
    main()