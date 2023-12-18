import requests

base_url = "http://127.0.0.1:8080"  

delete_data = {'spesifikasi_id': input("Enter Spesifikasi ID to Delete: ")}
delete_response = requests.delete(f"{base_url}/delete", params=delete_data)
print("Delete Response:", delete_response.json())
