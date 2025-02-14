# Account Enumeration and Bruteforce

User enumeration with email validation and password bruteforce with multithreading support.

## Description

This script performs two main functions:

1. **Email Validation** - Checks if an email exists in the target system.
2. **Bruteforce Attack** - Attempts to find the correct password for a given email using a dictionary attack with multi-threading support.

## Features

- Validates if an email is registered on the target system.
- Bruteforces passwords from a provided wordlist.
- Supports multi-threading for faster attacks.
- Includes timeout handling to prevent hanging requests.

## Requirements

- Python 3.x
- `requests` module (install with `pip install requests`)

## Usage

### Basic Commands

#### Validate an Email

```sh
python program.py -e test@example.com -v
```

#### Bruteforce an Email (with a password list)

```sh
python program.py -e test@example.com -b -f passwords.txt
```

#### Use Multiple Threads (for faster bruteforcing)

```sh
python program.py -e test@example.com -b -f passwords.txt -t 10
```

## Arguments

| Argument             | Description                                   |
| -------------------- | --------------------------------------------- |
| `-e`, `--email`      | Email address to validate or bruteforce       |
| `-v`, `--validate`   | Validate if the email exists                  |
| `-b`, `--bruteforce` | Attempt to bruteforce the password            |
| `-f`, `--file`       | Path to the password list file                |
| `-t`, `--threads`    | Number of threads for bruteforce (default: 1) |

## Notes

- **Multi-threading**: When using `-t`, be mindful of the target server's rate limits to avoid getting blocked.
- **Timeouts**: The script ensures that each request times out after 5 seconds to prevent long waits.
- **Usage**: The script is intended as a base to develop a more complex system.

## Disclaimer

This tool is for educational and authorized security testing purposes only. Unauthorized use is illegal and unethical. The developer is not responsible for any misuse of this script.

## LICENSE

MIT License

Copyright (c) 2025 Lautaro Colella

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
