from pathlib import Path
import json

DATA_DIR = Path("data")
DATA_FILE = DATA_DIR / "issues.json"


def load_issues():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            content = f.read().strip()
            if content:
                return json.loads(content)
    return []

def save_issues(issues):
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(issues, f, indent=2)