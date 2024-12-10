import requests
import json
import os

# Define API URLs
API_BASE_URL = "https://api.socialverseapp.com/"
POSTS_VIEWED_URL = "posts/view"
POSTS_LIKED_URL = "posts/like"
POSTS_INSPIRED_URL = "posts/inspire"
POSTS_RATED_URL = "posts/rating"
POSTS_SUMMARY_URL = "posts/summary/get"

# Headers for API Authorization
HEADERS = {
    "Flic-Token": "flic_6e2d8d25dc29a4ddd382c2383a903cf4a688d1a117f6eb43b35a1e7fadbb84b8"
}

# Directory to save raw data
RAW_DATA_DIR = 'data/raw_data/'

# Create the directory if it doesn't exist
if not os.path.exists(RAW_DATA_DIR):
    os.makedirs(RAW_DATA_DIR)

# Helper function to fetch data
def fetch_data(api_url, params, filename):
    page = 1
    all_data = []
    
    while True:
        params['page'] = page
        response = requests.get(f"{API_BASE_URL}{api_url}", headers=HEADERS, params=params)
        
        if response.status_code == 200:
            data = response.json()
            if not data.get('posts'):  # If no more posts, break
                break
            all_data.extend(data['posts'])
            page += 1
        else:
            print(f"Error fetching data from {api_url}, Status Code: {response.status_code}")
            break
    
    # Save the fetched data to a JSON file
    with open(os.path.join(RAW_DATA_DIR, filename), 'w') as f:
        json.dump(all_data, f, indent=4)
    
    print(f"Fetched {len(all_data)} records and saved to {filename}")

# Fetch data for different categories
def fetch_all_data():
    fetch_data(POSTS_VIEWED_URL, {"page_size": 1000}, "viewed_posts.json")
    fetch_data(POSTS_LIKED_URL, {"page_size": 1000}, "liked_posts.json")
    fetch_data(POSTS_INSPIRED_URL, {"page_size": 1000}, "inspired_posts.json")
    fetch_data(POSTS_RATED_URL, {"page_size": 1000}, "rated_posts.json")
    fetch_data(POSTS_SUMMARY_URL, {"page_size": 1000}, "all_posts_summary.json")

if __name__ == "__main__":
    fetch_all_data()
