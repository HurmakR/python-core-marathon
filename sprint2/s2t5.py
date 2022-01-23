import re


def max_population(data):
    result=max([re.findall(r"(\D[a-z]_\w+),([0-9]+)", i) for i in data][1])
    return result[0], int(result[1])
    