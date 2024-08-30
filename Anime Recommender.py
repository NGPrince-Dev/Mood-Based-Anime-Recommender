import requests
from random import choice

def main():
    """
    Asks the user how they're feeling and recommends an anime based on their mood.

    Example:
    >>> main()
    How are you feeling right now?
    1. Happy
    2. Sad
    3. Excited
    4. Curious
    Enter the number of your choice: 1
    Based on you being happy, I recommend you watch Great Teacher Onizuka!
    """
    print("How are you feeling right now?", "1. Happy", "2. Sad", "3. Excited", "4. Curious", sep="\n")
    select = input("Enter the number of your choice: ").strip()

    if select in ["1", "2", "3", "4"]:
        if select == "1":
            mood = "happy"
        elif select == "2":
            mood = "sad"
        elif select == "3":
            mood = "excited"
        else:
            mood = "curious"
        
        database = pick(select)
        print(f"Based on you being {mood}, I recommend you watch {database['title']}!")
    else:
        print("Unfortunately, the value you typed doesn't have a designated mood yet. Please select one of the moods from the options.")

def pick(select):
    """
    Picks a random anime from the Jikan API based on the user's mood.

    Args:
        select (str): The user's mood selection (1, 2, 3, or 4)

    Returns:
        dict: A dictionary containing the title of the recommended anime

    Example:
    >>> pick("1")
    {'title': 'One Punch Man'}
    """
    api_url = "https://api.jikan.moe/v4/anime"

    parame = {
        "genre": "",
        "order_by": "popularity",
        "sort": "desc",
        "limit": 10
    }
    
    if select == "1" or select == "3":
        parame["genre"] = choice(["action", "comedy"])
    elif select == "2":
        parame["genre"] = choice(["romance", "drama"])
    else:
        parame["genre"] = "drama"
    
    response = requests.get(api_url, params=parame)
    data = response.json()

    if response.status_code == 200:
        anime_list = data["data"]
        random_anime = choice(anime_list)
        return {"title": random_anime["title"]}
    else:
        return {"title": "Unfortunately, the API request failed. Please try again later."}

if __name__ == "__main__":
    main()
