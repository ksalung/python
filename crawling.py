import requests
from bs4 import BeautifulSoup
import trafilatura
from transformers import pipeline


url = "https://www.metroseoul.co.kr/article/20250909500439"

# response = requests.get(url)
# response.raise_for_status()

# if response.status_code == 200:
#     html = response.text
#     soup = BeautifulSoup(response.text, 'html.parser')
#     headlines = soup.select("div.hdline_article_tit > a")

#     print("네이버 뉴스 헤드라인 & 본문\n")

#     for idx, hl in enumerate(headlines, 1):
#         title = hl.get_text(strip=True)
#         link = hl["href"]


#         printf(title)
# else : 
#     print(response.status_code)

headers = {"User-Agent": "Mozilla/5.0"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "html.parser")

headline_h1 = soup.find("title")
if headline_h1:
    print("헤드라인:", headline_h1.get_text(strip=True))

downloaded = trafilatura.fetch_url(url)

text = trafilatura.extract(
        downloaded,
        include_comments=False,
        include_tables=False,
        include_images=False,
        favor_recall=True, 
        output_format="txt"
    )
print("본문 = ", text)

min_len = 20
max_len = 130
if len(text) < 200:
    min_len = 10
    max_len = 80

summarizer = pipeline("summarization", model = "gogamza/kobart-summrization")
summary = summarizer(text, max_length=max_len, min_length=5, do_sample=False)

summaries.append(summary[0]['summary_text'])
