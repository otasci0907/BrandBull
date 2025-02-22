import requests
import json

# Your SerpAPI key
API_KEY = "B9E12DC6834C421EACCF7101A449C230"

# List of queries
queries = [
    "Complete list of sports sponsorships 2024",
    "Which companies sponsor professional sports teams?",
    "Major sports sponsorships across leagues 2024",
    "Biggest corporate sponsors in sports",
    "Full list of sports team sponsors",
    "Most valuable sports sponsorship deals",
    "Largest sports sponsorship contracts ever",
    "NBA team sponsors list 2024",
    "NFL team sponsors list 2024",
    "MLB sponsorship deals 2024",
    "NHL corporate sponsors",
    "FIFA World Cup sponsors 2024",
    "Premier League official sponsors",
    "La Liga sponsorship deals",
    "Formula 1 sponsors 2024",
    "Olympic Games sponsors 2024",
    "PGA Tour sponsorships 2024",
    "NASCAR team sponsors 2024",
    "Tennis Grand Slam sponsors list",
    "Esports sponsorships list 2024",
    "Retail companies sponsoring sports teams",
    "Tech companies that sponsor sports leagues",
    "Financial services companies sponsoring sports",
    "Automotive brands that sponsor sports teams",
    "Telecom industry sports sponsorships",
    "Alcohol brands sponsoring professional sports",
    "Airline companies that sponsor sports teams",
    "Insurance companies sponsoring sports leagues",
    "Energy companies in sports sponsorships",
    "Which companies spend the most on sports sponsorships?",
    "Largest sports sponsorship budgets 2024",
    "Global sports sponsorship market trends 2024",
    "Sponsorship revenue of major brands in sports",
    "Top companies by sports sponsorship investment",
    "Most expensive sports sponsorship deals ever",
    "Sports sponsorship spending by industry 2024",
    "sports sponsorship database site:sponsorpitch.com",
    "corporate sponsorship reports site:statista.com",
    "sports sponsorship market research site:sportbusiness.com",
    "team sponsorship deals site:sportspromedia.com",
    "stadium sponsorship agreements site:frontofficesports.com",
    "New sports sponsorship deals announced 2024",
    "Major sports sponsorship announcements",
    "Companies signing new sponsorship contracts 2024",
    "Biggest new sports sponsors this year",
    "Recent sponsorship agreements in sports",
    "Breaking sports sponsorship news site:forbes.com",
]

# Function to get URLs from SerpAPI
def get_urls(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": 'B9E12DC6834C421EACCF7101A449C230',
        "num": 10,  # Get top 10 results
        "engine": "google",
    }

    #response = requests.get(url, params=params)
    response = requests.get(f'https://api.scaleserp.com/search?api_key=B9E12DC6834C421EACCF7101A449C230&q={query}')
    data = response.json()
    
    # Extract URLs
    urls = [result["link"] for result in data.get("organic_results", [])]
    return urls

# Loop through queries
all_urls = {}
for query in queries:
    print(f"Fetching results for: {query}")
    all_urls[query] = get_urls(query)

# Save results to JSON file
with open("sponsorship_urls.json", "w") as file:
    json.dump(all_urls, file, indent=4)

print("URLs saved to sponsorship_urls.json")
