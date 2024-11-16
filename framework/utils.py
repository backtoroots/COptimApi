from uuid import UUID


def reverse_line(input_string):
    """Reverse the line"""
    input_string = input_string.lower().replace(' ', '')
    return input_string[::-1]


def is_valid_uuid(uuid_to_test, version=4):
    """
        Check if string is a valid UUID
    Args:
        uuid_to_test: String to check for UUID format
        version: Version of UUID

    Returns:
        If input string is a valid UUID
    """
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test
