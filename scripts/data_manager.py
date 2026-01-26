import requests
import os

# Define URLs for the datasets
datasets = {
    "dataset_part_1.csv": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv",
    "dataset_part_2.csv": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_2.csv",
    "spacex_launch_dash.csv": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv",
    "spacex_launch_geo.csv": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_geo.csv",
    "Spacex.csv": "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv"
}

def download_data():
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Created 'data' directory.")
    
    for name, url in datasets.items():
        path = os.path.join('data', name)
        if not os.path.exists(path):
            print(f"Downloading {name}...")
            try:
                response = requests.get(url)
                response.raise_for_status()
                with open(path, 'wb') as f:
                    f.write(response.content)
                print(f"Saved {name}.")
            except Exception as e:
                print(f"Failed to download {name}: {e}")
        else:
            print(f"{name} already exists.")

if __name__ == "__main__":
    download_data()
