import importlib
import pkgutil

ANALYSIS_TOOLS = {}

def load_analysis_tools():
    global ANALYSIS_TOOLS

    for module_info in pkgutil.iter_modules(__path__):
        if module_info.name.startswith("_"):
            continue
        module = importlib.import_module(f"{__name__}.{module_info.name}")

        if hasattr(module, "NAME"):
            ANALYSIS_TOOLS[module.NAME] = module

load_analysis_tools()

