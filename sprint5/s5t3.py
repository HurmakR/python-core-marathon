import re


def valid_email(mail):
    try:
        if mail.count('@') == 1 and \
        re.fullmatch(r'[A-Za-z0-9]+@[a-z]+\.?[a-z]+\.?[a-z]+',mail):
            return 'Email is valid'
        else:
            raise ValueError('Email is not valid')
    except ValueError as e:
        return e
