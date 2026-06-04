"""Dò input mơ hồ để tìm cái kích hoạt nhánh low-confidence (bot hỏi lại).

Chạy: ..\\..\\codebase\\backend\\.venv\\Scripts\\python.exe probe-lowconfidence.py
"""
import json

import requests

API = "http://127.0.0.1:8000/api/chat/triage"
PATIENT = {"name": "Nguyen Van A", "phone": "0900000000", "birth_year": 1990}

PROBES = [
    "Tôi bị đau",
    "Tôi thấy không khỏe trong người",
    "Mấy hôm nay tôi thấy là lạ",
    "Tôi muốn đi khám",
    "Tôi bị khó chịu",
]

for text in PROBES:
    data = requests.post(API, json={"patient": PATIENT, "messages": [{"role": "user", "content": text}]}, timeout=60).json()
    print(f"\ninput: {text!r}")
    print("  path        :", data.get("path"), "| needs_more_info:", data.get("needs_more_info"))
    print("  specialty   :", data.get("specialty"), "| confidence:", data.get("confidence"))
    print("  follow_up   :", data.get("follow_up_questions"))
    print("  reply       :", (data.get("reply") or "")[:200])
