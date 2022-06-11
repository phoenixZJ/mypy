import requests
import os

class simple:
    def getHTMLText(self,url):
        try:
            r=requests.get(url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            return r.text
        except:
            return "产生异常"


    def downloadHtml(self,url):
        root = "D://html//"
        path = root + url.split('/')[-1]+'.html'
        print(path)
        try:
            if not os.path.exists(root):
                os.mkdir(root)
            if not os.path.exists(path):
                r = requests.get(url)
                with open(path, 'wb') as f:
                    f.write(r.content)
                    f.close()
                    print("文件保存成功")
            else:
                print("文件爬取失败")
        except:
            print("爬取失败")






