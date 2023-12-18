import requests

base_url = "http://127.0.0.1:8080"  

def get_user_input():
    return {'spesifikasi_id': input("Enter Spesifikasi ID to Show: ")}

show_data = get_user_input()
show_response = requests.get(f"{base_url}/showdata", params=show_data)
print("Show Data Response:", show_response.json())
