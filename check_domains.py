import os
import subprocess
import requests
import socket
from concurrent.futures import ThreadPoolExecutor
from pyfiglet import Figlet
from termcolor import colored

def dashing_opening():
    """Display a dashing opening screen with custom fonts and credits."""
    os.system('clear')
    fig = Figlet(font='slant')
    print(colored(fig.renderText('Domain Checker'), 'cyan'))
    print(colored('By Junaid Farhan', 'magenta'))
    print(colored('https://www.instagram.com/jdf_000/', 'magenta'))
    print(colored('=' * 60, 'yellow'))

def is_pingable(domain):
    """Check if the domain is reachable via ICMP ping."""
    try:
        output = subprocess.run(["ping", "-c", "1", "-W", "1", domain], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return output.returncode == 0
    except Exception:
        return False

def is_dns_resolvable(domain):
    """Check if the domain resolves via DNS."""
    try:
        socket.gethostbyname(domain)
        return True
    except socket.gaierror:
        return False

def is_http_reachable(domain):
    """Check if the domain is reachable via HTTP/HTTPS."""
    try:
        response_http = requests.get(f"http://{domain}", timeout=2)
        response_https = requests.get(f"https://{domain}", timeout=2)
        return response_http.status_code == 200 or response_https.status_code == 200
    except requests.RequestException:
        return False

def check_domain(domain):
    """Check the reachability of a domain using multiple methods."""
    dns_resolvable = is_dns_resolvable(domain)
    pingable = is_pingable(domain)
    http_reachable = is_http_reachable(domain)

    reachable = dns_resolvable and pingable and http_reachable

    if reachable:
        with open('reachable.txt', 'a') as file:
            file.write(domain + '\n')
        print(colored(f"{domain} is reachable.", 'green'))
    else:
        print(colored(f"{domain} is not fully reachable.", 'red'))

def main():
    # Show the opening screen
    dashing_opening()

    # Clear the previous reachable.txt file
    if os.path.exists('reachable.txt'):
        os.remove('reachable.txt')

    # Read domains from domains.txt
    if not os.path.exists('domains.txt'):
        print(colored("domains.txt file not found!", 'red'))
        return

    with open('domains.txt', 'r') as file:
        domains = [line.strip() for line in file if line.strip()]

    # Use ThreadPoolExecutor for faster domain checks
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(check_domain, domains)

    print(colored("\nCheck complete! Reachable domains saved to reachable.txt", 'cyan'))

if __name__ == "__main__":
    main()
