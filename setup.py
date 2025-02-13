# from setuptools import setup, find_packages
# import os
# import requests
# import zipfile


# def get_user_api_keys():
#     """Prompt user for API keys and save to config files."""
#     shodan_api = input("Enter your Shodan API Key: ").strip()
#     numverify_api = input("Enter your NumVerify API Key: ").strip()
#     ipstack_api = input("Enter your IPStack API Key: ").strip()
#     gmap_api = input("Enter your Google Maps API Key: ").strip()

#     # Write API keys to core/config.py
#     with open("core/config.py", "w") as fout:
#         fout.write(f'shodan_api = "{shodan_api}"\n')

#     # Write API keys to plugins/api.py
#     with open("plugins/api.py", "w") as fout:
#         fout.write("def phoneapis():\n")
#         fout.write(f'    api= "{numverify_api}"\n')
#         fout.write("    return str(api)\n\n")

#         fout.write("def ipstack():\n")
#         fout.write(f'    api= "{ipstack_api}"\n')
#         fout.write("    return str(api)\n\n")

#         fout.write("def gmap():\n")
#         fout.write(f'    api= "{gmap_api}"\n')
#         fout.write("    return str(api)\n")

#     print("\n✅ API Keys have been set successfully!")


# def download_ip2location_db():
#     """Download and extract the IP2Location PX8 LITE database using requests."""
#     url = "https://www.ip2location.com/download?token=hg5uYe2Jvri4R7P1j8b71Pk8dnvIU2M6A9jz2tvcVtGx8ZK2UPQgzr6Hk3cV68oH&file=PX8LITEBIN"
#     plugins_dir = os.path.join(os.getcwd(), "plugins/")
#     zip_path = os.path.join(plugins_dir, "IP2PROXY-LITE-PX8.BIN.ZIP")

#     if not os.path.exists(plugins_dir):
#         os.makedirs(plugins_dir)

#     print("\n🌐 Downloading IP2Location PX8 LITE Database...")
#     response = requests.get(url, stream=True)

#     with open(zip_path, 'wb') as file:
#         for chunk in response.iter_content(chunk_size=1024):
#             if chunk:
#                 file.write(chunk)

#     print("\n📦 Extracting Database...")
#     with zipfile.ZipFile(zip_path, "r") as zip_ref:
#         zip_ref.extract("IP2PROXY-LITE-PX8.BIN", plugins_dir)

#     print("\n✅ IP2Location Database Setup Complete!\n")


# setup(
#     name="OpenIntel",
#     version="1.0.0",
#     description="Advanced OSINT and Reconnaissance Tool",
#     url="https://github.com/sandeepdhoni/openintel",
#     author="Sandeep",
#     author_email="sandeep@example.com",
#     license="GPL-3.0",
#     packages=find_packages(),
#     install_requires=[
#         "shodan", "requests", "prompt_toolkit", "beautifulsoup4", "click",
#         "urllib3", "IP2proxy", "paramiko", "h8mail", "nmap", "pythonping",
#         "whois", "gmplot", "pillow", "lxml", "tweepy"
#     ],
#     python_requires='>=3.6',
# )

# print("\n✅ Dependencies installed successfully!")

# # Call DB Download
# download_ip2location_db()

# # Call API Key Setup
# get_user_api_keys()

# print("\n🎉 Setup Complete! OpenIntel is ready to use.")
import os
import subprocess
import sys
import requests
import zipfile


def install_dependencies():
    """Install all required dependencies using pip."""
    print("\n📦 Installing dependencies...")
    dependencies = [
        "shodan", "requests", "prompt_toolkit", "beautifulsoup4", "click",
        "urllib3", "IP2proxy", "paramiko", "h8mail", "nmap", "pythonping",
        "whois", "gmplot", "pillow", "lxml", "tweepy"
    ]

    subprocess.check_call([sys.executable, "-m", "pip", "install"] + dependencies)
    print("✅ Dependencies installed successfully!")


def download_ip2location_db():
    """Download and extract the IP2Location PX8 LITE database."""
    url = "https://www.ip2location.com/download?token=hg5uYe2Jvri4R7P1j8b71Pk8dnvIU2M6A9jz2tvcVtGx8ZK2UPQgzr6Hk3cV68oH&file=PX8LITEBIN"
    plugins_dir = os.path.join(os.getcwd(), "plugins/")
    zip_path = os.path.join(plugins_dir, "IP2PROXY-LITE-PX8.BIN.ZIP")

    if not os.path.exists(plugins_dir):
        os.makedirs(plugins_dir)

    print("\n🌐 Downloading IP2Location PX8 LITE Database...")
    response = requests.get(url, stream=True)

    with open(zip_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)

    print("\n📦 Extracting Database...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extract("IP2PROXY-LITE-PX8.BIN", plugins_dir)

    print("✅ IP2Location Database Setup Complete!\n")


def get_user_api_keys():
    """Prompt user for API keys and save to config files."""
    shodan_api = input("Enter your Shodan API Key: ").strip()
    numverify_api = input("Enter your NumVerify API Key: ").strip()
    ipstack_api = input("Enter your IPStack API Key: ").strip()
    gmap_api = input("Enter your Google Maps API Key: ").strip()

    # Write API keys to core/config.py
    with open("core/config.py", "w") as fout:
        fout.write(f'shodan_api = "{shodan_api}"\n')

    # Write API keys to plugins/api.py
    with open("plugins/api.py", "w") as fout:
        fout.write("def phoneapis():\n")
        fout.write(f'    api= "{numverify_api}"\n')
        fout.write("    return str(api)\n\n")

        fout.write("def ipstack():\n")
        fout.write(f'    api= "{ipstack_api}"\n')
        fout.write("    return str(api)\n\n")

        fout.write("def gmap():\n")
        fout.write(f'    api= "{gmap_api}"\n')
        fout.write("    return str(api)\n")

    print("\n✅ API Keys have been set successfully!")


if __name__ == '__main__':
    print("🚀 Starting OpenIntel Setup...")

    # Step 1: Install dependencies
    install_dependencies()

    # Step 2: Download the IP2Location Database
    download_ip2location_db()

    # Step 3: Prompt for API keys and save
    get_user_api_keys()

    print("\n🎉 Setup Complete! OpenIntel is ready to use.")