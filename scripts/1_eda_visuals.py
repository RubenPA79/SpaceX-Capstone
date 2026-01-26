import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def create_eda_visuals():
    if not os.path.exists('assets/eda'):
        os.makedirs('assets/eda')
        print("Created 'assets/eda' directory.")

    # Load dataset
    df = pd.read_csv('data/dataset_part_2.csv')

    # Set style
    sns.set_theme(style="whitegrid")

    # 1. Flight Number vs. Payload Mass
    plt.figure(figsize=(12, 6))
    sns.catplot(y="PayloadMass", x="FlightNumber", hue="Class", data=df, aspect=3)
    plt.xlabel("Flight Number", fontsize=20)
    plt.ylabel("Pay load Mass (kg)", fontsize=20)
    plt.title("Flight Number vs Payload Mass", fontsize=20)
    plt.savefig('assets/eda/1_flight_vs_payload.png', bbox_inches='tight')
    plt.close()
    print("Generated 1_flight_vs_payload.png")

    # 2. Flight Number vs. Launch Site
    plt.figure(figsize=(12, 6))
    sns.catplot(y="LaunchSite", x="FlightNumber", hue="Class", data=df, aspect=3)
    plt.xlabel("Flight Number", fontsize=20)
    plt.ylabel("Launch Site", fontsize=20)
    plt.title("Flight Number vs Launch Site", fontsize=20)
    plt.savefig('assets/eda/2_flight_vs_site.png', bbox_inches='tight')
    plt.close()
    print("Generated 2_flight_vs_site.png")

    # 3. Payload Mass vs. Launch Site
    plt.figure(figsize=(12, 6))
    sns.catplot(y="LaunchSite", x="PayloadMass", hue="Class", data=df, aspect=3)
    plt.xlabel("Payload Mass (kg)", fontsize=20)
    plt.ylabel("Launch Site", fontsize=20)
    plt.title("Payload Mass vs Launch Site", fontsize=20)
    plt.savefig('assets/eda/3_payload_vs_site.png', bbox_inches='tight')
    plt.close()
    print("Generated 3_payload_vs_site.png")

    # 4. Success Rate by Orbit (Bar Chart)
    orbit_success = df.groupby('Orbit')['Class'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Orbit", y="Class", data=orbit_success, hue='Orbit', palette='viridis', legend=False)
    plt.xlabel("Orbit", fontsize=20)
    plt.ylabel("Success Rate", fontsize=20)
    plt.title("Success Rate by Orbit", fontsize=20)
    plt.savefig('assets/eda/4_success_by_orbit.png', bbox_inches='tight')
    plt.close()
    print("Generated 4_success_by_orbit.png")

    # 5. Flight Number vs. Orbit
    plt.figure(figsize=(12, 6))
    sns.catplot(y="Orbit", x="FlightNumber", hue="Class", data=df, aspect=3)
    plt.xlabel("Flight Number", fontsize=20)
    plt.ylabel("Orbit", fontsize=20)
    plt.title("Flight Number vs Orbit", fontsize=20)
    plt.savefig('assets/eda/5_flight_vs_orbit.png', bbox_inches='tight')
    plt.close()
    print("Generated 5_flight_vs_orbit.png")

    # 6. Payload Mass vs. Orbit
    plt.figure(figsize=(12, 6))
    sns.catplot(y="Orbit", x="PayloadMass", hue="Class", data=df, aspect=3)
    plt.xlabel("Payload Mass (kg)", fontsize=20)
    plt.ylabel("Orbit", fontsize=20)
    plt.title("Payload Mass vs Orbit", fontsize=20)
    plt.savefig('assets/eda/6_payload_vs_orbit.png', bbox_inches='tight')
    plt.close()
    print("Generated 6_payload_vs_orbit.png")

    # 7. Yearly Success Trend
    # Extract year
    year = []
    def Extract_year(date):
        for i in df["Date"]:
            year.append(i.split("-")[0])
        return year
    
    Extract_year(df["Date"])
    df['Year'] = year
    
    yearly_avg = df.groupby('Year')['Class'].mean().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x="Year", y="Class", data=yearly_avg)
    plt.xlabel("Year", fontsize=20)
    plt.ylabel("Success Rate", fontsize=20)
    plt.title("Yearly Success Trend", fontsize=20)
    plt.savefig('assets/eda/7_yearly_trend.png', bbox_inches='tight')
    plt.close()
    print("Generated 7_yearly_trend.png")

if __name__ == "__main__":
    create_eda_visuals()
