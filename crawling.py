import requests
from bs4 import BeautifulSoup
import trafilatura
from transformers import pipeline

#pip install -r requirements.txt //install

url = input("내용을 요약하고 싶은 뉴스의 url을 입력해 주세요. :")
print(url)

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

headline_h1 = soup.find("title")
if headline_h1:
    headline = headline_h1.get_text(strip=True)

downloaded = trafilatura.fetch_url(url)

text = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        include_images=False,
        favor_recall=True, 
        output_format="txt"
    )

min_len = 20
max_len = 130
if len(text) < 200:
    min_len = 10
    max_len = 80

summarizer = pipeline("summarization", model = "gogamza/kobart-summarization")
summary = summarizer(text, max_length=max_len, min_length=5, do_sample=False)


print("==================================================")
print("헤드라인 = ", headline)
print("본문 = ", text)
print("본문 요약 = ", summary[0]['summary_text'])
print("==================================================")