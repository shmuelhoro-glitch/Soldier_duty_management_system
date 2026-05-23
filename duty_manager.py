from utils import find_soldier_by_id,soldier_has_duty,is_valid_day,is_valid_status,find_duty_by_name

def add_duty_to_soldier(soldier_id: int, duty_name: str, day: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier == None:
        raise KeyError("ID isn't exists")
    elif soldier_has_duty(duty_name):
        raise ValueError("A duty with this name already exists for a soldier ")
    elif not is_valid_day(day):
        raise ValueError("Invalid day")
    else:
        soldier["duties"].append({"name":duty_name,"day":day,"status":"pending"})


def update_duty_status(soldier_id: int, duty_name: str, new_status: str) -> None:
    soldier = find_soldier_by_id(soldier_id)
    if soldier == None:
        raise KeyError("ID isn't exists")
    elif not soldier_has_duty(soldier,duty_name):
        raise KeyError("A duty with this name was not found for a soldier")
    elif not is_valid_status(new_status):
        raise ValueError("The new status is invalid")
    else:
        duty = find_duty_by_name(soldier["duties"],duty_name)
        duty["status"] = new_status



def get_soldier_duties(soldier_id: int) -> list:
    soldier = find_soldier_by_id(soldier_id)
    if soldier == None:
        raise KeyError("ID isn't exists")
    else:
        return soldier["duties"]


