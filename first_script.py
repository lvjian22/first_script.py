# -*- coding: utf-8 -*-
"""
Created on Tue May 21 23:17:29 2024

@author: Lijian
"""

#！/usr/bin/env 
from math import exp,log,sqrt
#使用math模块中的一些函数function

print("output #1: I'm excited to learn python.")
#两个数值相乘
x = 7
y = 8
z = x * y
print("output #2: seven multiply eight equals {0:d}.".format(z))
#{}表示一个占位符，表示这里传入print语句一个具体的值，这里指变量z，
#0指向format()方法中的第一个参数；冒号（:）用来分隔传入的值与他的格式

#两个列表相加
a = [1,2,3,4]
b = ["first","second","third","fourth"]
c = a + b
print("output #3: {0},{1},{2}".format(a,b,c))

#数值：整数、浮点数
#整数int
x=9
print("output #4:{0}".format(x))
print("output #5:{0}".format(3**5))
print("output #6:{0}".format(int(8.3)/int(2.4)))

#浮点数float
print("output #7:{0:.3f}".format(8.3/2.7)) #.3f设定打印输出值保留3位小数
y = 2.5*4.8
print("output #8:{0:.1f}".format(y))
r = 8/float(3)
print("output #9:{0:.2f}".format(r))
print("output #10:{0:.4f}".format(8.0/3))

#字符串string，可包含在单引号、双引号、三个单引号或三个双引号之间
print("output #11:{0:s}".format('I\'m enjoying learning python.'))

string1 = "This is a "#留有空格
string2 = "short string"
sentence = string1 + string2
print("output #12:{0:s}".format(sentence))
print("output #13:{0:s}{1:s}{2:s}".format("She is ","very "*4,"beautiful."))
m = len(sentence)
print("output #14:{0:d}".format(m))

#1.4.3正则表达式 re模块
import re
string = "The quick brown fox jumps over the lazy dog."
string_list = string.split()
pattern = re.compile(r"The", re.I)#re.I函数确保模式不区分大小写
count = 0
for word in string_list:
    if pattern.search(word):
        count += 1
print("output #15:{0:d}".format(count))

#1.4.4日期 datetime模块
from datetime import date,time,datetime,timedelta
today = date.today()#创建一个date对象，包含年月日，不包含时间元素
print("output #16:today:{0!s}".format(today))#!s表示传入到print语句中的值应该格式化为字符串
current_datetime = datetime.today()
print("output #17:today:{0!s}".format(current_datetime))

#1.4.5列表---使用方括号[]创建列表
a_list = [1,2,3]
print("output #18:{}".format(a_list))
#1.4.6元组---使用圆括号()创建元组,不能被修改
my_tuple = ('x','y','z')
print("output #19:{}".format(my_tuple))
#1.4.7字典---使用花括号{}创建字典，本质上是包含各种唯一标识符的成对信息的列表
empty_dict = {}
a_dict = {'one':1,'two':2,'three':3}#说明键和值用冒号隔开
print("output #20:{}".format(a_dict))
#1.4.8控制流--逻辑循环
#1.5读取文本文件 sys模块
'''
sys.argv[]是一个列表
sys.argv[0]是被调用的脚本文件名或全路径
sys.argv[1:]之后的元素就是我们从程序外部输入的，而非代码本身的，想要看到它的效果，就要将程序保存，从外部运行程序并给参数，这也是我们在cmd里面运行的原因。
'''
#读取单个文本文件(旧方法）
import sys
from operator import itemgetter
'''
input_file = sys.argv[1]#提供文件路径名
print("Output #21:")
filereader = open(input_file,'r')#r模式--只读模式
for row in filereader:
    print(row.strip())
filereader.close()
'''
#读取单个文本文件(新方法）with语句，结束后自动关闭文件
input_file = sys.argv[1]
print("Output #22:")
with open(input_file,'r', newline='') as filereader:
    for row in filereader:
        print("{}".format(row.strip()))
python first_script.py file_to_read.txt
#python first_script.py "路径名\file_to_read.txt"
#1.6使用glob读取多个文本文件/处理文件夹
import glob #找出与特定模式匹配的所以路径名
import os #提供路径名函数
#print("Output #23:")
#input_path = sys.argv[1] #提供目录路径名
#for input_file in glob.glob(os.path.join(inputPath,'*.txt')):#找出符合特定模式的某个文件夹下所以文件
   # with open(input_file, 'r', newline='') as filereader:
 #       for row in filereader:
 #           print("{}".format(row.strip()))
#python first_script.py "C：Users\[Your Name]\Desktop"