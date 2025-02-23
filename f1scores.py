import json
import requests
from datetime import datetime

input_json = "test.json"
output_json = "f1_win_factors.json"
ergast_api_url = "https://ergast.com/api/f1/"

def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def save_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def get_race_results(year):
    url = f"{ergast_api_url}{year}/results.json?limit=1000"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("MRData", {}).get("RaceTable", {}).get("Races", [])
    return []

def calculate_win_factor(place):
    return round(1 - (place - 1) / 20, 4)

def filter_f1_sponsorships(data):
    f1_sponsorships = [entry for entry in data if entry["sport"] == "Formula 1"]

    output_data = []

    for entry in f1_sponsorships:
        team = entry["team"]
        company_ticker = entry["company"]
        start_date = datetime.strptime(entry["start_date"], "%Y-%m-%d")
        end_date = datetime.strptime(entry["end_date"], "%Y-%m-%d") if entry["end_date"] else datetime(2024, 12, 31)

        for year in range(start_date.year, min(2024, end_date.year) + 1):
            races = get_race_results(year)

            for race in races:
                race_date = datetime.strptime(race["date"], "%Y-%m-%d")
                if start_date <= race_date <= end_date:
                    team_win_factors = []

                    for result in race["Results"]:
                        if result["Constructor"]["name"] in team:
                            driver_position = int(result["position"])
                            team_win_factors.append(calculate_win_factor(driver_position))

                    if team_win_factors:
                        avg_win_factor = round(sum(team_win_factors) / len(team_win_factors), 4)

                        output_data.append({
                            "company_ticker": company_ticker,
                            "date": race["date"],
                            "outcome_score": avg_win_factor,
                            "sport": "Formula 1"
                        })

    return output_data

data = load_json(input_json)
filtered_f1_data = filter_f1_sponsorships(data)
save_json(filtered_f1_data, output_json)

print(f"Processed F1 sponsorships saved to {output_json}")
