# -*- coding:utf-8 -*-
from  binascii import *
import sys
import  passwordlist

if len(sys.argv) != 3 or sys.argv[1] not in ('0','1'):
    sys.exit(
'''Useage:
python exchange.py <mode> <'exchange-string'> 

Examples:
python exchange.py 0 'hello'
python exchange.py 1 '12345' '''
)

def a2b(exc_num):
    src_pw = ''
    src_num = a2b_hex(exc_num)
    src_num_len = len(src_num)
    for m in range(0,src_num_len,2):
        n = m+1
        if n <= src_num_len:
           src_pw += pwlist[int(src_num[m])][int(src_num[n])]
        else:
           break
    return src_pw

def b2a(src_str):
    exc_list=[]
    exc_str=''
    for s in src_str:
        for i in range(len(pwlist)):
            if s in pwlist[i]:
               exc_list.append(i)
               #print pwlist[i].index(s)
               exc_list.append(pwlist[i].index(s)) 
               exc_str += str(i)+str(pwlist[i].index(s))
    return(b2a_hex(exc_str))

pwlist = passwordlist.pwlist
arg_list=[b2a,a2b]
print('{} => {}'.format(sys.argv[2],arg_list[int(sys.argv[1])](sys.argv[2])))
