# SmartGen

SmartGen is a simple Python program designed to enhance file security by adding password protection to any Windows directory. It achieves this by creating a batch file within the directory that can hide or reveal the contents based on a password.

## Features

- Password protection for any Windows directory.
- Simple command-line interface.
- Creates a batch file for easy access and management.

## Requirements

- Python 3.6 or higher.
- Windows operating system.

## Installation

1. Ensure you have Python 3 installed on your machine.
2. Clone the repository or download the `smartgen.py` script to your machine.

## Usage

Open a command prompt and navigate to the directory where `smartgen.py` is located. Run the following command:

```bash
python smartgen.py <directory_path> <password>
```

- `<directory_path>`: The path to the directory you want to protect.
- `<password>`: The password you want to set for accessing the directory.

Example:

```bash
python smartgen.py "C:\Users\YourName\Documents\MyFolder" "mypassword"
```

This command will create a `lock.bat` file inside the specified directory. Use this batch file to lock or unlock the folder.

## Security Note

This method relies on basic Windows features and is not meant to replace professional encryption tools for high-security needs. It's a simple deterrent for casual snooping.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Disclaimer

Use this software at your own risk. The author is not responsible for any data loss or security breaches resulting from the use of this tool.