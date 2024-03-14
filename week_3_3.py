# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 08:45:18 2024

@author: student
"""

import random

# 建立撲克牌
suits = ['♠', '♥', '♦', '♣']
ranks = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
deck = [rank + suit for rank in ranks for suit in suits]

# 洗牌
random.shuffle(deck)

# 初始化四個玩家的手牌列表
players = [[] for _ in range(4)]

# 發牌
for i, card in enumerate(deck):
    player_index = i % 4  # 玩家索引
    players[player_index].append(card)

# 將手牌排序
for player in players:
    player.sort(key=lambda x: (ranks.index(x[:-1]), suits.index(x[-1])))

# 顯示結果
for i, player in enumerate(players):
    print(f"玩家 {i + 1} 的手牌：", player)
