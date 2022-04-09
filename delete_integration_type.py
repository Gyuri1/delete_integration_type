# Module Maker
# https://ciscosecurity.github.io/tr-05-module-maker/

# API Documentation:
# https://visibility.amp.cisco.com/iroh/iroh-int/index.html#/ModuleType/delete_iroh_iroh_int_module_type__id_

import requests
from requests.auth import HTTPBasicAuth

# Create SecureX API Client here:
# https://securex.us.security.cisco.com/settings/apiClients
ctr_user_id = "client-XX"
ctr_password = "XXX"

# Auth 
url = "https://visibility.amp.cisco.com/iroh/oauth2/token"
payload='grant_type=client_credentials'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

print("Connection SecureX CTR Integration API ... ")
response = requests.request("POST", url, headers=headers, data=payload, auth=HTTPBasicAuth(ctr_user_id, ctr_password))
json_data=response.json();
ctr_token=json_data['access_token'];
print("Authentication was successful.")

# Get Integration Module Type
url = "https://visibility.amp.cisco.com/iroh/iroh-int/module-type"
payload = ""
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer '+ctr_token
}
response = requests.request("GET", url, headers=headers, data=payload)
res=response.json()
print("Integration Module Types:")
for r in res:
  print(r["title"])

int_module=input("Which Integration Module Type do You want to delete?")

int_module_id=0

for r in res:
  if int_module == r["title"]:
    int_module_id = r["id"] 

# Delete Integration Module Type
if int_module_id :
  url = "https://visibility.amp.cisco.com/iroh/iroh-int/module-type/"+int_module_id
  payload = ""
  headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer '+ctr_token
  }
  response = requests.request("DELETE", url, headers=headers, data=payload)
  print(f"{int_module} was successfully deleted.")

else:
  print("Error: Integration Module Type Not Found.")


