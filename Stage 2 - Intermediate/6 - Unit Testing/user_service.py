import requests


def get_user(user_id):
    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    data = res.json()
    return {"name": data["name"], "email": data["email"]}


def get_post_title(post_id):
    res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    if res.status_code != 200:
        raise ConnectionError("failed to fetch post")
    return res.json()["title"]


def send_notification(email, msg):
    print(f"sending '{msg}' to {email}")
    return True
