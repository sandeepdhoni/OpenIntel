import sys

def banner():
    return ("""
 ██████╗ ██████╗ ███████╗███████╗███╗   ██╗██╗████████╗███████╗██╗
██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║██║╚══██╔══╝██╔════╝██║
██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║██║   ██║   █████╗  ██║
██║   ██║██╔═══╝ ██╔══╝  ██╔══╝  ██║╚██╗██║██║   ██║   ██╔══╝  ██║
╚██████╔╝██║     ███████╗███████╗██║ ╚████║██║   ██║   ███████╗███████╗
 ╚═════╝ ╚═╝     ╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚══════╝╚══════╝

                   $ OpenIntel - Open Data, Clear Insights!
""")
def menu():
    return ("""
ENTER 0 - 13 TO SELECT OPTIONS

1.  Domain Profiler          Gather information about a given domain
2.  IP Recon                 Enumerate detailed information from an IP address
3.  VPN/Proxy Checker        Check if an IP uses VPN, Proxy, or TOR
4.  DNS Mapper               Map and visualize DNS records of a target
5.  IP GeoHeatmap            Visualize geolocation data of IP addresses
6.  Phone Intel              Retrieve information associated with a phone number
7.  Social Profiler          Extract account information from social media
8.  Image Tracker            Perform reverse image search to trace image origins
9.  Metadata Extractor       Extract metadata from uploaded files
10. Honeypot Detector        Detect if a system is a honeypot or a real host
11. MAC Address Profiler     Retrieve vendor and device details from a MAC address
12. Torrent Monitor          Investigate torrent activity and download history of an IP
13. Email Breach Checker     Check if emails from a domain have been involved in breaches
99. UPDATE                   Update OpenIntel to its latest version

0. EXIT                         Exit from  OpenIntel  to your terminal
       """)

if __name__ == '__main__':
    if sys.version_info[0] > 2:
        try:
            print(banner())
            from core import repl_prompt
        except ModuleNotFoundError:
            print("\nIt looks like the required dependencies are missing, or you're not using Python 3. Please install the requirements using:\n\npython3 setup.py install")
            quit()
    else:
        try:
            from core import repl_prompt
        except ImportError:
            print("\nThis tool requires Python 3 and the necessary dependencies. Please install them using:\n\npython3 setup.py install")
            quit()