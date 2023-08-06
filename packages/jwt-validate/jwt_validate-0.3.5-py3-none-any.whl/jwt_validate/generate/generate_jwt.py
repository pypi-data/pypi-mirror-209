import requests


def generate_jwt():
    headers = {
        'x-api-key': '451a6926-7ce7-491f-abe6-656d699d4783',
    }

    response = requests.get(
        'https://platform-account-api-preprod.luizalabs.com/validate-request',
        headers=headers,
    )
    result = {
        'token': response.json()['accessToken'],
        'status_code': response.status_code,
    }

    return result
