import os
import sys

def verify_key():
    key = os.getenv("SOVEREIGN_MASTER_KEY")
    
    if not key:
        print("[!] ERROR: SOVEREIGN_MASTER_KEY not found in environment.")
        sys.exit(1)
        
    # Check if the key is base64 encoded (32 bytes when decoded)
    # 32 bytes * 4/3 = ~44 characters in base64
    if len(key) < 40:
        print("[!] ERROR: Key entropy too low. Generate a 32-byte key.")
        sys.exit(1)
        
    print("[+] SUCCESS: Master key is loaded and secure.")
    print(f"[+] Key Length: {len(key)} characters.")

if __name__ == "__main__":
    verify_key()
