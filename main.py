import requests
from bs4 import BeautifulSoup

page = 1
previous_title = ""
while True:
    end = False
    url = "https://comic.naver.com/webtoon/list?titleId=183559&page=" + str(page)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    cartoons = soup.find_all("td", attrs={"class": "title"})
    scores = soup.find_all("div", attrs={"class": "rating_type"})

    rates = []
    for score in scores:
        rates.append(score.find("strong").get_text())

    for score, cartoon in enumerate(cartoons):
        title = cartoon.a.get_text()
        link = "https://comic.naver.com" + cartoon.a["href"]

        if title == previous_title:
            end = True
            break
        print(f"Title is {title} and Score is {rates[score]} / {page} page.")
        print(f"Quick Link : {link}\n")
        previous_title = title
    page += 1
    if end:
        break
