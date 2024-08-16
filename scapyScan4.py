#!/usr/bin/python3

# Script Name: scapyScan4.py
# Author: Michael Sineiro
# Date of latest revision: 8/15/2024
# adapted from a script I previously wrote https://github.com/KrustyKode/ops_challenges/blob/main/401/scapyScan3.py
# Purpose: Enhanced network scanning tool with ICMP ping and port scanning functionalities using Scapy.
# This version includes improvements for user input validation, error handling, feedback, and additional features.

### MUST HAVE SCAPY AND TQDM INSTALLED 
### sudo pip install tqdm
### sudo pip install scapy
### MUST BE RUN USING SUDO


from concurrent.futures import ThreadPoolExecutor
from scapy.layers.inet import IP, ICMP, TCP
from scapy.sendrecv import sr1, send
from scapy.volatile import RandShort
from ipaddress import ip_address
from colorama import Fore, Style, init
from tqdm import tqdm
import argparse
import signal
import sys
from socket import gethostbyname, gaierror

# Initialize colorama for color-coded output
init(autoreset=True)

def signal_handler(sig, frame):
    """Handle script interruption gracefully."""
    print("\nExiting... Please wait while we clean up.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def validate_ip_format(ip):
    """Check if the IP is in proper IPv4 format."""
    try:
        ip_address(ip)
        return True
    except ValueError:
        return False

def resolve_hostname(host):
    """Resolve a hostname to an IP address."""
    try:
        return gethostbyname(host)
    except gaierror:
        print_error(f"Could not resolve hostname: {host}")
        sys.exit(1)

def validate_ip(ip):
    """Validate the given IP address or hostname to ensure it's in a proper IPv4 format."""
    if validate_ip_format(ip):
        return ip
    else:
        return resolve_hostname(ip)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(description='Enhanced Network Scanner')
    parser.add_argument('-t', '--target', help='Target IP address or hostname', required=True)
    parser.add_argument('-sp', '--start_port', help='Starting port number', type=int, default=1)
    parser.add_argument('-ep', '--end_port', help='Ending port number', type=int, default=1024)
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    return parser.parse_args()

def icmp_ping(target_host):
    """Check if the target host responds to ICMP echo requests (ping)."""
    try:
        pkt = IP(dst=target_host)/ICMP()
        resp = sr1(pkt, timeout=1, verbose=0)
        return resp is not None
    except Exception as e:
        print_error(f"Error during ICMP ping: {e}")
        return False

def print_open_port(port):
    """Print the open port with green color."""
    print(f"{Fore.GREEN}Port {port}: Open{Style.RESET_ALL}")

def print_error(message):
    """Print error messages in red color."""
    print(f"{Fore.RED}Error: {message}{Style.RESET_ALL}")

def scan_port(target_host, port, result_list):
    """Scan a specific TCP port on the target host and record if it's open."""
    src_port = RandShort()  # Generate a random source port
    try:
        response = sr1(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="S"), timeout=1, verbose=0)
        if response is not None and response.haslayer(TCP):
            if response[TCP].flags == 0x12:  # Check for SYN/ACK flags
                # Send a RST packet to close the connection
                send(IP(dst=target_host)/TCP(sport=src_port, dport=port, flags="R"), verbose=0)
                result_list.append(port)  # Port is open
    except Exception as e:
        print_error(f"Error scanning port {port}: {e}")

def port_scan(target_host, start_port, end_port):
    """Perform a TCP port scan on the target host, using threading for efficiency."""
    print(f"Scanning {target_host} for open ports...")
    open_ports = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = []
        for port in tqdm(range(start_port, end_port + 1), desc="Scanning Ports", unit="port"):
            futures.append(executor.submit(scan_port, target_host, port, open_ports))
    return sorted(open_ports)

def save_results_to_file(results, filename='scan_results.txt'):
    """Save the scan results to a text file."""
    with open(filename, 'w') as f:
        for port in results:
            f.write(f"Port {port}: Open\n")
    print(f"{Fore.GREEN}Results saved to {filename}{Style.RESET_ALL}")

def main():
    """Main function to orchestrate the scanning process based on user input."""
    args = parse_arguments()
    target_host = validate_ip(args.target)
    start_port, end_port = args.start_port, args.end_port

    if icmp_ping(target_host):
        print(f"{Fore.BLUE}Host {target_host} is up. Proceeding with port scan...{Style.RESET_ALL}")
        open_ports = port_scan(target_host, start_port, end_port)
        if open_ports:
            print(f"{Fore.CYAN}Open ports:{Style.RESET_ALL}")
            for port in open_ports:
                print_open_port(port)
            save_results_to_file(open_ports)
        else:
            print(f"{Fore.YELLOW}No open ports found.{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}Host {target_host} is down or not responding to ICMP echo requests.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
