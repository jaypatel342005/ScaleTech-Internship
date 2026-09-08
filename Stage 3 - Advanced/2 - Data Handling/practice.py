import requests
import pandas as pd

# practice - fetch todos from api, clean data, find completion rate per user

def get_data(url):
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.RequestException as e:
        print("error:", e)
        return []


todos_data = get_data("https://jsonplaceholder.typicode.com/todos")
users_data = get_data("https://jsonplaceholder.typicode.com/users")

if not todos_data:
    print("no data")
    exit()

df = pd.DataFrame(todos_data)
users_df = pd.DataFrame(users_data)

print(df.shape)
print(df.head())

# clean
df.drop_duplicates(inplace=True)
df["title"] = df["title"].fillna("unknown")

# count total and done per user
total = df.groupby("userId")["id"].count().rename("total")
done = df[df["completed"]].groupby("userId")["id"].count().rename("done")

summary = pd.concat([total, done], axis=1).fillna(0)
summary["rate_%"] = (summary["done"] / summary["total"] * 100).round(1)
summary = summary.reset_index()

# add user name from users api
users_slim = users_df[["id", "name"]].rename(columns={"id": "userId"})
summary = pd.merge(summary, users_slim, on="userId", how="left")

print(summary.sort_values("rate_%", ascending=False))

summary.to_csv("todo_report.csv", index=False)
print("saved todo_report.csv")



