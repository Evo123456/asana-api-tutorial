import asana
# import pycurl
import urllib3
from urllib3 import request


# Personal access token
personal_access_token = '0/22905d2cc4fed64d634ee62d980737c4'

# CONSTRUCT ASANA CLIENT
client = asana.Client.access_token(personal_access_token)

# url = "https://app.asana.com/api/1.0/projects"

# Get your user info
me = client.users.me()
print(me)
print("Hello,  " + me["name"])
