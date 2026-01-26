import sqlite3
import pandas as pd
import os

def run_sql_analysis():
    if not os.path.exists('assets/sql'):
        os.makedirs('assets/sql')
        print("Created 'assets/sql' directory.")

    # Load data
    df = pd.read_csv('data/Spacex.csv')
    
    # Create database
    con = sqlite3.connect("spacex.db")
    df.to_sql("SPACEXDATASET", con, if_exists='replace', index=False, method="multi")
    
    # helper to run and save query
    results_file = open('assets/sql/results.txt', 'w')
    
    def run_query(title, query):
        print(f"Running: {title}")
        results_file.write(f"--- {title} ---\n")
        results_file.write(f"Query: {query}\n\n")
        try:
            res = pd.read_sql(query, con)
            results_file.write(res.to_string())
        except Exception as e:
            results_file.write(f"Error: {e}")
        results_file.write("\n\n" + "="*50 + "\n\n")

    # Queries from the lab
    run_query("Distinct Launch Sites", "SELECT DISTINCT Launch_Site FROM SPACEXDATASET")
    
    run_query("Launch Sites beginning with 'CCA'", "SELECT * FROM SPACEXDATASET WHERE Launch_Site LIKE 'CCA%' LIMIT 5")
    
    run_query("Total Payload Mass by NASA (CRS)", "SELECT SUM(PAYLOAD_MASS__KG_) FROM SPACEXDATASET WHERE Customer = 'NASA (CRS)'")
    
    run_query("Avg Payload Mass for F9 v1.1", "SELECT AVG(PAYLOAD_MASS__KG_) FROM SPACEXDATASET WHERE Booster_Version LIKE 'F9 v1.1%'")
    
    run_query("Date of First Successful Landing", "SELECT MIN(Date) FROM SPACEXDATASET WHERE Landing_Outcome = 'Success (ground pad)'")
    
    run_query("Boosters with Success (drone ship) and Payload 4000-6000", 
              "SELECT Booster_Version FROM SPACEXDATASET WHERE Landing_Outcome = 'Success (drone ship)' AND PAYLOAD_MASS__KG_ BETWEEN 4000 AND 6000")
    
    run_query("Total Items and Success/Failure Outcomes", 
              "SELECT Landing_Outcome, COUNT(Landing_Outcome) FROM SPACEXDATASET GROUP BY Landing_Outcome")
    
    run_query("Boosters with Max Payload Mass", 
              "SELECT Booster_Version FROM SPACEXDATASET WHERE PAYLOAD_MASS__KG_ = (SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEXDATASET)")
    
    # Note: Date extraction might depend on date format in CSV. Assuming ISO or standard.
    # CSV dates usually DD-MM-YYYY or YYYY-MM-DD. Let's check format or just use substr if consistent.
    # The lab used: substr(Date, 6, 2) since format was YYYY-MM-DD or DD-MM-YYYY.
    # Inspecting data usually required but here we'll try standard SQL substr.
    # Assuming YYYY-MM-DD: Month is substr(Date, 6, 2).
    
    run_query("Failed Landing Outcomes in 2015", 
              "SELECT substr(Date, 6, 2) as Month, 'F9 v1.1' as Booster_Version, Launch_Site FROM SPACEXDATASET WHERE substr(Date,0,5)='2015' AND Landing_Outcome = 'Failure (drone ship)'")
    
    run_query("Rank Landing Outcomes (2010-06-04 to 2017-03-20)", 
              "SELECT Landing_Outcome, COUNT(Landing_Outcome) as Count FROM SPACEXDATASET WHERE Date BETWEEN '2010-06-04' AND '2017-03-20' GROUP BY Landing_Outcome ORDER BY Count DESC")

    results_file.close()
    con.close()
    print("SQL Analysis complete. Results in assets/sql/results.txt")

if __name__ == "__main__":
    run_sql_analysis()
