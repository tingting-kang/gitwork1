import re
def get_urls():
    #with open("web_yuan.html","r",encoding="utf-8") as f:
       # text=f.read()
        #print(text)

    result=re.findall("img src='(.*?)'",text)
    print(result)
    url='https://www.usst.edu.cn/'+result
