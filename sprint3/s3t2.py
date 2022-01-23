def create(outer_arg):
    return lambda inner_arg: True if inner_arg == outer_arg else False
            