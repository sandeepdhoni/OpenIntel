# 🚀 OpenIntel - Powerfull OSINT Reconnaissance Framework

OpenIntel is an all-in-one Open Source Intelligence (OSINT) and reconnaissance toolkit designed for security professionals, ethical hackers, and cybersecurity enthusiasts to gather actionable intelligence from various public sources. 🕵️‍♂️🌍

This tool empowers users to map digital footprints, analyze domains, gather metadata, track online activity, and much more—providing a modern approach to OSINT.
# OpenIntel - Advanced OSINT Tool

![OpenIntel Banner](image.png)

OpenIntel is an all-in-one OSINT and reconnaissance solution enabling security researchers to automate data gathering and digital profiling...
---

## ✨ Features at a Glance

| 🛠️ Tool                  | 🔍 Description                                                               |
|---------------------------|-------------------------------------------------------------------------------|
| 🌐 **Domain Profiler**     | Collect comprehensive domain information                                    |
| 🏠 **IP Recon**            | Retrieve IP details with geolocation & network info                         |
| 🕶️ **VPN/Proxy Checker**  | Identify VPN, Proxy, or Tor usage                                           |
| 🗺️ **DNS Mapper**          | Visualize and map DNS records                                                |
| 📍 **IP GeoHeatmap**       | Generate a heatmap of IP geolocations                                       |
| 📞 **Phone Intel**         | Extract details linked to phone numbers                                     |
| 📱 **Social Profiler**     | Investigate social media profiles via usernames                            |
| 🖼️ **Image Tracker**       | Reverse image search to trace image sources                                |
| 🗂️ **Metadata Extractor**  | Extract hidden metadata from files                                           |
| 🧪 **Honeypot Detector**   | Detect honeypots masquerading as real systems                              |
| 🏷️ **MAC Address Profiler**| Fetch MAC address vendor details                                             |
| 🌊 **Torrent Monitor**     | Track torrent download activity                                              |
| 📧 **Email Breach Checker**| Check email/domain for breach history                                        |

---

## 🛠️ Installation Guide

Ensure Python 3.x is installed on your system.

### 🔽 Step 1: Clone the Repository
```bash
git clone https://github.com/sandeepdhoni/openintel.git
cd openintel
```

### ⚙️ Step 2: Install Dependencies & Setup API Keys
```bash
python3 setup.py install
```
You will be prompted to enter the following API keys during setup:

- 🔍 Shodan API Key
- 📲 NumVerify API Key
- 🗺️ IPStack API Key
- 🗺️ Google Maps API Key

Obtain your keys from their respective platforms.

---

## 🚀 Launching OpenIntel
```bash
python3 openintel.py
```
Follow the interactive menu to select tools and start reconnaissance.

---

## 🧑‍💻 Usage Examples

### Example 1: Domain Profiler
```bash
python3 openintel.py
# Select Option 1
# Enter domain (e.g., example.com)
```
### Example 2: IP Recon
```bash
python3 openintel.py
# Select Option 2
# Enter IP Address (e.g., 8.8.8.8)
```
### Example 3: Social Profiler (Username Lookup)
```bash
python3 openintel.py
# Select Option 7
# Enter username (e.g., johndoe123)
```
### Example 4: Metadata Extractor
```bash
python3 openintel.py
# Select Option 9
# Provide path to the file (e.g., /path/to/image.jpg)
```
Feel free to explore other modules similarly by selecting their corresponding options from the interactive menu.

---

## 🔑 API Configuration
API keys are stored in:
- 🛒 `core/config.py` – Shodan API
- 🧩 `plugins/api.py` – NumVerify, IPStack, Google Maps

You can update these keys manually anytime by editing these files.

---

## 📦 System Requirements
- ✅ Python 3.x
- ✅ Dependencies installed via `setup.py`

## 💻 Supported Platforms
- 🐧 Linux
- 🍎 macOS
- 🪟 Windows

---

## ⚖️ Legal Disclaimer
This tool is intended for **legal and ethical use only**. The author is **not responsible for misuse**. Use it responsibly.

---

## 👤 Author
**Sandeep**  
🔗 [GitHub Profile](https://github.com/sandeepdhoni)

---

## 🤝 Contributing
Contributions are welcome! Submit issues or pull requests to help improve OpenIntel.
