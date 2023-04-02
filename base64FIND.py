# -*- coding: utf-8 -*-
# Author: Dimitrios Zacharopoulos
# All copyrights to Obipixel Ltd
# 01 April 2021

import argparse
import base64
import sys
import os
import codecs

# Print ASCII art
print("""
 ██▄ ▄▀▄ ▄▀▀ ██▀ █▀ █▄ █▀ █ █▄ █ █▀▄
 █▄█ █▀█ ▄██ █▄▄ ██  █ █▀ █ █ ▀█ █▄▀
""")

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
