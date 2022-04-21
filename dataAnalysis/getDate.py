# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import datetime
import time

import requests
from bs4 import BeautifulSoup

# 怀孕期
url1 = "https://www.mama.cn/ask/list/c0-l2-all-p1.html"
# 婴儿期
url2 = "https://www.mama.cn/ask/list/c0-l1-all-p1.html"
# 幼儿期
url3 = "https://www.mama.cn/ask/list/c0-l3-all-p1.html"
# 学龄前
url4 = "https://www.mama.cn/ask/list/c0-l4-all-p1.html"
baseUrl = "https://www.mama.cn/ask/list/c0-l%d-all-p%d.html"


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(baseUrl % (1, 1))


def get_content(url, time_date=""):
    print("start %s %s" % (url, time_date))
    response = requests.get(url)
    if response.status_code != 200:
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    result_set = soup.find(name="ul", attrs={"class": "aFilter"}).find_all(name="li")
    for result in result_set:
        contents = result.find(name="div", attrs={"class": "aCon"}).contents
        title = contents[1].contents[0]["title"]
        time_str = contents[3].contents[3].contents[3].text[0:10]
        if time_date == "" or time_str == time_date:
            save("mama_data_%s.txt" % (time_str), title + "|" + time_str + "\n")


def save(file_path, content):
    with open(file_path, 'a', encoding="utf8") as f:
        f.write(content)
        f.close()
        print("finish:" + content)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(1, 5):
        for j in range(1, 50):
            get_content(baseUrl % (i, j), (datetime.date.today() + datetime.timedelta(days=-0)).strftime("%Y-%m-%d"))
            time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
