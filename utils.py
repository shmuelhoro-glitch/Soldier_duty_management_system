from data import soldiers_data

"""Check if a id is exists in the system"""
def find_soldier_by_id(soldier_id: int) -> dict | None:
    for soldier in soldiers_data:
        if soldier["id"] == soldier_id:
            return soldier
    return None

"""Searching for a shift by name in the list of shifts"""
def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty == duty_name:
            return duty
    return None

"""Checks if a status is valid"""
def is_valid_status(status: str) -> bool:
    if status in ["pending","completed","missed"]:
        return True
    return False


"""Checks if the name is valid (not empty)"""
def is_valid_name(name: str) -> bool:
    if name not in [""," ",None,"  "]:
        return True
    return False

"""Checks if a soldier has a duty with a specific name"""
def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
    return False


"""Checks if the day is valid (not Friday or Saturday)"""
def is_valid_day(day: str) -> bool:
    if day in ["sunday","monday","tuesday","wednesday","thursday"]:
        return True
    return False
