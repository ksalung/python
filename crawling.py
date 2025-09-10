from gensim.summarization import summarize
import kss
import re
import requests
from bs4 import BeautifulSoup
import trafilatura

from summa.summarizer import summarize #pip install gensim==3.8.3, 이전 버젼 지우고, pip uninstall -y gensim kss summa


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
html = requests.get(url, headers=headers).text
html.raise_for_status()

soup = BeautifulSoup(html, "html.parser")

headline_h1 = soup.find("title")
if headline_h1:
    print("헤드라인:", headline_h1.get_text(strip=True))

text = trafilatura.extract(
        html,
        include_comments=False,
        include_tables=False,
        include_images=False,
        favor_recall=True, 
    )
print("본문 = ", text.strip())


