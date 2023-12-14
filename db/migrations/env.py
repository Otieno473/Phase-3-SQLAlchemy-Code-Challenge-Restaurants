script output.
    """
    url = config.get_main_option("sqlite:///db/concerts.sqlite")
    context.configure(
        url=url,
        target_metadata=target_metadata