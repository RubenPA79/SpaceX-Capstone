
import requests
import pandas as pd
import numpy as np
import datetime
from bs4 import BeautifulSoup
import io

# Helper functions to mimic the notebook
BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []

def getBoosterVersion(data):
    for x in data['rocket']:
        if x:
            # Check known IDs to avoid network calls if possible, or just call API
            # For this specific lab, usually we can just call the API or use a cache.
            # However, for speed, let's try to be smart.
            # Falcon 1 ID: 5e9d0d95eda69955f709d1eb
            # Falcon 9 ID: 5e9d0d95eda69973a809d1ec
            # Falcon Heavy ID: 5e9d0d95eda69974db09d1ed
            if x == '5e9d0d95eda69955f709d1eb':
                BoosterVersion.append('Falcon 1')
            elif x == '5e9d0d95eda69973a809d1ec':
                BoosterVersion.append('Falcon 9')
            elif x == '5e9d0d95eda69974db09d1ed':
                 BoosterVersion.append('Falcon Heavy')
            else:
                # Fallback to API if unknown (unlikely for this dataset)
                try:
                    response = requests.get("https://api.spacexdata.com/v4/rockets/"+str(x)).json()
                    BoosterVersion.append(response['name'])
                except:
                    BoosterVersion.append(None)


def getLaunchSite(data):
    # We don't strictly need this for the questions asked (Q1, Q2, Q3, Q4)
    # Q1: static_fire_date_utc (raw data)
    # Q2: Count Falcon 9 (rocket column)
    # Q3: Missing LandingPad (cores column)
    # So we can skip fetching LaunchSite details to save time
    pass

def getPayloadData(data):
    # Not needed for Q1-Q4
    pass

def getCoreData(data):
    for core in data['cores']:
        if core['core'] != None:
            # We don't need to fetch core details from API for LandingPad count
            # The 'cores' column in the 'launches' response acts as a join key or contains data?
            # In the notebook: "From cores we would like to learn... the landing pad used"
            # It fetches: response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
            # AND: LandingPad.append(core['landpad'])  <-- WAIT. 
            # In the notebook code: `LandingPad.append(core['landpad'])` comes from the `core` object inside the `launches` response usually?
            # Let's check the notebook code again.
            # def getCoreData(data):
            #     for core in data['cores']:
            #         ...
            #         LandingPad.append(core['landpad'])
            # It seems 'landpad' is IN the 'core' dict from the initial list, NOT from the fetched core info.
            # Wait, `core` variable is `data['cores']`.
            # In the initial dataframe `data['cores']` is a LIST of cores.
            # The notebook does `data['cores'] = data['cores'].map(lambda x : x[0])`
            # So `core` in `getCoreData` loop is a dictionary like `{'core': '...', 'landpad': '...', ...}`
            # MAKE SURE TO USE THIS VALUE.
            pass
        else:
             pass

def solve():
    # --- Question 1 ---
    static_json_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json'
    response = requests.get(static_json_url)
    data = pd.json_normalize(response.json())
    
    # Q1: Year in first row of static_fire_date_utc
    first_static_fire = data['static_fire_date_utc'].iloc[0]
    # It might be None/NaT. Let's check.
    # The question asks "What year...".
    if first_static_fire:
        q1_year = pd.to_datetime(first_static_fire).year
    else:
        q1_year = "N/A"
    
    print(f"Pregunta 1: {q1_year}")

    # --- Data Processing for Q2 & Q3 ---
    # Filter columns and rows as per notebook
    data = data[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]
    data = data[data['cores'].map(len)==1]
    data = data[data['payloads'].map(len)==1]
    data['cores'] = data['cores'].map(lambda x : x[0])
    data['payloads'] = data['payloads'].map(lambda x : x[0])
    
    # Q2 needs BoosterVersion (Falcon 9 vs Falcon 1)
    getBoosterVersion(data)
    
    # Construct mostly empty dict just for the columns we need
    # We need to mimic the notebook's list population
    
    # Populate lists manually for speed where functions were skipped
    # BoosterVersion is populated by getBoosterVersion
    
    # For LandingPad (Q3), we need to extract it from 'cores' column
    # In notebook: `LandingPad.append(core['landpad'])`
    global LandingPad
    LandingPad = [x['landpad'] for x in data['cores']]
    
    # Create simplified dataframe
    df_sim = pd.DataFrame({
        'BoosterVersion': BoosterVersion,
        'LandingPad': LandingPad
    })
    
    # Q2: How many Falcon 9 launches after removing Falcon 1?
    # Logic: Filter `data['BoosterVersion']!='Falcon 1'`
    # Then count.
    data_falcon9 = df_sim[df_sim['BoosterVersion'] != 'Falcon 1']
    q2_count = len(data_falcon9)
    print(f"Pregunta 2: {q2_count}")
    
    # Q3: Missing values for LandingPad column
    # The notebook says: "The LandingPad column will retain None values... Calculate missing values"
    # data_falcon9.isnull().sum()
    q3_missing = data_falcon9['LandingPad'].isnull().sum()
    print(f"Pregunta 3: {q3_missing}")
    
    # --- Question 4 ---
    # Web scraping
    url = "https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    resp_wiki = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp_wiki.content, 'html.parser')
    print(f"Pregunta 4: {soup.title}")

if __name__ == "__main__":
    solve()
