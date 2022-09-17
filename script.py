# Standard Libraries

# Third party packages
import requests


r = requests.get("https://coreyms.com")
print(r.status_code)
