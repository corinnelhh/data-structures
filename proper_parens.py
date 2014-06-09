def paren_checker(our_string):
    open_paren = 0
    for char in our_string:
        if char == u'(':
            open_paren += 1
        elif char == u')':
            open_paren -= 1
        if open_paren < 0:
            return -1
    return 1 if open_paren else 0
