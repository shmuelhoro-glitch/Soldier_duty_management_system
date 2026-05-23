from data import soldiers_data


def find_soldier_by_id(soldier_id: int) -> dict | None:
    for soldier in soldiers_data:
        if soldier["id"] == soldier_id:
            return soldier
    return None

def find_duty_by_name(duties: list, duty_name: str) -> dict | None:
    for duty in duties:
        if duty == duty_name:
            return duty
    return None

def is_valid_status(status: str) -> bool:
    if status in ["pending","completed","missed"]:
        return True
    return False


def is_valid_name(name: str) -> bool:
    if name not in [""," ",None,"  "]:
        return True
    return False


def soldier_has_duty(soldier: dict, duty_name: str) -> bool:
    for duty in soldier["duties"]:
        if duty["name"] == duty_name:
            return True
    return False


def is_valid_day(day: str) -> bool:
    if day in ["sunday","monday","tuesday","wednesday","thursday"]:
        return True
    return False
