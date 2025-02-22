import requests
import json

# Your SerpAPI key
API_KEY = "B9E12DC6834C421EACCF7101A449C230"

# List of queries
queries_old = [
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
        "Fortune 500 companies sponsoring the Super Bowl",
    "Fortune 500 companies sponsoring the FIFA World Cup",
    "Fortune 500 companies sponsoring the Olympic Games",
    "Major sponsors of the 2022 Winter Olympics",
    "Fortune 500 brands sponsoring the NBA Finals",
    "Companies sponsoring the NFL Super Bowl Halftime Show",
    "Fortune 500 companies sponsoring the UEFA Champions League",
    "Fortune 500 sponsors of major tennis events like Wimbledon",
    "Companies sponsoring the FIFA Women's World Cup",
    "Fortune 500 sponsors of the NCAA March Madness",
    "Fortune 500 companies sponsoring the Tour de France",
    "Major companies sponsoring the Rugby World Cup",
    "Fortune 500 brands sponsoring the Daytona 500",
    "Major sponsors of the Monaco Grand Prix",
    "Fortune 500 sponsors for the 2020 Summer Olympics",
    "Nike, Coca-Cola, and other Fortune 500 companies sponsoring sports events",
    "Sponsors of the 2018 FIFA World Cup",
    "Companies sponsoring the 2020 Summer Olympics",
    "Sponsors of the 2022 Super Bowl",
    "Major sponsors of the 2016 Rio Olympics",
    "Fortune 500 brands sponsoring the 2014 FIFA World Cup",
    "Companies sponsoring the 2010 Winter Olympics in Vancouver",
    "Fortune 500 sponsors of the 2019 Cricket World Cup",
    "Companies sponsoring the 2015 Women's World Cup",
    "Sponsors of the 2023 Rugby World Cup",
    "Fortune 500 brands sponsoring the NBA and NFL teams",
    "Fortune 500 companies sponsoring MLB teams",
    "Fortune 500 sponsors of the 2019 NBA Finals",
    "Brands sponsoring the 2020 UEFA Champions League Final",
    "Fortune 500 companies sponsoring Major League Soccer",
    "Fortune 500 sponsors for the College Football Playoff",
    "Top Fortune 500 sponsors of the NFL season",
    "Coca-Cola and Pepsi sponsoring the 2016 Olympics",
    "Nike and Adidas sponsorship deals in FIFA World Cup",
    "Fortune 500 companies sponsoring Formula 1 teams",
    "Fortune 500 sponsors in Formula 1 racing",
    "Major sponsors of Formula 1 teams 2023",
    "Fortune 500 sponsors of Red Bull Racing Formula 1",
    "Fortune 500 brands sponsoring Mercedes F1 team",
    "Companies sponsoring Ferrari Formula 1 team",
    "Fortune 500 sponsors of McLaren F1 team",
    "Companies sponsoring Formula 1 Grand Prix 2022",
    "Formula 1 sponsorship deals with Fortune 500 companies",
    "Brands sponsoring the F1 Monaco Grand Prix",
    "Sponsors of Formula 1 races in Europe 2022",
    "Major sponsors of the F1 British Grand Prix",
    "Companies sponsoring the F1 Abu Dhabi Grand Prix",
    "Fortune 500 companies sponsoring the F1 Singapore Grand Prix",
    "Sponsors of the 2020 Formula 1 season",
    "Formula 1 sponsorships for the 2019 Monaco Grand Prix",
    "Fortune 500 brands sponsoring the 2021 F1 Australian Grand Prix",
    "Sponsors of the 2018 Formula 1 season",
    "Companies sponsoring the 2022 Formula 1 British Grand Prix",
    "Major sponsors of the 2017 Formula 1 Malaysian Grand Prix",
    "Fortune 500 companies sponsoring the 2014 Formula 1 Monaco Grand Prix",
    "Brands sponsoring the 2016 Formula 1 Abu Dhabi Grand Prix",
    "F1 sponsors for the 2015 Italian Grand Prix",
    "Companies sponsoring the F1 Ferrari team 2020",
    "Major sponsors of the Red Bull Racing Formula 1 team",
    "Fortune 500 companies sponsoring the Mercedes AMG Petronas F1 team",
    "Brands sponsoring the McLaren Formula 1 team 2023",
    "Corporate sponsorships of Williams F1 team",
    "Fortune 500 companies backing Aston Martin F1 team",
    "Companies sponsoring Alfa Romeo Formula 1 team",
    "Fortune 500 sponsors of the F1 Monaco Grand Prix 2021",
    "Companies sponsoring the 2021 Formula 1 French Grand Prix",
    "Major sponsors of the 2020 F1 Bahrain Grand Prix",
    "Sponsors of the 2022 F1 Canadian Grand Prix",
    "Corporate sponsors for the 2018 Formula 1 Japanese Grand Prix",
    "How Fortune 500 companies have partnered with Formula 1 over the years",
    "List of Fortune 500 sponsors for Formula 1 2019-2022",
    "Historical sponsors of Formula 1 teams and events",
    "How F1 sponsorship deals affect global brands like Coca-Cola and Shell",
    "Fortune 500 companies’ involvement in Formula 1 racing since 2000",
    "Fortune 500 companies sponsoring NFL teams",
    "Fortune 500 sponsors in the NFL 2023",
    "Companies sponsoring NFL teams 2022",
    "Major sponsors of the NFL Super Bowl 2023",
    "NFL sponsorship deals with Fortune 500 companies",
    "Brands sponsoring the NFL 2022 season",
    "Sponsors of the NFL 2021 playoffs",
    "Fortune 500 companies sponsoring NFL games",
    "Super Bowl 2023 Fortune 500 sponsors",
    "Major sponsors of the 2022 Super Bowl",
    "Companies sponsoring the Super Bowl 2021",
    "Fortune 500 companies in the Super Bowl 2020",
    "Fortune 500 brands sponsoring Super Bowl halftime",
    "Top sponsors of Super Bowl LV",
    "Fortune 500 sponsors of the Super Bowl 2019",
    "Super Bowl 2023 major sponsors",
    "Companies sponsoring the 2022 FIFA World Cup Qatar",
    "Major sponsors of the 2022 FIFA World Cup",
    "Fortune 500 sponsors for the 2022 UEFA Champions League",
    "Sponsors of the UEFA Champions League final 2022",
    "Top sponsors for the 2019 FIFA Women’s World Cup",
    "Companies sponsoring UEFA Euro 2020",
    "Sponsors of the 2018 FIFA World Cup Russia",
    "Fortune 500 sponsors of the FIFA Women’s World Cup 2019",
    "Fortune 500 sponsorships in the UEFA Champions League 2021",
    "Companies sponsoring Manchester United",
    "Fortune 500 companies sponsoring Chelsea FC 2022",
    "Major sponsors of Barcelona FC 2023",
    "Corporate sponsors of Real Madrid 2022",
    "Fortune 500 companies sponsoring Arsenal FC",
    "Brands sponsoring Bayern Munich 2023",
    "Companies sponsoring Paris Saint-Germain 2021",
    "Sponsors of LA Galaxy 2022",
    "Major sponsors of New York Red Bulls 2023",
    "Fortune 500 sponsors of soccer events in North America",
    "Companies sponsoring the 2022 Copa America"
]

queries = [

]



# Function to get URLs from SerpAPI
def get_urls(query):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": 'EB83818AB3E34E94B01E675B0DAB21B0',
        "num": 5,  # Get top 10 results
        "engine": "google",
    }

    #response = requests.get(url, params=params)
    #response = requests.get(f'https://api.scaleserp.com/search?api_key=EB83818AB3E34E94B01E675B0DAB21B0&q={query}')
    response = requests.get('https://api.scaleserp.com/search', params)
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
with open("sponsorship_urls_3.json", "w") as file:
    json.dump(all_urls, file, indent=4)

print("URLs saved to sponsorship_urls.json")
