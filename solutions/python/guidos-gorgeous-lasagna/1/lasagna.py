EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Return the remaining bake time in minutes."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time in minutes."""
    return number_of_layers * 2


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the total elapsed cooking time."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time