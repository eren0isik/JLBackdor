import requests

def download_file(url, destination):
    """
    Download a file from the given URL and save it to the specified destination.
    """
    try:
        with requests.get(url, stream=True) as response:
            response.raise_for_status()  # Raise an exception for HTTP errors
            with open(destination, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        print(f"File downloaded successfully: {destination}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage
#file_url = "https://example.com/file.zip"
#save_path = "file.zip"
#download_file(file_url, save_path)
