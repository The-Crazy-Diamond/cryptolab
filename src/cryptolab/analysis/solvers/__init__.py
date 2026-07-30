# import importlib
# import pkgutil

# SOLVERS = {}

# def load_solvers():
#     global SOLVERS

#     for module_info in pkgutil.iter_modules(__path__):
#         if module_info.name.startswith("_"):
#             continue
#         module = importlib.import_module(f"{__name__}.{module_info.name}")

#         if hasattr(module, "NAME"):
#             SOLVERS[module.NAME] = module

# load_solvers()

