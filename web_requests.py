import requests
import threading

# URL to which the requests will be sent
url = 'https://pashaev.pythonanywhere.com/'  # Replace with your actual URL

# Number of requests to send
num_requests = 10

def send_request(i):
    try:
        response = requests.get(url)
        print(f'Request {i+1} status: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request {i+1} failed: {e}')

threads = []

# Creating and starting threads
for i in range(num_requests):
    thread = threading.Thread(target=send_request, args=(i,))
    thread.start()
    threads.append(thread)

# Waiting for all threads to complete
for thread in threads:
    thread.join()