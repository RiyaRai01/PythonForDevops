import requests
import json
import argparse
import logging
import time

# url = "https://api.github.com/repos/kubernetes/kubernetes"
api_retries = 2
api_timeout = 5

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def fetch_repo_data(url,api_retries=api_retries):
    for retry in range(1, api_retries+1):
        try:
            response = requests.get(url, timeout=api_timeout)
            response.raise_for_status()
            try:
                return response.json()
            except ValueError:
                logging.error(
                    "Response is not valid JSON. Please check the API URL."
                )
                
        except requests.exceptions.RequestException as error:
            logging.warning(f"Attempt {retry} - Error fetching data from API: {error}")
            time.sleep(2)
        logging.error(f"API failed after {retry} attempts.")
        return None

def process_data(data):
        usefull_data = {
        "id" : data["id"],
        "node_id" : data["node_id"],
        "full name" : data["full_name"],
        "subscribers_count" : data["subscribers_count"],
        }
        return usefull_data
    
def save_to_file(data, filename): 
    with open(filename, "w") as output_file:
        json.dump(data,output_file, indent=4) 
    logging.info(f"Data saved to {filename}")  

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch and process GitHub repository data.")
    parser.add_argument("--url", required=True, help="GitHub repository API URL")
    parser.add_argument("--output", default="output.json", help="Output filename")
    return parser.parse_args()
        
def main():
    args = parse_arguments()
    
    logging.info("Fetching data from GitHub API...")
    repo_data = fetch_repo_data(args.url)
    if repo_data is None:
        logging.info("Exiting safely due to API failure.")
        return
    
    logging.info("Processing data...")
    processed_data = process_data(repo_data)
    logging.info(processed_data)
    
    logging.info("Saving data to file...")
    save_to_file(processed_data, args.output)    
    
if __name__ == "__main__":
    main()
    




    
        
    

