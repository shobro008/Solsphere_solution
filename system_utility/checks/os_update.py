import platform
import subprocess

def check():
    try:
        output = subprocess.check_output(["sc", "query", "wuauserv"], text=True)
        if "RUNNING" in output:
            return "Enabled"
        else:
            return "Disabled"
    except Exception as e:
        print("[!] OS update check error:", e)
        return "Unknown (manual check needed)"