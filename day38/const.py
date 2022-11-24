import os

NIX_NAT_EX_URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
NIX_API_KEY = os.environ['NIX_API_KEY']
NIX_ID = os.environ['NIX_ID']

ANDREW_BIO = {'gender': 'male',
              'weight_kg': '66',
              'height_cm': '170',
              'age': '30'}

# -----------------------------------------------------------------------
SHEETLY_URL_POST = 'https://api.sheety.co/42d9c8c88b600e298147017771843602/copyOfMyWorkouts/workouts'
# SHEETLY_URL_PUT = 'https://api.sheety.co/42d9c8c88b600e298147017771843602/copyOfMyWorkouts/workouts/[Object ID]'
SHEETLY_KEY = os.environ['SHEETLY_KEY']
# --------------------------------------------------------------------------

EXERCISE = 0
DURATION = 1
CALORIES = 2

# --------------------------------------------------------
OAI_API_KEY = os.environ['OAI_API_KEY']
OAI_ID = os.environ['OAI_ID']
