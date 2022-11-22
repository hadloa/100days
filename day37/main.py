import requests
from datetime import datetime


pixela_endpoint = 'https://pixe.la/v1/users'
token= 'l;akjf9pq83url;kaa04uraokmao34rj39a8ufio'
username= 'hadloa'
graph = 'a1'


user_param = {
    'token': 'l;akjf9pq83url;kaa04uraokmao34rj39a8ufio',
    'username': 'hadloa',
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# r = requests.post(url=pixela_endpoint, json=user_param)
# print(r.text)

graph_endpoint = f'{pixela_endpoint}/{username}/graphs'

graph_param = {
    'id': 'a1',
    'name': "hadloa's test graph",
    'unit': 'willpower',
    'type': 'int',
    'color': 'shibafu',
    'timezone': 'US/Pacific'
                }

headers = {
    'X-USER-TOKEN': token
}

#r_graph = requests.post(url=graph_endpoint, json=graph_param, headers=headers)

pixel_endpoint = graph_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph}'
date = datetime.now().strftime('%Y%m%d')
update_param = {
    'date': f'{date}',
    'quantity': f'{10}'
                }
#r_pixel = requests.post(url=pixel_endpoint, json=update_param, headers=headers)

update_pixel_endpoint = f'{pixela_endpoint}/{username}/graphs/{graph}/{date}'

update_param_1 = {
    'quantity': f'{20}'
                }

#r_update = requests.put(url=update_pixel_endpoint, json=update_param_1, headers=headers)

r_delete = requests.delete(url=update_pixel_endpoint, headers=headers)

print(r_delete.text)