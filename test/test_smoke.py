def test_app_imports():
    """
    Smoke test: el proyecto importa sin errores.
    Ajustá si necesitás importar módulos específicos.
    """
    import importlib

    importlib.import_module("main")
