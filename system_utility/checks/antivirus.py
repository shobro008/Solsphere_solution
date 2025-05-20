import platform
import subprocess
def check():
    try:
        result = subprocess.run(
            ['powershell', '-Command',
             "Get-MpComputerStatus | Select-Object -ExpandProperty RealTimeProtectionEnabled"],
            capture_output=True, text=True)
        if result.returncode == 0:
            enabled = result.stdout.strip()
            return "Enabled" if enabled == "True" else "Disabled"
        else:
            return "Unknown"
    except Exception as e:
        print(f"[!] Antivirus check error: {e}")
        return "Unknown"
