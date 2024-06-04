import requests

# URL to which the requests will be sent
url = 'https://pashaev.pythonanywhere.com/'  # Replace with your actual URL

# Number of requests to send
num_requests = 10

for i in range(num_requests):
    try:
        response = requests.get(url)
        print(f'Request {i+1} status: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request {i+1} failed: {e}')