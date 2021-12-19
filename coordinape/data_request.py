import requests

# Not working: getting Response 404
response = requests.get("https://coordinape.me/api/users?circle_id=24")
print(response)

#response = requests.get("https://coordinape.me/api/users?circle_id=24&deleted_users=true")
# print(response)

# Not working getting Response 404
# response = requests.get('https://staging-api.coordinape.com/api/circles')
# print(response)
