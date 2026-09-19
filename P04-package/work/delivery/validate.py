


def is_valid_order(order):
    if order["distance_km"] <= 0:
        return False
    if order["prep_time_min"] < 0:
        return False
    if order["traffic_level"] not in [1, 2, 3]:
        return False
    if order["rain"] not in [0, 1]:
        return False
    return True
