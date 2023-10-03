from bs4 import BeautifulSoup
import requests

def fetch_metadata(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the website.")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    title = soup.title.string if soup.title else "No title found"
    
    description_tag = soup.find("meta", attrs={"name": "description"})
    description = description_tag["content"] if description_tag else "No description found"
    
    keywords_tag = soup.find("meta", attrs={"name": "keywords"})
    keywords = keywords_tag["content"] if keywords_tag else "No keywords found"
    
    print(f"Website: {url}")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Keywords: {keywords}")

# Test the function
fetch_metadata("https://www.example.com")
