import platform
from utils import get_machine_id, send_report
from checks import encryption, os_update, antivirus, sleep_timeout

def main():
    print("[*] Running System Utility...")

    data = {
        "machine_id": get_machine_id(),
        "os": platform.system(),  # corrected from 'os_name' to 'os'
        "encryption": encryption.check(),  # corrected from 'encryption_status'
        "os_update": os_update.check(),   # corrected from 'os_update_status'
        "antivirus": antivirus.check(),   # corrected from 'antivirus_status'
        "sleep_timeout": sleep_timeout.check(),  # corrected from 'sleep_setting'
    }

    print("[*] Report Prepared:", data)
    send_report(data)

if __name__ == "__main__":
    main()
