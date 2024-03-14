# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:42:59 2024

@author: student
"""

import random

# 讀取使用者輸入
n = int(input("請輸入要抽取的數字個數 n："))
a = int(input("請輸入隨機數的下限 a："))
b = int(input("請輸入隨機數的上限 b："))

# 隨機抽取 n 個數字並儲存在列表中
random_numbers = [random.randint(a, b) for _ in range(n)]

# 刪除重複的數字
random_numbers = list(set(random_numbers))

# 由大到小排序
random_numbers.sort(reverse=True)

# 顯示結果
print("隨機抽取的數字（刪除重複並由大到小排序）：", random_numbers)

