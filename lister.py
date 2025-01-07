import requests
from bs4 import BeautifulSoup

# URL of the webpage
url = 'https://www.ign.com/articles/the-100-best-playstation-games-of-all-time/'

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}

# Making a GET request with headers
r = requests.get(url, headers=headers)

# Check the status code
print(f"Status code: {r.status_code}")  # Should print 200 for a successful request

# Parse the HTML content
soup = BeautifulSoup(r.content, 'html.parser')

# Find all <h2> tags that contain the game titles
game_titles = soup.find_all('h2', class_='title2')

# Extract and print the text from each <h2> tag
for title in game_titles:
    print(title.get_text(strip=True))
