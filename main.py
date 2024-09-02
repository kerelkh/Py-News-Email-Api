import dotenv
import requests
import os
from send_email import send_email

dotenv.load_dotenv()

query = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=" + os.getenv("API_KEY")

request = requests.get(query)

result = request.json()

if result["status"] == "ok":
    article = result["articles"][0]
    send_email(article)
else:
    print("Response have no result")
