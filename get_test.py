import requests

input_get={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

header = {'accept': 'application/json'}
res = requests.post(f"https://petstore.swagger.io/v2/get", params=input_get, headers=header)

print(res.status_code)
print(res.text)
print(res.json())
print(type(res.json()))