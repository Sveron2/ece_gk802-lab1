import requests
from datetime import datetime


def fetch_server_status(url):
    try:

        response = requests.head(url, timeout=5)
        server_software = response.headers.get('Server', 'N/A')
        print(f"Server Software: {server_software}")

        cookies = response.cookies
        if cookies:
            print("Cookies: ")
            for cookie in cookies:
                print(f'Name: {cookie.name}', end="\t")

                if cookie.expires:
                    expires = datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d')
                    print(f'Expires: {expires}', end="\t")
                print("headers: ", response.headers)
        else:
            print("No cookies found.")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def main():
    url = input("Enter a URL: ")
    fetch_server_status(url)

if __name__ == "__main__":
    main()
