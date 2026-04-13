# Journal de bord
[cryptolab](https://github.com/The-Crazy-Diamond/cryptolab)

-----------------------------------------------------------
## Tasks
### To do
-[ ] recycle MonoalphabeticDecoder and cryptoUtils
-[x] add txt file option for input
-[x] make keys optional or add default keys (e.g. for bacon default key should be 'AB')
-[x] roughly clean the architecture (erase useless folders and files)
-[X] improve UX with helpers (main.py, common_cmds.py)
-[X] People can enter via main (python3 main.py) and get blocked. Check lines added in main.py
-[x] Explain how to install (also check the difference between having a package or the whole project)
-[ ] Refactor README.md

### Ideas
-[ ] add streaming option for input
-[ ] create a jupyter notebook "sandbox" to try things using files in the project
-[ ] add feature that support binary files and potentially other alphabets

-----------------------------------------------------------
## Updating the project
### General procedure
1. Add feature
2. Update version
3. Commit
4. pip install -e . (is it really needed ?)

### Installing
- Locally from the terminal at the root of cryptolab: `pip install -e .`
- A snapshot from GitHub link: `pip install git+https://github.com/The-Crazy-Diamond/cryptolab.git`
- Uninstalling `pip uninstall cryptolab`
    
### Version number
Do it manually (for now) in pyproject.toml. MAJOR.MINOR.PATCH
- PATCH = Small fixes: bug fixes, minor improvements, no breaking changes
- MINOR = new features: new cipher added, new CLI command, new analysis tool
- MAJOR = Breaking changes: CLI syntax changes, API changes, removing features
Special rule 0.x.x: = Still in development
Move to 1.0.0 = Big milestone (stable tool)

### Using git
(think about changing the version first)
1. git init (first time only)
2. git status (to see the current state)
3. git add .
4. git commit -m "Add new cipher"
5. git commit -m "Bump version to 0.2.0" (eventually, for important version update)
6. git push
7. git push origin v0.2.0 (eventually)

-----------------------------------------------------------
## History

- 2026-04-11 Cleaned the architecture of repo, minor refactor of morse, installation note changed in README.md, improvement of journal, refactor of _template.py, updated version
- 2026-04-10 Refactor morse cipher and improve space handling
- 2026-04-09 Refactor CLI to support flexible cipher arguments (0, 1, or multiple keys). KeyError in bacon and cardan triliteral ciphers to correct.
- 2026-04-08 Implemented morse code. Dealing with ciphers having different key setups becomes annoying. Should work on this as a priority.
- 2026-04-07 Did git stuff locally and pushed to GitHub
- 2026-04-06 Implemented monoalphabetic cipher.
- 2026-04-05 Implemented vigenere cipher.
- 2026-04-04 Implemented bacon.py and backward.py in ciphers just to exercise. Realised that some ciphers methods need no key, some need several and some could be optional. To adjust later.
- 2026-04-03 Creation of the repo and the architecture of the project. Basics examples implemented with AI to have a guideline. Understood for most of the files what they are for. Lot of things to do. Looking forward to it.
