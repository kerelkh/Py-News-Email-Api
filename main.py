import dotenv
import requests
import os

dotenv.load_dotenv()

query = os.getenv("WEB_APP") + "/v2/everything?q=" + "testla" + "&apiKey=" + os.getenv("API_KEY")

request = requests.get(query)

result = request.json()

if result["status"] == "ok":
    article = result["articles"][0]
    print(article["title"])
    print(article["description"])
    print(article["url"])