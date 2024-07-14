def human_size(bytes, units=[' bytes','KB','MB','GB','TB', 'PB', 'EB']):
    """ Returns a human readable string representation of MB """
    return str(MB) + units[0] if int(MB) < 1024 else human_size(int(MB)>>10, units[1:])
