import requests
import json

url = "https://api.github.com/repos/kubernetes/kubernetes"

def fetch_repo_data(url):
    response = requests.get(url)
    return response.json()

def process_data(data):
        usefull_data = {
        "id" : data["id"],
        "node_id" : data["node_id"],
        "full name" : data["full_name"],
        "subscribers_count" : data["subscribers_count"],
        }
        return usefull_data
    
def save_to_file(data, filename="output.json"): 
    with open(filename, "w") as output_file:
        json.dump(data,output_file, indent=4) 
    print(f"Data saved to {filename}")  
    
def main():
    print("Fetching data from GitHub API...")
    repo_data = fetch_repo_data(url)
    print(repo_data)
    
    print("\nProcessing data...")
    processed_data = process_data(repo_data)
    print(processed_data)
    
    print("\nSaving data to file...")
    save_to_file(processed_data)    
    
if __name__ == "__main__":
    main()
    




    
        
    

