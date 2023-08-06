# from app import myUtility
import requests


URL = "https://api.utiliti.ai"
headers = {
    # 'X-API-Key': 'f253d57f-1740-4603-9697-2dc1399eef73',
    "Accept": "*/*",
}

# print(myUtility.apikey)


def GET_RESPONSE(url, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.get(_url, headers=headers)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data


def POST_RESPONSE(url, body, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.post(_url, headers=headers, json=body)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data


def PUT_RESPONSE(url, body, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.put(_url, headers=headers, json=body)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data


def DELETE_RESPONSE(url, apikey):
    headers['X-API-Key'] = apikey
    try:
        _url = f'{URL}/{url}'
        response = requests.delete(_url, headers=headers)
        response.raise_for_status()  # raise an HTTPError for 4xx and 5xx status codes
        data = {
            "status_code": response.status_code,
            "status_text": response.reason,
            "details": response.json()      # parse the response data as JSON
            }  

    except requests.exceptions.RequestException as e:
        print("Error making API request:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  

    except ValueError as e:
        print("Error parsing JSON response:", e)
        return {
            "status_code": e.response.status_code,
            "status_text": e.response.reason,
            "details": e      # parse the response data as JSON
            }  
    else:
        print("API response:", data)
        return data
