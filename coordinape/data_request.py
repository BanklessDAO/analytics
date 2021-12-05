import requests

# Not working: getting Response 404
response = requests.get(
    "https://coordinape.me/api/users?circle_id=24&deleted_users=true")
print(response)
