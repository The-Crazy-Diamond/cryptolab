import importlib
import pkgutil

CIPHERS = {}

def load_ciphers():
    global CIPHERS

    for module_info in pkgutil.iter_modules(__path__):
        if module_info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{__name__}.{module_info.name}")

        if hasattr(module, "NAME"):
            CIPHERS[module.NAME] = module

load_ciphers()

