import requests
def get_one_img():
    url="https://www.usst.edu.cn/_upload/article/images/f3/aa/875e5c3e4e9ab4b311847c1b9d6e/9ca89902-1c4c-44a3-8111-5a0a398b9a36.jpg"

    headers={
         'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.9101 SLBChan/105 SLBVPV/64-bit'
      }

    res=requests .get(url, headers=headers)
    with open("picture321_2.jpg" , 'wb') as f:
        f.write(res.content)

# get_one_img()

def get_imgs(url,name):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 SLBrowser/9.0.5.9101 SLBChan/105 SLBVPV/64-bit'
    }

    res = requests.get(url, headers=headers)
    img_name=f"{name}.jpg"
    with open(img_name, 'wb') as f:
        f.write(res.content)
url="https://www.usst.edu.cn/_upload/article/images/86/f3/e2110ef34c74bfa76e8d0fdb4c88/84277ddb-b458-47c0-a8ee-7cdbae70c8f6.png"
name="1"
get_imgs(url,name)