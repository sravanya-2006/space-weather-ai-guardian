from dotenv import load_dotenv
import os
import requests
import pandas as pd

# Load environment variables from .env
load_dotenv()

# Read NASA API key
API_KEY = os.getenv("NASA_API_KEY")

if not API_KEY:
    raise ValueError("NASA_API_KEY not found in .env file")

# NASA DONKI Solar Flare Endpoint
URL = "https://api.nasa.gov/DONKI/FLR"

PARAMS = {
    "startDate": "2024-01-01",
    "endDate": "2024-12-31",
    "api_key": API_KEY
}

try:
    print("Fetching Solar Flare Data...")

    response = requests.get(URL, params=PARAMS, timeout=30)

    print(f"Status Code: {response.status_code}")

    response.raise_for_status()

    data = response.json()

    print(f"Records Found: {len(data)}")

    if not data:
        print("No data returned from API.")
        exit()

    # Convert JSON to DataFrame
    df = pd.DataFrame(data)

    # Create data/raw directory if it doesn't exist
    os.makedirs("data/raw", exist_ok=True)

    # Save dataset
    output_file = "data/raw/solar_flares.csv"
    df.to_csv(output_file, index=False)

    print(f"Dataset saved successfully: {output_file}")

    print("\nDataset Shape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

except requests.exceptions.RequestException as e:
    print(f"API Request Error: {e}")

except Exception as e:
    print(f"Unexpected Error: {e}")