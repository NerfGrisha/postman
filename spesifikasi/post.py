import requests

base_url = "http://127.0.0.1:8080"  

def get_user_input():
    return {
        'laptop_id': input("Enter Laptop ID: "),
        'processor': input("Enter Processor: "),
        'RAM': input("Enter RAM: "),
        'penyimpanan': input("Enter Penyimpanan: ")
    }

sample_data = get_user_input()
add_response = requests.post(f"{base_url}/add", data=sample_data)
print("Add Response:", add_response.json())
