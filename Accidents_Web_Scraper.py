import requests
import numpy as np
import pandas as pd

# NHTSA Crash API endpoint
base_url = 'https://crashviewer.nhtsa.dot.gov/CrashAPI/'


def accident_information_api(year1, year2):
    accidents_api = 'crashes/GetCaseList?states=1,51&fromYear='+ str(year1) +'&toYear='+ str(year2) +'&minNumOfVehicles=1&maxNumOfVehicles=6&format=json'
    temp = pd.DataFrame()
    try:
        response = requests.get(base_url + accidents_api)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            crash_data = response.json()
            # Process the crash data as needed
            datalist = crash_data['Results'][0]
            for index in range(len(datalist)):
                print('Accident Data fetched for: '+str(index)+'/'+str(len(datalist)))
                temp = pd.concat([temp, pd.DataFrame(datalist[index], index = [index])])
        else:
            print(f"Error: {response.status_code}, {response.text}")
        print(temp.head(40))
        return temp

    except Exception as e:
        print(f"An error occurred: {e}")

def accident_by_vehicle_api(year1, year2):
    accidents_api = 'crashes/GetCrashesByVehicle?make=6&model=41&bodyType=4&fromCaseYear='+ str(year1) +'&toCaseYear='+ str(year2) +'&state=21&format=json'
    temp = pd.DataFrame()
    try:
        response = requests.get(base_url + accidents_api)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            crash_data = response.json()
            # Process the crash data as needed
            datalist = crash_data['Results'][0]
            for index in range(len(datalist)):
                # print(str(index)+'/'+str(len(datalist)))
                temp = pd.concat([temp, pd.DataFrame(datalist[index], index = [index])])
        else:
            print(f"Error: {response.status_code}, {response.text}")
        return temp

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    info = pd.DataFrame()
    vehicle = pd.DataFrame()
    nums = [2014, 2019, 2024]
    for year in nums:
        temp = accident_information_api(year, year+5)
        info = pd.concat([info, temp])

        # temp = accident_information_api(year, year + 5)
        # vehicle = pd.concat([vehicle, temp])
    info.to_csv('DataSet/Accidents_List_Information.csv', index = False)
