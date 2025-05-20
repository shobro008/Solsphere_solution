import uuid
import requests
from config import API_URL
import platform

def get_machine_id() -> str:
    """
    Returns a unique machine identifier based on MAC address.
    """
    return str(uuid.getnode())

def send_report(data: dict):
    """
    Sends the system health report data to the configured API endpoint.
    """
    try:
        response = requests.post(API_URL, json=data, timeout=10)  # timeout in seconds
        if response.status_code == 200:
            print("[+] Data sent: 200 OK")
        else:
            print(f"[!] Failed to send data: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"[!] Error sending data: {e}")
def get_os_info() -> str:
    """
    Returns a string describing the current operating system with version info.
    Examples:
        "Windows 10"
        "Ubuntu 20.04"
        "macOS 13.3"
    """
    system = platform.system()
    if system == "Windows":
        version = platform.version()
        release = platform.release()
        return f"Windows {release} (Version {version})"
    elif system == "Linux":
        # Try to get distro info if possible
        try:
            import distro  # This is an external package, optional
            distro_name = distro.name(pretty=True)
            if distro_name:
                return distro_name
        except ImportError:
            pass
        # fallback
        return "Linux " + platform.release()
    elif system == "Darwin":
        # macOS
        version, _, _ = platform.mac_ver()
        return f"macOS {version}"
    else:
        return system