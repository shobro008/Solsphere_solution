import platform
import subprocess
import re

def check():
    try:
        output = subprocess.check_output(["powercfg", "-query"], text=True)
        match = re.search(r"Sleep after.*?Power Setting Index: (\w+)", output, re.DOTALL)
        if match:
            minutes = int(match.group(1), 16)  # Convert hex to decimal
            return f"{minutes} minutes"
        else:
            return "Not Set"
    except Exception as e:
        print("[!] Sleep timeout check error:", e)
        return "Unknown"