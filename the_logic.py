import requests, json
from pprint import pprint
from functional_functions import *

#### Config/Init API Call ####
token = ''
base_url = 'https://my.tanda.co/api/v2'
roster_endpoint = base_url + '/rosters/current'
schedules_endpoint = base_url + '/schedules'
profile_endpoint =  base_url + '/users/me'

header = {'Authorization': 'bearer ' + token, 'Cache-Control': 'no-cache'}
api_call = requests.get(roster_endpoint, headers=header)
api_return = api_call.json()

user_id = 207955
Shifts = []
tmpShifts = {}
#######################


input = next_7(user_id)

shifts_call = requests.get(schedules_endpoint, headers=header, params=input).json()

##pprint(shifts_call)
##print('\n\n')

def get_Shift():
    shifts = extractor(shifts_call)

    return shifts
