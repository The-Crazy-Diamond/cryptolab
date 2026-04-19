# Cryptolab

A command-line tool to experiment with classical ciphers and basic cryptanalysis.

It supports multiple cipher systems, file input, and an extensible plugin architecture.

## Features

- Encrypt and decrypt using classical ciphers
- Command-line interface powered by Typer
- Basic cryptanalysis tools
- Extensible plugin system for adding new ciphers or new analysis tools

## Installation

For simple usage:

```bash
pip install git+https://github.com/The-Crazy-Diamond/cryptolab.git
```

For development:

```bash
git clone https://github.com/The-Crazy-Diamond/cryptolab.git
cd cryptolab
pip install -e .
```

## Usage

Run the CLI from your terminal:

```bash
cryptolab --help
cryptolab encrypt --help
cryptolab decrypt --help
cryptolab analyse --help
```

## Examples

### Basic example
Encrypt/decrypt with Caesar cipher:

```bash
cryptolab encrypt caesar "HELLO" 3
cryptolab decrypt caesar "KHOOR" 3
```

### Other ciphers

```bash
cryptolab encrypt vigenere "secret text" "KEY"
cryptolab encrypt monoalphabetic "Dear Countess, ..." "KEYWORD"
cryptolab decrypt morse "... --- -- . / ... . -.-. .-. . - / -- . ... ... .- --. . "
```

### Use a file

```bash
cryptolab encrypt caesar message.txt 15
```

### Use analysis tools

Analyse a text assuming it was encrypted with monoalphabetic substitution:

```bash
cryptolab monoalphabetic message.txt
```

## Project Structure

- `ciphers/` — cipher implementations
- `analysis/` — cryptanalysis tools
- `cli/` — command-line interface
- `utils/` — helper functions

## Add new features

### Add new cipher

Use cipher plugin template in cryptolab/ciphers/:

```bash
cp _template.py your_cipher.py
```

Modify the code in your_cipher.py and implement encrypt and decrypt functions.

### Add new analysis tool

Use analysis tool plugin template in cryptolab/analysis/:

```bash
cp _template.py your_tool.py
```

Modify the code in your_tool.py and implement analyse function.
  
## Personal note

This project grew out of a personal interest in cryptology as a mathematician. It is an opportunity to improve my programming skills while having fun.