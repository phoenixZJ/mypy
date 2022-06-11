def doubleName(name):
    print(name+"+"+name)

print("第一次运行")

def stupid(name):
    return name+"怎么这么简单"



def appendNo(name):
    for i in range(100):
        print(name+str(i))


appendNo('编号')

import os
def amazing():
    root = "D://么么哒//"
    os.mkdir(root)
    for i in range(100):
        path=root+"么么哒"+str(i)
        print(path)
        if not os.path.exists(path):
            os.mkdir(path)
amazing()

