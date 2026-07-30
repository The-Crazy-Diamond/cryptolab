import importlib
import pkgutil

ANALYSIS_METHODS = {}

def load_methods():
    global ANALYSIS_METHODS

    for module_info in pkgutil.iter_modules(__path__):
        if module_info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{__name__}.{module_info.name}")

        if hasattr(module, "NAME"):
           ANALYSIS_METHODS[module.NAME] = module

load_methods()

