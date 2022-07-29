import json


def load_candidates_from_json() -> list[dict]:
    """
    Читает из файла и возвращает список кандидатов
    """
    with open('candidates.json', 'r', encoding='utf-8') as file:
        list_candidates = json.load(file)
        return list_candidates


def get_candidate(candidate_id: str) -> dict:
    """
    возвращает одного кандидата по его id
    """
    for i in load_candidates_from_json():
        if int(candidate_id) == i['id']:
            return i


def get_candidates_by_name(candidate_name: str) -> dict:
    """
    возвращает кандидатов по имени
    """
    list_candidates = []
    for i in load_candidates_from_json():
        if candidate_name.lower() in i['name'].lower():
            list_candidates.append(i)

    return list_candidates


def get_candidates_by_skill(skill_name: str) -> dict:
    """
    возвращает кандидатов по навыку
    """
    list_candidates = []
    for i in load_candidates_from_json():
        if skill_name.lower() in i['skills'].lower():
            list_candidates.append(i)

    return list_candidates

