import json
import requests
from bs4 import BeautifulSoup
import re

# File paths
json_file = "sponsorship_urls_2.json"
output_file = "scraped_text_2.txt"
timeout_duration = 10  # Timeout in seconds

def load_all_urls(file_path):
    """Extracts all URLs from the JSON dictionary (values are lists of URLs)."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    urls = []
    for query, url_list in data.items():
        if isinstance(url_list, list):  # Ensure it's a list before extending
            urls.extend(url_list)

    return urls

def get_clean_text(url):
    """Fetches and extracts visible, cleaned text from a webpage."""
    try:
        headers = {"User-Agent": "Mozilla/5.0"}  # Prevent bot detection

        # Skip URLs ending in .pdf
        if url.lower().endswith(".pdf"):
            print(f"Skipping PDF: {url}")
            return None

        response = requests.get(url, headers=headers, timeout=timeout_duration)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted elements (script, style, meta, etc.)
        for script in soup(["script", "style", "noscript", "meta", "head", "footer"]):
            script.extract()

        # Extract text and clean it
        text = ' '.join(soup.stripped_strings)

        # Remove non-alphanumeric characters except spaces, newlines, and punctuation
        cleaned_text = re.sub(r"[^a-zA-Z0-9\s.,!?']", "", text)

        # Remove excess spaces or newline characters
        cleaned_text = re.sub(r"\s+", " ", cleaned_text).strip()

        return cleaned_text

    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

# Load URLs
urls = load_all_urls(json_file)

# Scrape and save text
with open(output_file, "w", encoding="utf-8") as file:
    for url in urls:
        if url.lower().endswith(".pdf"):
            print(f"Skipping PDF: {url}")
            continue  # Skip this URL

        print(f"Scraping: {url}")
        text = get_clean_text(url)

        if text:
            file.write(f"=== Content from {url} ===\n")
            file.write(text + "\n\n")

print(f"Scraping complete. Text saved to {output_file}")
