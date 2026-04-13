def clean_data(data):
    """
    TODO: Implement your "clean_heartrate_data" function from TLAB #1 & #2
    within this module. Note that this code will be *slightly* different
    from your original function.
    """
    clean_data = []
    for x in data:
        if x != "mnutes\n":
            clean_data.append(float(x.strip))
    return clean_data