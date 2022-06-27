try:
    from importlib.metadata import entry_points  # type:ignore
except ImportError:  # pragma: no cover
    from importlib_metadata import entry_points  # type:ignore


# TODO: this is a duplication of code from Fugue, dedup it!
def register_plugins():
    for plugin in entry_points().get("tune.plugins", []):
        try:
            register_func = plugin.load()
            assert callable(register_func), f"{plugin.name} is not a callable"
            register_func()
        except ImportError:  # pragma: no cover
            pass


register_plugins()
