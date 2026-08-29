import requests
from bs4 import BeautifulSoup
import json
import os

DIR = os.path.dirname(os.path.abspath(__file__))
URL = "https://www.python.org/"
HEADERS = {"User-Agent": "Mozilla/5.0"}

# ---- requests basics ----

# simple get request
res = requests.get(URL)
print(res.status_code)
print(res.text[:300])


# check status code
if res.status_code == 200:
    print("success")
else:
    print("failed")


# error handling
try:
    res = requests.get(URL, timeout=10)
    res.raise_for_status()
    print("ok:", res.status_code)
except requests.exceptions.RequestException as e:
    print("error:", e)


# request with headers (user-agent)
res = requests.get(URL, headers=HEADERS)
print(res.status_code)


# query parameters (example: python.org search)
params = {"q": "decorator"}
r = requests.get("https://www.python.org/search/", params=params, headers=HEADERS)
print(r.url)


# ---- beautifulsoup basics ----

res = requests.get(URL, headers=HEADERS)
soup = BeautifulSoup(res.text, "html.parser")


with open(os.path.join(DIR, "python_org.html"), "w", encoding="utf-8") as f:
    f.write(soup.prettify())

# page title
print(soup.title.text.strip())


# find single element - first h1
h1 = soup.find("h1")
print(h1.text.strip() if h1 else "no h1")


# find all - all links on page
all_links = soup.find_all("a")
print(f"total links on page: {len(all_links)}")


# find by class
download_widget = soup.find("div", class_="download-widget")
print(download_widget.get_text(strip=True)[:100])


# find by id
nav = soup.find(id="touchnav-wrapper")
print("nav found:", nav is not None)


# css selector - single
intro = soup.select_one(".introduction p")
if intro:
    print(intro.get_text(strip=True)[:150])


# css selector - all nav links
print("\nmain nav links:")
for li in soup.select(".navigation.menu > li"):
    a = li.find("a")
    if a and a.get("href", "").startswith("/") and len(a.get_text(strip=True)) > 2:
        print(" ", a.get_text(strip=True), "->", a.get("href"))


# extract links (href attribute)
print("\nall external links (first 5):")
for a in soup.find_all("a", href=True)[:20]:
    href = a.get("href")
    if href.startswith("http"):
        print(" ", a.get_text(strip=True)[:40], "->", href)


# ---- scraping actual data from python.org ----

# 1. latest python download version
dl_link = soup.find("div", class_="download-widget").find("a")
print("\nlatest python:")
print(" version:", dl_link.get_text(strip=True))
print(" link: https://www.python.org" + dl_link.get("href"))


# 2. latest news
print("\nlatest news:")
news = []
for li in soup.find("div", class_="blog-widget").find("div", class_="shrubbery").find_all("li"):
    a = li.find("a")
    time_tag = li.find("time")
    if a:
        title = a.get_text(strip=True)
        href = a.get("href")
        date = time_tag.get("datetime", "")[:10] if time_tag else ""
        news.append({"title": title, "href": href, "date": date})
        print(f"  [{date}] {title}")


# 3. upcoming events
print("\nupcoming events:")
events = []
for li in soup.find("div", class_="event-widget").find("div", class_="shrubbery").find_all("li"):
    a = li.find("a")
    time_tag = li.find("time")
    if a:
        name = a.get_text(strip=True)
        href = a.get("href")
        date = time_tag.get_text(strip=True) if time_tag else ""
        events.append({"event": name, "href": href, "date": date})
        print(f"  [{date}] {name}")


# 4. python use cases / applications
print("\npython applications:")
apps = []
for li in soup.find("div", class_="applications-widget").find("ul").find_all("li"):
    text = li.get_text(strip=True)
    apps.append(text)
    print(" ", text[:80])


# ---- save scraped data to json ----

data = {
    "latest_version": dl_link.get_text(strip=True),
    "news": news,
    "events": events,
    "applications": apps,
}

with open(os.path.join(DIR, "python_org_data.json"), "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

print("\nsaved to python_org_data.json")
