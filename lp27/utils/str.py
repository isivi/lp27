def str_to_bool(name):
    """
    Convert string to boolean inspecting string value more deeply.
    """
    if isinstance(name, bool):
        return name
    return name.lower() in ("true", "yes", "t", "y", "on", "1")
