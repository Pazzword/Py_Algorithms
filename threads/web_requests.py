import requests
import threading


url = 'enter web link here'  

num_requests = 10

def send_request(i):
    try:
        response = requests.get(url)
        print(f'Request {i+1} status: {response.status_code}')
    except requests.exceptions.RequestException as e:
        print(f'Request {i+1} failed: {e}')

threads = []

for i in range(num_requests):
    thread = threading.Thread(target=send_request, args=(i,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()