import requests

def fetch_api_data():
    api_url = "https://api.restful-api.dev/objects" 
    response = requests.get(url=api_url)
    
    datalist = response.json()
    
    for item in datalist:
        for key, value in item.items():
            if key == "name":
                continue
            else:
                print(key,value)
    
fetch_api_data()


        
    

