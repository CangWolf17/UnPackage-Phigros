#基于python3.10
#加载库
import time
import hashlib
import jsonpath     #打算把数据一对一存到json
import json
import os

print("------WARNING------")
print("请将音频文件放置到工作目录下的audio文件夹中")
print("将曲绘文件放置到工作目录下的image文件夹中")
print("------WARNING------")

print("功能加载中...","")

#初始信息导入
number = 0    #可能把for语句记叉了所以只会用while做循环，定义一个计数变量

workpath = str(input("请输入工作目录（绝对路径）：")+"//")
audiopath = str(workpath + "audio//")
imagepath = str(workpath + "image//")
allcount = int(input("请输入总铺面数（即总文件数）："))-1

bufsize = 8*1024    #定义比对数据长度

#文件读取+生成md5模块

def load_hash(number):
    try:
        with open(str(filelist[number]),mode="rb") as file:  #打开文件
            data = file.read()   #将信息写入变量
                #生成md5校验信息
            md5 = hashlib.md5(data)
            file.close
            return md5

    except:
        print("Error:"+str(number))
    
    #原来更名部分的代码，留着改到功能2
    #src = os.path.join(workpath,str(number)+'.json')     #记录路径和更改后名字
    #dst = os.path.join(workpath,str(numOfNotes)+'('+str(number)+')'+'.json')
    #os.rename(src,dst)  #更名
    #print(str(number)+".json已处理，结果为："+str(i)+'('+str(number)+')'+'.json')     #输出结果

    
#欢迎页
print("数字0：退出","数字1：歌曲文件信息写入json","数字2：歌曲文件整理","数字3：曲绘文件整理")      #未完善
runfunction = int(input("输入数字选择功能："))

while runfunction > 0:

    if runfunction == 1:

        time_begin = time.time()    #效率计数

        number = 0
        filelist = os.listdir(audiopath)     #读取音频目录文件信息
        os.chdir(str(audiopath))             #切换工作目录
        while number <= int(allcount):
            
            md5 = load_hash(number=number)
            print(md5)
            number = number + 1

        time = time.time() - time_begin
        print("运行用时：",time)
            
    runfunction = int(input("输入数字选择功能："))
