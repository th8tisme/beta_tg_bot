import json, random, uuid
from pathlib import Path

DATA = Path("data")
QUESTIONS = DATA / "questions.json"
SESSIONS = DATA / "sessions.json"
USED = DATA / "used.json"

def _read(p: Path, default): return json.loads(p.read_text("utf-8")) if p.exists() else default
def _write(p: Path, data): p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def load_questions() -> list[str]:
    return [str(x).strip() for x in _read(QUESTIONS, []) if str(x).strip()]

def create_session(user_a: int, user_b: int) -> str:
    session_id = str(uuid.uuid4())
    data = _read(SESSIONS, {})
    data[session_id] = {"a": user_a, "b": user_b, "status": "pending"}
    _write(SESSIONS, data)
    return session_id

def confirm_session(session_id: str) -> dict | None:
    data = _read(SESSIONS, {})
    if session_id not in data:
        return None
    data[session_id]["status"] = "active"
    _write(SESSIONS, data)
    return data[session_id]

def cancel_session(session_id: str) -> None:
    data = _read(SESSIONS, {})
    data.pop(session_id, None)
    _write(SESSIONS, data)

def get_user_sessions(user_id: int) -> list[str]:
    sessions = _read(SESSIONS, {})
    return [sid for sid, s in sessions.items() if s["status"] == "active" and user_id in (s["a"], s["b"])]

def get_partner(session_id: str, user_id: int) -> int:
    s = _read(SESSIONS, {})[session_id]
    return s["b"] if s["a"] == user_id else s["a"]

def pick_question(session_id: str) -> str | None:
    qlist = load_questions()
    used = _read(USED, {})
    used_ids = set(used.get(session_id, []))
    available = [q for i, q in enumerate(qlist) if str(i) not in used_ids]

    if not available:
        return None

    question = random.choice(available)
    qid = str(qlist.index(question))
    used.setdefault(session_id, []).append(qid)
    _write(USED, used)
    return question
