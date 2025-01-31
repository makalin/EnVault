import os
import json
from datetime import datetime
from .encryption import EnvVaultEncryption

class EnvVaultVersionControl:
    def __init__(self, vault_dir=".envvault"):
        self.vault_dir = vault_dir
        if not os.path.exists(self.vault_dir):
            os.makedirs(self.vault_dir)

    def save_version(self, env_vars, key):
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        version_file = os.path.join(self.vault_dir, f"version_{timestamp}.json")

        encrypted_vars = {}
        encryptor = EnvVaultEncryption(key)
        for k, v in env_vars.items():
            encrypted_vars[k] = encryptor.encrypt(v).decode()

        with open(version_file, 'w') as f:
            json.dump(encrypted_vars, f)

    def load_version(self, version_file, key):
        with open(version_file, 'r') as f:
            encrypted_vars = json.load(f)

        decryptor = EnvVaultEncryption(key)
        env_vars = {}
        for k, v in encrypted_vars.items():
            env_vars[k] = decryptor.decrypt(v.encode())

        return env_vars