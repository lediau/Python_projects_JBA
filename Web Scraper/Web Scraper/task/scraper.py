import os
import requests
import string
from bs4 import BeautifulSoup

HOST = "https://www.nature.com"
number_of_pages = int(input())
article_type = input()


def get_html(url):
    r = requests.get(url)
    return r


# search links we need
def get_content(html, number):
    soup = BeautifulSoup(html.content, "html.parser")
    articles = soup.find_all("article")
    for article in articles:
        if article.find("span", class_="c-meta__type").text == article_type:
            link_of_article = HOST + article.find("a").get("href")  # getting links to the articles we need
            second_part(link_of_article, number)


def second_part(link, number):
    req_link = requests.get(link)  # request for the links we need
    s = BeautifulSoup(req_link.content, "html.parser")
    #           === getting titles and body of each article ===
    title_of_article = s.find("h1", class_="c-article-magazine-title").text.strip()
    body_of_article = s.find("div", class_="c-article-body").text.strip()
    #    === Rename of article's title and save it into a list ===
    title_of_article = title_of_article.translate(str.maketrans('', '', string.punctuation))
    title_of_article = title_of_article.replace(" ", "_")
    create_txt(title_of_article, body_of_article, number)


def create_txt(title, body, number):
    #      === Creating a text file and writing the body of the article into it ===
    txt_file = open(fr"{os.getcwd()}\Page_{number}\{title}.txt", "wb")
    txt_file.write(body.encode("UTF-8"))
    txt_file.close()


def parse():
    for number in range(1, number_of_pages + 1):
        os.mkdir(f"Page_{number}")
        URL = f"https://www.nature.com/nature/articles?searchType=journalSearch&sort=PubDate&year=2020&page={number}"
        html = get_html(URL)
        if html.status_code == 200:
            get_content(html, number)
    print("Saved all articles.")


parse()
