import requests
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
list_img_name = []

for page in range(1, 51): # 获取HTML，将书名放入列表
    html = requests.get(f"https://books.toscrape.com/catalogue/page-{page}.html").text
    soup = BeautifulSoup(html, "html.parser")
    generator_img_name = soup.find_all("h3")
    print(f"This is the page{page}.")
    for img_name in generator_img_name:
        list_img_name.append(img_name.a["title"])

print(f"共有{len(list_img_name)}本")
for num in range(1, len(list_img_name)+1): # 每一页分隔开
    if num % 20 == 0:
        print(f"-----------{num / 20}页")
    else:
        print(list_img_name[num-1])