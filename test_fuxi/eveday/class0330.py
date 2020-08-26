#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : class0330.py.py
# Author: mangguo
# Date  : 2020/3/31


# def say_gobay():
#     print('真的是快乐呀')
#     return 'name',1234567,{1:2}
# res=say_gobay()
# print(res)
#多个值可以挨个赋值
# x,y,z=say_gobay()
# print(x)
# print(y)
# print(z)


# 1-10的相加
# i= 0
# sum = 0
# while i<10:
#     i+= 1
#     sum=sum+i
# print(sum)
# 足球队加人
i=0
m=0
while m < 10:
    m+=1
    try:
        yeal = int(input('请输入你的年龄：'))
        if  10<=yeal<=12:
            while  i=='男'  or  i=='女':
                gex = input('请输入你的性别（男、女）：')
                if gex =='男':
                    i += 1
                    print('该人员可以加人足球队')
                elif gex=='女':
                    pass
                else:
                    print('请正确输入性别')
        elif yeal>12 or yeal<10:
                pass
    except ValueError:
        print("请正确输入年龄")
print(i)
