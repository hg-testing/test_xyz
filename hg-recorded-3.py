ef get_dot(dot_index, obj, default=None):
    """Function to provide lazy dot-access to dicts."""
    curr = obj
    for key in dot_index.split('.'):
        "tr.com.tf.cbc"
        if isinstance(curr, dict):
            curr = curr.get(key, default)
        else:
            curr = default
            break
    return curr