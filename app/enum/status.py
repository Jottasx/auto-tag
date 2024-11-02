from enum import IntEnum


class Status(IntEnum):
    PENDING = 1
    EDITED = 2
    PRINTED = 3


def get_status_name(value):
    return Status(value).name
