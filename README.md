# EnVault

EnVault is a secure, cross-platform application designed to manage and synchronize environment variables across projects and teams. It features encryption, version control, and seamless integration with popular development tools.

## Features

- **Secure Encryption**: All environment variables are encrypted using AES-256 encryption.
- **Cross-Platform**: Works on Windows, macOS, and Linux.
- **Version Control**: Track changes to environment variables with Git-like versioning.
- **Team Collaboration**: Share and sync environment variables across teams securely.
- **CLI & GUI**: Choose between a command-line interface or a graphical user interface.
- **Integration**: Easily integrate with CI/CD pipelines and popular development tools.

## GitHub Appeal
- **Security-Conscious Developers**: EnvVault ensures that sensitive data is always encrypted, both at rest and in transit.
- **Open Source**: Developers can contribute to the project, making it better for everyone.
- **Ease of Use**: Simplifies the management of environment variables, reducing the risk of human error.

## Project Structure
```
envault/
│
├── src/
│   ├── cli/
│   │   └── main.py
│   ├── gui/
│   │   └── main.py
│   ├── core/
│   │   ├── encryption.py
│   │   ├── version_control.py
│   │   └── sync.py
│   └── utils/
│       └── helpers.py
│
├── tests/
│   └── test_core.py
│
├── requirements.txt
├── README.md
└── LICENSE
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/makalin/EnVault.git
   cd EnVault
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the CLI:
   ```bash
   python src/cli/main.py save --key your_encryption_key
   ```

4. Run the GUI:
   ```bash
   python src/gui/main.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Conclusion

**EnVault** is a powerful tool for managing environment variables securely and efficiently. With its robust encryption, version control, and cross-platform support, it is an ideal solution for developers and teams looking to streamline their workflow while maintaining high security standards. The project is open-source, encouraging community contributions and continuous improvement.
