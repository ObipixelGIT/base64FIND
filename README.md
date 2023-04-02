# base64FIND
base64FIND decodes Base64 encoded strings and outputs the strings for OSINT analysis.

## How the script works

- base64FIND decodes a Base64 encoded string.
- It uses the base64 library to decode the input string and the argparse library to parse command line arguments.
- The code starts by printing some ASCII art to the console.
- Then, it uses argparse to define and parse command line arguments.

Specifically, the program expects a Base64 encoded string as the first argument and provides two optional arguments:

- --output, which specifies a file to which the decoded string will be written.
- --encoding, which specifies the encoding to use for the decoded string. The default encoding is UTF-8.

- The code then validates the input string by attempting to decode it using base64.b64decode().
- If the input string is not a valid Base64 string, the program prints an error message and exits with an error code.

- If the input string is valid, the program decodes it using the specified encoding (or the default encoding if none was specified).
- If the decoded string cannot be decoded using the specified encoding, the program prints an error message and exits with an error code.

- If the --output argument was provided, the program writes the decoded string to the specified file using the specified encoding.
- If the file cannot be written, the program prints an error message and exits with an error code.

- Finally, the program attempts to copy the decoded string to the clipboard using the pyperclip library (if available) and prints the decoded string to the console.

Overall, this script provides a convenient way to decode Base64 strings from the command line and save the decoded output to a file.

## Preparation

```bash
sudo pip3 install argparse, base64, codecs
```

## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x base64FIND.py
```

## Usage

### Getting help
```bash
sudo python3 base64FIND.py -h

usage: base64FIND.py [-h] [--output FILE] [--encoding ENCODING] STRING

Decode a Base64 encoded string

positional arguments:
  STRING                the Base64 encoded string to decode

options:
  -h, --help            show this help message and exit
  --output FILE, -o FILE
                        write the decoded string to a file
  --encoding ENCODING, -e ENCODING
                        the encoding to use for the decoded string (default is utf-8)
```

### Executing example
```bash
sudo python3 base64FIND.py --output [output file] [encoded string]
```

## Example script
```python
import argparse
import base64
import sys
import os
import codecs

# Add command line arguments
parser = argparse.ArgumentParser(description='Decode a Base64 encoded string')
parser.add_argument('string', metavar='STRING', type=str,
                    help='the Base64 encoded string to decode')
parser.add_argument('--output', '-o', metavar='FILE', type=str,
                    help='write the decoded string to a file')
parser.add_argument('--encoding', '-e', metavar='ENCODING', type=str, default='utf-8',
                    help='the encoding to use for the decoded string (default is utf-8)')
args = parser.parse_args()

# Print the input string
print('\033[1;41m Input String: \033[m')
print(args.string)
print()

# Validate input string
try:
    decoded_bytes = base64.b64decode(args.string)
except (binascii.Error, TypeError):
    print("Invalid Base64 string.")
    sys.exit(1)

# Decode the string
try:
    decoded_string = decoded_bytes.decode(args.encoding)
except UnicodeDecodeError:
    print("Error: Unable to decode string with specified encoding.")
    sys.exit(1)

# Write the decoded string to a file if specified
if args.output:
    try:
        with codecs.open(args.output, 'w', encoding=args.encoding) as f:
            f.write(decoded_string)
        print(f"Decoded string written to {args.output}")
        print()
    except OSError:
        print(f"Error: Unable to write to file {args.output}")
        sys.exit(1)

# Copy the decoded string to the clipboard if available
try:
    import pyperclip
    pyperclip.copy(decoded_string)
    print("Decoded string copied to clipboard")
except ImportError:
    pass

# Display the decoded string to the console
print('\033[1;41m Decoded String: \033[m')
print(decoded_string)
```

## Example output
```
sudo python3 base64FIND.py --output base64FIND-decoded.txt SGVsbG8gV29ybGQh                                                                  ─╯
Password:

 ██▄ ▄▀▄ ▄▀▀ ██▀ █▀ █▄ █▀ █ █▄ █ █▀▄
 █▄█ █▀█ ▄██ █▄▄ ██  █ █▀ █ █ ▀█ █▄▀

 Input String:
SGVsbG8gV29ybGQh

Decoded string written to base64FIND-decoded.txt

 Decoded String:
Hello World!
```

## Disclaimer
"The scripts in this repository are intended for authorized security testing and/or educational purposes only. Unauthorized access to computer systems or networks is illegal. These scripts are provided "AS IS," without warranty of any kind. The authors of these scripts shall not be held liable for any damages arising from the use of this code. Use of these scripts for any malicious or illegal activities is strictly prohibited. The authors of these scripts assume no liability for any misuse of these scripts by third parties. By using these scripts, you agree to these terms and conditions."

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.
