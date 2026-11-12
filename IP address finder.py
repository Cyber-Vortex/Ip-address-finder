import requests

def find_ip(ip=None):
    url = f"https://ipapi.co/{ip}/json/" if ip else "https://ipapi.co/json/"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.json()

        if data.get("error"):
            print("Invalid IP Address!")
            return

        print("\n--- IP Address Details ---")
        print("IP Address:", data.get("ip"))
        print("City:", data.get("city"))
        print("Region:", data.get("region"))
        print("Country:", data.get("country_name"))
        print("Longitude:", data.get("longitude"))
        print("Latitude:", data.get("latitude"))
        print("ISP:", data.get("org"))

    except requests.RequestException as e:
        # यह लाइन असली एरर बताएगी कि इंटरनेट बंद है या लाइब्रेरी मिसिंग है
        print(f"Unable to Connect to the Server. Reason: {e}")

ip = input("Enter IP address (leave Empty for your IP): ")
find_ip(ip.strip())
