import requests

def get_characters(movie_id):
    url = f"https://swapi.dev/api/films/{movie_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        characters = data["characters"]
        for character in characters:
            print(character["name"])
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    movie_id = int(input("Enter the movie ID: "))
    get_characters(movie_id)
