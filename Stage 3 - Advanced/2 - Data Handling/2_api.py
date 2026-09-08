import requests
import json
import os

# requests library is used to call apis from python
# install: pip install requests


url = "https://jsonplaceholder.typicode.com"


# get - fetch data
response = requests.get(f"{url}/users/1")
print(response.status_code)   # 200 = ok

data = response.json()
print(data["name"])
print(data["email"])


# get a list
response = requests.get(f"{url}/users")
users = response.json()
for u in users:
    print(u["id"], u["name"])


# query params
params = {"userId": 1}
response = requests.get(f"{url}/posts", params=params)
posts = response.json()
print(f"posts by user 1: {len(posts)}")


# headers - used for auth, content type etc
headers = {"Accept": "application/json"}
response = requests.get(f"{url}/users", headers=headers)
print(response.status_code)


# status codes
# 200 ok  201 created  204 no content
# 400 bad request  401 unauthorized  403 forbidden  404 not found
# 500 server error


# json module
raw = '{"name": "Jay", "age": 21}'
parsed = json.loads(raw)           # string to dict
back = json.dumps(parsed, indent=2) # dict to string
print(parsed["name"])


# post - create
new_post = {"title": "my post", "body": "some content", "userId": 1}
response = requests.post(f"{url}/posts", json=new_post)
print(response.status_code)   # 201
print(response.json())


# put - replace whole thing
updated = {"id": 1, "title": "new title", "body": "new body", "userId": 1}
response = requests.put(f"{url}/posts/1", json=updated)
print(response.json())


# patch - update one field only
response = requests.patch(f"{url}/posts/1", json={"title": "only title"})
print(response.json())


# delete
response = requests.delete(f"{url}/posts/1")
print(response.status_code)   # 200


# authentication - use env variable not hardcode
api_key = os.getenv("API_KEY", "demo_key")
headers = {"Authorization": f"Bearer {api_key}"}
# response = requests.get("https://some-api.com/data", headers=headers)


# error handling - always wrap in try except
try:
    response = requests.get(f"{url}/posts/1", timeout=10)
    response.raise_for_status()
    data = response.json()
    print(data["title"])
except requests.exceptions.HTTPError as e:
    print("http error:", e)
except requests.exceptions.ConnectionError:
    print("no connection")
except requests.exceptions.Timeout:
    print("timed out")
except requests.exceptions.RequestException as e:
    print("error:", e)


# checking status manually
response = requests.get(f"{url}/posts/999")
if response.status_code == 200:
    print(response.json())
elif response.status_code == 404:
    print("not found")
elif response.status_code == 401:
    print("need to login")
elif response.status_code >= 500:
    print("server problem")


# response properties
response = requests.get(f"{url}/posts/1")
print(response.status_code)
print(response.url)
print(response.text[:100])
print(response.json())



# rest conventions
# GET    /posts       - get all
# GET    /posts/1     - get one
# POST   /posts       - create
# PUT    /posts/1     - replace
# PATCH  /posts/1     - partial update
# DELETE /posts/1     - delete
