from data import soldiers_data
from utils import find_soldier_by_id,is_valid_name

def add_soldier(soldier_id: int, name: str) -> None:
    if find_soldier_by_id(soldier_id):
        raise ValueError("id exists")
    elif not is_valid_name(name):
        raise ValueError("invalid name")
    else:
        soldiers_data.append({"id":soldier_id,"name":name,"duties":[]})

def remove_soldier(soldier_id: int) -> None:
    if find_soldier_by_id(soldier_id) == None:
        raise KeyError("id isn't exists")
    else:
        for soldier in soldiers_data:
            if soldier["id"] == soldier_id:
                soldiers_data.remove(soldier)
                break

def get_all_soldiers() -> list:
    return soldiers_data

