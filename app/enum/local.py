from enum import IntEnum

class Local(IntEnum):
    EXCEL = 1
    SASOI006 = 2
    RASCUNHO = 3
    TAGSELL = 4

def get_local_name(value):
    return Local(value).name
