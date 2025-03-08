import requests
import json

def vin_lookup(vin):
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValuesBatch/"
    params = {"format": "json", "data": vin}
    
    try:
        response = requests.post(url, data=params)
        response.raise_for_status()
        data = response.json()
        results = data.get("Results", [])[0]
        
        if not results:
            print("No data found for the provided VIN.")
            return
        
        print("VIN Lookup Results:")
        print(f"VIN: {results.get('VIN', 'N/A')}")
        print(f"Make: {results.get('Make', 'N/A')}")
        print(f"Model: {results.get('Model', 'N/A')}")
        print(f"Model Year: {results.get('ModelYear', 'N/A')}")
        print(f"Body Class: {results.get('BodyClass', 'N/A')}")
        print(f"Drive Type: {results.get('DriveType', 'N/A')}")
        print(f"Engine Configuration: {results.get('EngineConfiguration', 'N/A')}")
        print(f"Engine Cylinders: {results.get('EngineCylinders', 'N/A')}")
        print(f"Fuel Type: {results.get('FuelTypePrimary', 'N/A')}")
    
    except requests.RequestException as e:
        print(f"Error retrieving VIN data: {e}")

if __name__ == "__main__":
    vin = input("Enter VIN #: ").strip()
    if vin:
        vin_lookup(vin)
    else:
        print("Invalid VIN input.")
