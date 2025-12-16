#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Search for quotes in diet_speeches.csv and find their session_ids"""

import csv
import re

csv_path = r"c:\Users\youki\codes\i-1-grand-prix\each_project\ai-plan-test\kokkai\diet_speeches.csv"

# Quotes to search for (key parts)
quotes = [
    "海外のサービスを活用するだけではデジタル赤字がますます拡大",
    "リテラシー教育を進めていく",
    "司令塔機能を強化",
    "法、技術、契約、この三つの手段の適切な組合せ",
    "ディープフェイクポルノ",
    "基本計画の冒頭に記載されることで",
    "人間中心のＡＩ原則",
    "ＬＬＭの開発、日本語でやること",
    "グローバルサウスでのＡＩ人材",
    "学習データから偏見情報を除外",
    "ＥＵではＡＩ法を作り",
    "方言の衰退が進んでいる",
    "一兆円、二兆円、三兆円",
    "ＡＩ戦略本部の事務局である内閣府",
    "ＡＩエンジニアを始めとするＡＩ関連人材",
    "具体的な目標や指標の設定については適時適切",
    "研究開発の推進ですとか",
    "イノベーションの促進とリスク対応の両立"
]

print(f"Reading {csv_path}...")

results = {}
with open(csv_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        session_id = row['session_id']
        message_id = row['message_id']
        message = row['message']
        
        for quote in quotes:
            if quote in message:
                if quote not in results:
                    results[quote] = []
                results[quote].append({
                    'session_id': session_id,
                    'message_id': message_id,
                    'snippet': message[:200] if len(message) > 200 else message
                })

print("\n=== Results ===\n")
for quote, matches in results.items():
    print(f"Quote: {quote[:50]}...")
    for m in matches[:2]:  # Show first 2 matches
        print(f"  session_id: {m['session_id']}")
        print(f"  message_id: {m['message_id']}")
    print()

# Create a unique session_id to kokkai_id mapping
unique_sessions = set()
for matches in results.values():
    for m in matches:
        unique_sessions.add(m['session_id'])

print("\n=== Unique Session IDs ===")
for i, sid in enumerate(sorted(unique_sessions), 1):
    print(f"kokkai_{i:03d}: {sid}")
