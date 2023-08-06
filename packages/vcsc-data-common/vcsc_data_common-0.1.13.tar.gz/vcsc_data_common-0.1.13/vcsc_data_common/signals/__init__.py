import requests
import json

def publish_signals_to_all_domains(data):
    domains = ['https://mt-dev.vietcap.com.vn']

    for domain in domains:
        try:
            publish_signals_to_domain(domain,data)
        except Exception as e:
            print(e)
            print(f'error publish signal to {domain}')

def publish_signals_to_domain(domain:str,data):
    token = get_token(domain)
    publish_signals(domain,token,data)

def publish_signals(domain:str,token:str,data):
    url = f"{domain}/api/signal-ai-service/v1/signal/create"

    headers = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJjbGllbnRJZCI6IjA5YWIxMWFmLWI3MjQtNDc3NS1hODQ2LTg5ODA0N2Q5ZGViNyIsImFwcGxpY2F0aW9uTmFtZSI6IldFQiBBSSIsImlhdCI6MTY4NDQ4MjQwMH0.GUpu26klAleNKPUAwVzFjT9bP-b-XHU-zaYBnz9p0_tsbvjjju51jevqOh1TNNvFziF4WSbXpLAioNbcnpGFN2Fsr85YIubNA93wsGpY8yefV7ZKlQ379F_kvfKjkrZA3GpD8Tc5u33uuR10RVr3kVkyutvaaOL0LJuj8hv1NEcd199wNME_-jLqkJNoMnrp7DyjN-MNIFMKtCRl_bVY39GCKhjtG7tYZznJcd-857ZnEpKIaQw_Dx0DwBbBtC1fqWGNs00gvqa3MMfKEX7Yv7HPtifL4mELaR25Md0sWE7nTwanP3bf1w7P2nUaV67gEULrARXkMyLJeIkk4qkAHw',
    'Cookie': 'JSESSIONID=C8BEE7F4C0ECCDAC4183D867819FE5FE; JSESSIONID=03273813B9359E33074821215EF72442',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))
    print(response.text)

def get_token(domain:str)->str:
    url = f"{domain}/api/iam-external-service/v1/authentication/login"

    payload = json.dumps({})
    headers = {
    'Content-Type': 'application/json',
    'Accept': '*',
    'grant-type': 'client_credential',
    'client-id': 'ff120ac8-9911-4b0f-8041-9dce64d5dbad',
    'client-secret': '123456'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)['data']['token']