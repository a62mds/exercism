def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, (list, tuple)):
            item = flatten(item)
            flat_list.extend(subitem for subitem in item)
        elif item is not None:
            flat_list.append(item)
    return flat_list
