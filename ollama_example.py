import requests
import json

url = "http://localhost:11434/api/generate"

payload = json.dumps({
  "model": "llama2",
  "prompt": "what is python?",
  "stream": False
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)