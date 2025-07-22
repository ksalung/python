newjeans = ["철수", "영희", "민수", "지현", "서연"]
ive = ["영희", "민수", "지수", "서연", "하나"]
aespa = ["철수", "지현", "지수", "서연", "나영"]


like = []
for member in newjeans:
    if member in ive:
        like.append(member)
for fan in like:
    if not fan in aespa:
        print(fan)

    

