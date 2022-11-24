from const import NIX_NAT_EX_URL, NIX_ID, NIX_API_KEY, ANDREW_BIO
from data_requests import post_request_data

header = {
    'x-app-id': NIX_ID,
    'x-app-key': NIX_API_KEY
}

natural_ex_param = {
    'query': 'ran 1 mile',
    'gender': ANDREW_BIO['gender'],
    'weight_kg': ANDREW_BIO['weight_kg'],
    'height_cm': ANDREW_BIO['height_cm'],
    'age': ANDREW_BIO['age']
                        }


def nat_ex_req():
    global natural_ex_param
    natural_input = input("what did you do? ")
    natural_ex_param['query'] = natural_input
    return post_request_data(url=NIX_NAT_EX_URL, headers=header, json=natural_ex_param)


def get_ex_dur_cal():
    data = nat_ex_req()
    exercise = data['exercises'][0]['user_input']
    duration_min = data['exercises'][0]['duration_min']
    nf_calories = data['exercises'][0]['nf_calories']
    return exercise, duration_min, nf_calories
