import subprocess
def check():
    try:
        result = subprocess.run(["manage-bde", "-status", "C:"], capture_output=True, text=True)
        if result.returncode != 0:
            return f"BitLocker Not Available or Not Running as Admin"

        output = result.stdout
        if "Percentage Encrypted: 100%" in output:
            return "Encrypted"
        elif "Percentage Encrypted: 0%" in output or "Fully Decrypted" in output:
            return "Not Encrypted"
        else:
            return "Partially Encrypted"
    except Exception as e:
        print("[!] Encryption check error:", e)
        return "Unknown"
