# -*- coding: utf-8 -*-
# jungol 33~127 입력받아 아스키코드 변환.

while True:
    num = input("아스키 코드 =? ")
    int_num = int(num)
    if int_num < 33 or int_num > 127:
        break
    print ("%c" %(int_num))