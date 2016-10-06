def transform(od):
    return {v.lower() : k for k in od for v in od[k]}
