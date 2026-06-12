# 1. Export the key from your secure storage
export SOVEREIGN_MASTER_KEY=$(cat /path/to/your/secure/sovereign.key)

# 2. Run the verification
python3 scripts/verify_vault.py

# 3. Only if it returns SUCCESS, execute the seal
./scripts/seal.sh
