"""
Prepared by Mr. Shobhit Sharma
B.Tech, Electrical Engineering
NIT Kurukshetra, Kurukshetra, India

System Monitoring Daemon:
- Periodically collects system status
- Reports to remote API only if any parameter changes
- Designed to run efficiently in the background
"""
import time
import threading
import requests
import json
from datetime import datetime
import platform
from config import API_URL, CHECK_INTERVAL_MINUTES
from utils import get_machine_id, get_os_info
from checks.encryption import check as check_encryption
from checks.os_update import check as check_os_update
from checks.antivirus import check as check_antivirus
from checks.sleep_timeout import check as check_sleep_timeout

machine_id = get_machine_id()

last_state = None  # Global cache to detect change

def to_bool(value: str) -> bool:
    """Convert string like 'Enabled'/'Disabled' to boolean"""
    return value.strip().lower() == "enabled"

def to_int_minutes(value: str) -> int:
    """Convert string like '1200 minutes' to int"""
    return int(value.replace(" minutes", "").strip())

def collect_status():
    """Collect current system configuration and security status"""
    encryption = to_bool(check_encryption())
    antivirus = to_bool(check_antivirus())
    os_update = to_bool(check_os_update())
    sleep_timeout = to_int_minutes(check_sleep_timeout())

    return {
        "machine_id": machine_id,
        "os": get_os_info(),  # optional: or platform.platform()
        "encryption": encryption,
        "antivirus": antivirus,
        "os_update": os_update,
        "sleep_timeout": sleep_timeout,
        "last_updated": datetime.utcnow().isoformat()
    }
def has_changed(current, previous):
    """Check if the current state is different from the last state"""
    return json.dumps(current, sort_keys=True) != json.dumps(previous or {}, sort_keys=True)

def send_to_server(data):
    """Send the system state to the backend API"""
    try:
        response = requests.post(API_URL, json=data)
        if response.status_code == 200:
            print("[+] Data sent successfully:", response.status_code)
        else:
            print("[!] Server responded with error:", response.status_code, response.text)
    except Exception as e:
        print("[!] Failed to send data:", str(e))

def daemon_loop():
    """Main loop that checks and reports system status periodically"""
    global last_state
    print(f"[*] System monitoring daemon started, checking every {CHECK_INTERVAL_MINUTES} minute(s).")

    while True:
        current_state = collect_status()

        print("[*] Current system state:", current_state)
        print("[*] Last known state:", last_state)

        if has_changed(current_state, last_state):
            print("[!] Change detected. Sending report...")
            send_to_server(current_state)
            last_state = current_state
        else:
            print("[*] No changes detected. Skipping report.")

        time.sleep(CHECK_INTERVAL_MINUTES * 60)

def start_daemon():
    """Start daemon in a separate background thread"""
    thread = threading.Thread(target=daemon_loop, daemon=True)
    thread.start()
    thread.join()

# Direct run support
if __name__ == "__main__":
    start_daemon()
