import requests
from dotenv import load_dotenv
import os


load_dotenv()
# Define your TMDb API key
TMDB_API_KEY = os.getenv('API_KEY')

# Function to verify if a title is a valid Korean movie
def is_valid_korean_movie(title: str) -> bool:
    # Call the TMDb API to search for the movie
    tmdb_url = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": title,
    }

    response = requests.get(tmdb_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("results"):
            # Check if the movie is Korean
            first_result = data["results"][0]
            if first_result["title"].lower() == title.lower() and any(
                country["iso_3166_1"] == "KR" for country in first_result["production_countries"]
            ):
                return True
    return False