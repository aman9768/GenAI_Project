from dotenv import load_dotenv
import os

#calling the API key
load_dotenv()
GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
print(GOOGLE_API_KEY)

