def get_user_api_keys():
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

    print("\n✅ API Keys have been set successfully.")

if __name__ == "__main__":
    get_user_api_keys()
