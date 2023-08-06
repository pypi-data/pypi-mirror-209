def raise_not_implemented():
    raise NotImplementedError("This function is not implemented")


def raise_missing_argument():
    raise ValueError("Must pass either `data_path` path or `data` arguments.")


def raise_empty_datapoint():
    raise ValueError("Please provide values and columns for datapoint")
