def study_schedule(permanence_period, target_time):
    if (
        not (isinstance(target_time, int))
        or not (isinstance(permanence_period, list))
        or (len(permanence_period) == 0)
    ):
        return None
    acc = 0

    for deltaS0, deltaS in permanence_period:
        if not (isinstance(deltaS0, int) and isinstance(deltaS, int)):
            return None
        elif deltaS0 <= target_time <= deltaS:
            acc += 1
    return acc
