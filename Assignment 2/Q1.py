import requests

def get_api_url():
    try:
        with open("api.txt", 'r') as f:
            api_url = f.readline().strip()
            if not api_url:
                print("api.txt is empty")
                return None
            return api_url

    except FileNotFoundError:
        print("File not found")
        return None

    except Exception as e:
        print("Error: ", e)
        return None


def fetch_live_matches(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code != 200:
            print("Error: Received status code ", response.status_code)
            print("Response: ", response.text)
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Network error")
        print("Details: ", e)
        return None


def print_api_status(data):
    if not data:
        print("No API data to display")
        return

    for key, value in data.items():
        if key not in ["data", "apikey"]:
            print(key, ":", value)


def get_match_details(api_url):
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()  

            if data.get("status") == "success" and "data" in data and data["data"]:
                match_list = data["data"]

                for match in match_list:
                    print("Match:", match.get('name', 'N/A'))
                    print("Status:", match.get('status', 'N/A'))
                    print("Venue:", match.get('venue', 'N/A'))
                    print("Date:", match.get('date', 'N/A'))
                    print("-" * 30)

                    scores = match.get("score", [])
                    if scores:
                        print(" Score Details:")
                        for inning in scores:
                            print(f"  Inning : {inning.get('inning', 'N/A')}")
                            print(f"  Runs   : {inning.get('r', 'N/A')}")
                            print(f"  Wickets: {inning.get('w', 'N/A')}")
                            print(f"  Overs  : {inning.get('o', 'N/A')}")
                            print("  " + "-" * 25)
                    else:
                        print("No score details available.")
                        print("-" * 30)
            else:
                print("No live matches found or an unknown error occurred.")

        else:
            print("Error, failed to fetch data. Status code:", response.status_code)
            print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print("Network error occurred:", e)

url = get_api_url()
print("Api url:", url)

if url:
    data = fetch_live_matches(url)
    if data is None:
        print("Unable to retrieve data from API")
    else:
        print_api_status(data)
        get_match_details(url)
else:
    print("No API URL found. Please check api.txt.")
