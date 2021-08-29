import requests
url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"https://developers.whatismybrowser.com/useragents/parse/?analyse-my-user-agent=yes"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html", "w", encoding="utf8") as f:
    f.write(res.text)