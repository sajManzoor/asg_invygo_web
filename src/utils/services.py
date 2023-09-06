import requests

filters_url = 'https://api.invygo.com/web/api/v2/vehicle-groups/filters'
filter_results_url = 'https://api.invygo.com/web/api/v2/vehicle-groups/list'

headers = {
    'authority': 'api.invygo.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-language': 'en',
    'origin': 'https://www.invygo.com',
    'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': 'macOS',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
}

default_filters_params = {
    'carTypes': 'NORMAL',
    'latitude': '25.2048',
    'limit': '1000',
    'longitude': '55.2708',
    'sortBy': 'PRICE_LOW_TO_HIGH',
    'version': '2',
}


def get_all_filters():
    response = requests.get(filters_url, headers=headers, params=default_filters_params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Request failed with status code {response.status_code}")


def get_all_car_cards(brand: str):
    default_filters_params['brandNames'] = brand
    response = requests.get(filter_results_url, headers=headers, params=default_filters_params)

    if response.status_code == 200:
        data = response.json()
        return data[0]["firstVehicle"]
    else:
        print(f"Request failed with status code {response.status_code}")


