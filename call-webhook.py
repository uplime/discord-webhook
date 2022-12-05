import os
import requests

api_key = os.getenv("INPUT_API-KEY")

if api_key is None:
  print(">>>>>>>>>>> got in here")
  api_key = os.getenv("INPUT_API_KEY")

print(api_key)
