import argparse
from core.version_control import EnvVaultVersionControl
from core.sync import EnvVaultSync
from core.encryption import EnvVaultEncryption

def main():
    parser = argparse.ArgumentParser(description="EnvVault CLI")
    parser.add_argument("command", choices=["save", "load", "push", "pull"], help="Command to execute")
    parser.add_argument("--key", required=True, help="Encryption key")
    parser.add_argument("--file", help="Version file to load")
    parser.add_argument("--server", help="Sync server URL")

    args = parser.parse_args()

    if args.command == "save":
        env_vars = {"API_KEY": "12345", "DB_PASSWORD": "s3cr3t"}
        version_control = EnvVaultVersionControl()
        version_control.save_version(env_vars, args.key)
        print("Environment variables saved.")

    elif args.command == "load":
        if not args.file:
            print("Error: --file is required for load command")
            return
        version_control = EnvVaultVersionControl()
        env_vars = version_control.load_version(args.file, args.key)
        print("Loaded environment variables:", env_vars)

    elif args.command == "push":
        if not args.server:
            print("Error: --server is required for push command")
            return
        env_vars = {"API_KEY": "12345", "DB_PASSWORD": "s3cr3t"}
        sync = EnvVaultSync(args.server, args.key)
        result = sync.push(env_vars)
        print("Push result:", result)

    elif args.command == "pull":
        if not args.server:
            print("Error: --server is required for pull command")
            return
        sync = EnvVaultSync(args.server, args.key)
        env_vars = sync.pull()
        print("Pulled environment variables:", env_vars)

if __name__ == "__main__":
    main()