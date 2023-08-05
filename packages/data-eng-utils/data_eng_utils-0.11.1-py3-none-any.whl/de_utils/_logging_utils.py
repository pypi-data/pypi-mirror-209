
def get_logger_name(name, override_name=None):
    """Return the string name to use for a logger in the de_utils package.

    This function handles naming of logs when the utility module is
    imported. If module scripts are run directly with the default name,
    it is not changed. I.e., if the input name is '__main__', this
    function simply returns
    '__main__'.

    This function drops any leading underscores in any part of the
    logger name. E.g., '_some._logger._hierarchy' is transformed to
    'some.logger.hierarchy'.

    The final part of the logger name (after the final '.') can be
    overrode using override_name.

    :param name: full default log hierarcy
    :type name: str

    :param override_name: override the last part of the logger name
                          after the final '.'
    :type override_name: str

    :returns: the name to use for the logger
    :rtype: str
    """
    if name == "__main__":
        return name
    else:
        name_list = name.split(".")
        name_list = [item[1:] if item[0] == "_" else item
                     for item in name_list]
        if override_name is not None:
            name_list = name_list[:-1] + [override_name]
        return ".".join(name_list)
