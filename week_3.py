# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:34:03 2024

@author: student
"""

# 建立字典
letter_dict = {chr(i + 97): chr(i + 65) for i in range(26)}

# 讀取使用者輸入
input_letter = input("請輸入小寫英文字母：")

# 轉換為大寫並顯示結果
if input_letter in letter_dict:
    upper_case_letter = letter_dict[input_letter]
    print("大寫字母為：", upper_case_letter)
else:
    print("輸入的不是小寫英文字母。")
