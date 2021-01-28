
def str_to_bool(s):

    if type(s) is bool:
        return s
    else:
        s = s.lower()
        if s == 'true':
            return True
        elif s == 'false':
            return False
        else:
            raise ValueError
