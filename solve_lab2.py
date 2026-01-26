
import pandas as pd
import numpy as np

def solve_lab2():
    # Load dataset
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv"
    df = pd.read_csv(url)
    
    # Q1: ¿Cuántos lanzamientos salieron del CCAFS SLC 40?
    # Count launches by site
    q1_ans = df['LaunchSite'].value_counts()['CCAFS SLC 40']
    print(f"Pregunta 1: {q1_ans}")
    
    # Q3: ¿Cuántos lanzamientos fueron a la órbita geosíncrona? (GTO)
    q3_ans = df['Orbit'].value_counts()['GTO']
    print(f"Pregunta 3: {q3_ans}")
    
    # Q4: ¿Cuántas veces se ha conseguido aterrizar en una nave no tripulada?
    # Drone ship = ASDS (Autonomous Spaceport Drone Ship)
    # Successful landing = True ASDS
    q4_ans = df['Outcome'].value_counts()['True ASDS']
    print(f"Pregunta 4: {q4_ans}")

    # Q2: ¿Cuál fue la tasa de éxito?
    # Create Class column
    # Success = True Ocean, True RTLS, True ASDS
    success_outcomes = {'True Ocean', 'True RTLS', 'True ASDS'}
    
    landing_class = []
    for outcome in df['Outcome']:
        if outcome in success_outcomes:
            landing_class.append(1)
        else:
            landing_class.append(0)
            
    df['Class'] = landing_class
    success_rate = df['Class'].mean()
    print(f"Pregunta 2: {success_rate:.2%}")

if __name__ == "__main__":
    solve_lab2()
