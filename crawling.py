import requests
from bs4 import BeautifulSoup
import trafilatura
from transformers import pipeline

#pip install -r requirements.txt //install

url = "https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0003186662&PAGE_CD=N0006&utm_source=naver&utm_medium=newsstand&utm_campaign=naver_news&CMPT_CD=E0033"#input("내용을 요약하고 싶은 뉴스의 url을 입력해 주세요. :")https://www.chosun.com/opinion/manmulsang/2025/11/25/LYZPAMIUNZE4JCOVB5YSRXHWAM/
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



if soup.title and soup.title.string:
    title = soup.title.string.strip()
text = soup.get_text(separator="\n", strip=True)
if category is None:
    # (1) meta 태그에서 섹션 찾기
    meta_section = (
            soup.find("meta", {"property": "article:section"})
            or soup.find("meta", {"name": "section"})
            or soup.find("meta", {"name": "category"})
    )
if meta_section and meta_section.get("content"):
    category = meta_section["content"].strip()

# (2) 빵빵(상단 카테고리)에서 찾기 – 사이트별로 커스터마이징
if category is None:
    # 예시: <div class="category">정치</div> 같은 경우
    cat_el = soup.select_one(".category, .news_category, .location .now, .lnb .on")
    if cat_el:
        category = cat_el.get_text(strip=True)


summarizer = pipeline("summarization", model = "gogamza/kobart-summarization")
summary = summarizer(text, max_length=max_len, min_length=5, do_sample=False)


print("==================================================")
print("헤드라인 = ", headline)
print("본문 = ", text)
print("본문 요약 = ", summary[0]['summary_text'])
print("==================================================")