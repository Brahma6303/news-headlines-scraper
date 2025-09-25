import requests
from bs4 import BeautifulSoup

# Step 1: Fetch HTML
url = "https://www.bbc.com/news"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)

# Step 2: Check for successful response
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 3: Extract headlines (usually in <h2> or <h3>)
    headlines = soup.find_all(["h2", "h3"])

    # Step 4: Save to .txt file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for tag in headlines:
            title = tag.get_text(strip=True)
            if title:
                file.write(title + "\n")

    print(" Headlines saved to headlines.txt")
else:
    print(f" Failed to fetch page. Status code: {response.status_code}")