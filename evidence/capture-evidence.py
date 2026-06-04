"""Bắn các test case triage vào backend đang chạy, lưu JSON bằng chứng (UTF-8 sạch).

Chạy bằng python của venv backend. Yêu cầu: backend chạy ở http://127.0.0.1:8000
(đã set OPENAI_API_KEY).
"""
import json
from pathlib import Path

import requests

API = "http://127.0.0.1:8000/api/chat/triage"
HERE = Path(__file__).resolve().parent
PATIENT = {"name": "Nguyen Van A", "phone": "0900000000", "birth_year": 1990}

CASES = {
    "TC1-happy": [
        {"role": "user", "content": "Tôi đau bụng âm ỉ 3 ngày nay, hay buồn nôn sau khi ăn"},
    ],
    "TC2-lowconf": [
        {"role": "user", "content": "Tôi thấy mệt"},
    ],
    "TC3-redflag": [
        {"role": "user", "content": "Tôi đau ngực dữ dội và khó thở"},
    ],
    "TC4-correction": [
        {"role": "user", "content": "Tôi bị đau đầu dữ dội và chóng mặt"},
        {"role": "assistant", "content": "Bạn đau đầu mức độ nào?"},
        {"role": "user", "content": "Thực ra tôi đùa, chỉ hơi sổ mũi thôi"},
    ],
}

for tc_id, messages in CASES.items():
    resp = requests.post(API, json={"patient": PATIENT, "messages": messages}, timeout=60)
    data = resp.json()
    out = HERE / f"{tc_id}.json"
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n===== {tc_id} =====")
    print("input        :", messages[-1]["content"])
    print("path         :", data.get("path"), "| source:", data.get("analysis_source"))
    print("specialty    :", data.get("specialty"), "| confidence:", data.get("confidence"))
    print("needs_more   :", data.get("needs_more_info"), "| follow_up:", data.get("follow_up_questions"))
    print("red_flags    :", data.get("red_flags"))
    print("reasoning    :", data.get("reasoning_summary"))
    print("reply        :", (data.get("reply") or "")[:260])
    print("slots        :", len(data.get("slots") or []))
