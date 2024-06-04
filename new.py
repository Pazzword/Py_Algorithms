import requests
from bs4 import BeautifulSoup

# URL of the website to scrape
url = 'https://dashb.pythonanywhere.com/dashboard/'

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Successfully fetched the page")
else:
    print(f"Failed to fetch the page, status code: {response.status_code}")

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all news headlines (assuming the class name is 'titlelink')
headlines = soup.find_all('a', class_='titlelink')

# Check if headlines are found
if headlines:
    for i, headline in enumerate(headlines, start=1):
        print(f'{i}. {headline.text}')
else:
    print("No headlines found")
