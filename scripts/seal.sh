#!/bin/bash
# MonFonts Black Folder Sealing Script

echo "[*] Initializing Black Folder Compression..."
# Pack all components excluding the secrets and output
tar --exclude='./output' --exclude='./.env' --exclude='./.git' \
    -czvf monfonts_sovereign_archive.tar.gz .

echo "[*] Encrypting container with AES-256-GCM..."
# This command uses the Vault logic to lock the archive
openssl enc -aes-256-gcm -salt -in monfonts_sovereign_archive.tar.gz \
    -out black_folder.enc -pass pass:$SOVEREIGN_MASTER_KEY

echo "[+] Black Folder Sealed. Ready for May 1st deployment."
