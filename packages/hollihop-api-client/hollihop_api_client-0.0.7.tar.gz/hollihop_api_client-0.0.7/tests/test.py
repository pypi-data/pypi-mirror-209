import os
from hollihop_api_client import HolliHopAPI
from dotenv import load_dotenv

load_dotenv()

hh_api = HolliHopAPI(os.getenv('HH_DOMAIN'), os.getenv('HH_API_COMMON_KEY'))

print(hh_api.leads.get_leads())
