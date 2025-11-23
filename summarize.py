from transformers import pipeline

# 요약 파이프라인 로드 (기본 모델: bart-large-cnn)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

text = """
인공지능은 컴퓨터 과학의 한 분야로, 기계가 인간처럼 사고하고 학습하며 문제를 해결할 수 있도록 하는 기술입니다.
최근 몇 년간 인공지능 기술은 비약적으로 발전하여 의료, 금융, 제조업 등 다양한 산업에 도입되고 있으며,
특히 자연어 처리, 컴퓨터 비전, 자율주행 등 분야에서 큰 성과를 이루고 있습니다.
"""

# 요약 실행
summary = summarizer(text, max_length=60, min_length=20, do_sample=False)

print("요약 결과:", summary[0]['summary_text'])