import requests
from pprint import pprint
import os

# using python-dotenv method
from dotenv import load_dotenv
load_dotenv()

# authorization & header
auth_token = os.environ.get('AUTH_TOKEN')
HEADER = {'Authorization': f'{auth_token}'}

# ----- Data Endpoints

# Coordinape Round -- OG Bankless(June): Circle id 24
response24 = requests.get(
    'https://api.coordinape.com/api/v2/token-gifts?circle_id=24', headers=HEADER)
pprint(response24.json())


# Coordinape Round -- Bankless L1: Circle id 305
# response2 = requests.get('https://api.coordinape.com/api/v2/token-gifts?circle_id=305', headers=HEADER)
# pprint(response2.json())

# Coordinape Round -- Bankless L2: Circle id 492
# response3 = requests.get('https://api.coordinape.com/api/v2/token-gifts?circle_id=492', headers=HEADER)
# pprint(response3.json())

# Coordinape Round -- Bankless GP: Circle id 878
# response4 = requests.get('https://api.coordinape.com/api/v2/token-gifts?circle_id=878', headers=HEADER)
# pprint(response4.json())


# ----- Get Epochs

# Epochs for Circle ID 24
# response1_epoch = requests.get('https://api.coordinape.com/api/v2/24/epoches', headers=HEADER)
# pprint(response1_epoch.json())

# Epochs for Circle ID 305
# response2_epoch = requests.get('https://api.coordinape.com/api/v2/305/epoches', headers=HEADER)
# pprint(response2_epoch.json())

# Epochs for Circle ID 492
# response3_epoch = requests.get('https://api.coordinape.com/api/v2/492/epoches', headers=HEADER)
# pprint(response3_epoch.json())

# Epochs for Circle ID 878
# response4_epoch = requests.get('https://api.coordinape.com/api/v2/878/epoches', headers=HEADER)
# pprint(response4_epoch.json())

# ----- Circle Data (Comprehensive) - no permissions

# {'message': 'User has no permission to view this profile'}
# comp_response = requests.get('https://api.coordinape.com/api/v2/profile/full-circle?circle_id=24', headers=HEADER)
# pprint(comp_response.json())
