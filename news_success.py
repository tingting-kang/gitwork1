import requests
from bs4 import BeautifulSoup
import csv
import schedule
import time
from datetime import datetime

# 目标网页URL
url = 'https://www.usst.edu.cn/slyw/list4.htm'

def fetch_and_save_news():
    # 发送GET请求获取网页内容
    response = requests.get(url)

    # 设置编码为UTF-8
    response.encoding = 'utf-8'

    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # 查找所有新闻项
        news_items = soup.select('ul.news_list.list2.list-img > li.news')

        # 打开CSV文件并准备写入，使用'a'模式追加数据
        with open('news_data4.csv', 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['标题', '日期', '内容简介', '链接', '图片链接']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # 如果文件为空，则写入表头
            if csvfile.tell() == 0:
                writer.writeheader()

            # 遍历新闻项并提取所需信息
            for item in news_items:
                try:
                    # 获取新闻标题
                    title = item.select_one('.news_title').get_text(strip=True)

                    # 获取新闻日期
                    date = item.select_one('.news_time').get_text(strip=True)

                    # 获取新闻内容（简介）
                    summary = item.select_one('.news_text').get_text(strip=True)

                    # 获取新闻链接
                    link = item.select_one('a')['href']

                    # 获取新闻的图片链接
                    image = item.select_one('.news_imgs img')['src'] if item.select_one('.news_imgs img') else 'No Image'

                    # 写入每条新闻的数据
                    writer.writerow({
                        '标题': title,
                        '日期': date,
                        '内容简介': summary,
                        '链接': link,
                        '图片链接': image
                    })
                except Exception as e:
                    print(f"处理新闻项时发生错误: {e}")

        print(f"[{datetime.now()}] 新闻数据已成功保存到 news_data4.csv 文件中")
    else:
        print(f"[{datetime.now()}] 请求失败，状态码：{response.status_code}")

if __name__ == "__main__":
    # 设置定时任务，每60秒执行一次fetch_and_save_news函数
    schedule.every(60).seconds.do(fetch_and_save_news)

    print('Scheduler started. Press Ctrl+C to exit.')
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)  # 每隔1秒检查一次是否需要运行任务
    except KeyboardInterrupt:
        print('Scheduler stopped.')
