# Cryptolab

A command-line tool to experiment with classical ciphers and basic cryptanalysis.

It supports multiple cipher systems, file input, and an extensible plugin architecture.

## Features

- Encrypt and decrypt using classical ciphers
- Command-line interface powered by Typer
- Basic cryptanalysis tools
- Extensible plugin system for adding new ciphers

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
cryptolab cipher --help
cryptolab decipher --help
```

## Examples

Encrypt/decrypt with Caesar cipher:

```bash
cryptolab cipher caesar "HELLO" 3
cryptolab decipher caesar "KHOOR" 3
```

### Other ciphers

```bash
cryptolab cipher vigenere "secret text" "KEY"
cryptolab cipher monoalphabetic "Dear Countess, blabla" "KEYWORD"
cryptolab decipher morse "... --- -- . / ... . -.-. .-. . - / -- . ... ... .- --. . "
```

### Using a file

```bash
cryptolab cipher caesar message.txt 15
```

## Project Structure

- `ciphers/` — cipher implementations
- `analysis/` — cryptanalysis tools
- `cli/` — command-line interface
- `utils/` — helper functions
  
## Personal note

This project grew out of a personal interest in cryptology as a mathematician. It is an opportunity to improve my programming skills while having fun.