# Cryptolab

A Python toolkit for classical cryptography, combining cipher implementations, cryptanalytic methods, and interactive solving tools through a command-line interface.

## Features

- Encrypt and decrypt using classical ciphers
- Apply cryptanalytic methods (frequency analysis, IoC, n-grams, ...)
- Interactive solving tools for classical ciphers
- Extensible plugin architecture for adding ciphers and analysis methods
- Command-line interface powered by Typer

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
cryptolab solve --help
```

## Examples

### Basic example
Encrypt/decrypt with Caesar cipher:

```bash
cryptolab encrypt caesar "HELLO" 3
cryptolab decrypt caesar "KHOOR" 3
```

### More ciphers examples

```bash
cryptolab encrypt vigenere "secret text" "KEY"
cryptolab encrypt monoalphabetic "Dear Countess, ..." "KEYWORD"
cryptolab decrypt morse "... --- -- . / ... . -.-. .-. . - / -- . ... ... .- --. . "
```

### File input

```bash
cryptolab encrypt caesar message.txt 15
```

### Use analysis methods

```bash
cryptolab analyse frequency message.txt
cryptolab analyse ngrams message.txt 3
cryptolab analyse kasiski message.txt
```

### Use an interactive solver

Interactively solve a ciphertext encrypted with a monoalphabetic substitution:

```bash
cryptolab solve monoalphabetic message.txt
```

## Project Structure

```text
cryptolab/
├── analysis/
│   ├── methods/
│   └── solvers/
├── ciphers/
├── ui/
├── utils/
└── data/
```

## Add new features

### Add new cipher

Use cipher plugin template:

```bash
cp ciphers/_template.py ciphers/my_cipher.py
```

Modify my_cipher.py and implement the encrypt() and decrypt() functions.

### Add new analysis method

Use analysis tool plugin template:

```bash
cp analysis/methods/_template.py analysis/methods/my_method.py
```

Modify my_method.py and implement the analyse() function.
  
## Personal note

Cryptolab began as a personal project driven by my interest in classical cryptology. It has become a playground for exploring cryptanalysis, improving my Python skills, and building a well-structured, extensible codebase.
