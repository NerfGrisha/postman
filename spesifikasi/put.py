import requests

base_url = "http://127.0.0.1:8080"  

def get_user_input():
    return {
        'spesifikasi_id': input("Enter Spesifikasi ID to Edit: "),
        'laptop_id': input("Enter Laptop ID: "),
        'processor': input("Enter Processor: "),
        'RAM': input("Enter RAM: "),
        'penyimpanan': input("Enter Penyimpanan: ")
    }

edit_data = get_user_input()
edit_response = requests.put(f"{base_url}/edit", params=edit_data)
print("Edit Response:", edit_response.json())
