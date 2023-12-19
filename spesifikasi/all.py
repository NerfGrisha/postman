import requests

BASE_URL = "http://localhost:8080"  # Update the port if needed

def show_menu():
    print("Menu:")
    print("1. GET data")
    print("2. POST data")
    print("3. PUT data")
    print("4. DELETE data")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    return choice

def print_matrix(data):
    print("Raw data:")
    print(data)  # Print raw data for debugging

    if not data:
        print("No data available.")
        return

    if isinstance(data, list) and data and isinstance(data[0], dict):
        # Print header
        header = list(data[0].keys())
        print("\t".join(header))

        # Print data
        for row in data:
            values = [str(row[key]) for key in header]
            print("\t".join(values))
    else:
        print("wes ketok gan")

def get_data():
    response = requests.get(f"{BASE_URL}/showdata")
    if response.status_code == 200:
        try:
            data = response.json()
            print_matrix(data)
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
    else:
        print(f"Error: {response.status_code} - {response.text}")

def post_data():
    laptop_id = input("Enter laptop_id: ")
    processor = input("Enter processor: ")
    RAM = input("Enter RAM: ")
    penyimpanan = input("Enter penyimpanan: ")

    payload = {
        "laptop_id": laptop_id,
        "processor": processor,
        "RAM": RAM,
        "penyimpanan": penyimpanan
    }

    response = requests.post(f"{BASE_URL}/add", data=payload)
    print(response.text)

def put_data():
    spesifikasi_id_data = input("Enter the spesifikasi_id to update: ")

    # Fetch existing data to display
    response = requests.get(f"{BASE_URL}/showdata?spesifikasi_id={spesifikasi_id_data}")
    if response.status_code == 200:
        data = response.json()
        print("Existing data:")
        print_matrix(data)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return

    # Get updated values
    laptop_id = input("Enter new laptop_id (press Enter to keep the existing value): ")
    processor = input("Enter new processor (press Enter to keep the existing value): ")
    RAM = input("Enter new RAM (press Enter to keep the existing value): ")
    penyimpanan = input("Enter new penyimpanan (press Enter to keep the existing value): ")

    # Prepare payload with updated values
    payload = {"spesifikasi_id": spesifikasi_id_data}
    if laptop_id:
        payload["laptop_id"] = laptop_id
    if processor:
        payload["processor"] = processor
    if RAM:
        payload["RAM"] = RAM
    if penyimpanan:
        payload["penyimpanan"] = penyimpanan

    # Send PUT request
    response = requests.put(f"{BASE_URL}/edit", params=payload)
    print(response.text)

def delete_data():
    spesifikasi_id = input("Enter the spesifikasi_id to delete: ")
    response = requests.delete(f"{BASE_URL}/delete?spesifikasi_id={spesifikasi_id}")
    print(response.text)

if __name__ == "__main__":
    while True:
        choice = show_menu()

        if choice == "1":
            get_data()
        elif choice == "2":
            post_data()
        elif choice == "3":
            put_data()
        elif choice == "4":
            delete_data()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
