import json


def load_candidates_from_json():
    '''возвращает список всех кандидатов'''
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)

    return candidates


def get_candidate(candidate_id):
    '''возвращает одного кандидата по его id'''
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            return candidate

    return None


def get_candidates_by_name(candidate_name):
    '''возвращает кандидатов по имени'''
    candidates = load_candidates_from_json()
    names_candidates = []
    name_lower = candidate_name.lower()

    for candidate in candidates:
        candidate_name = candidate['name'].lower()
        if name_lower in candidate_name:
            names_candidates.append(candidate)

    return names_candidates


def get_candidates_by_skill(skill_name):
    '''возвращает кандидатов по навыку'''
    candidates = load_candidates_from_json()
    skilled_candidates = []
    skill_lower = skill_name.lower()

    for candidate in candidates:
        candidate_skills = candidate['skills'].lower().split(', ')
        if skill_lower in candidate_skills:
            skilled_candidates.append(candidate)

    return skilled_candidates


def preformatted_list(candidates):
    '''Функция форматирует полученные данные в HTML'''
    page_content = ''

    for candidate in candidates:
        page_content += candidate['name'] + '\n'
        page_content += candidate['position'] + '\n'
        page_content += candidate['skills'] + '\n'
        page_content += '\n'

    return '<pre>' + page_content + '</pre>'


print(load_candidates_from_json())
print(get_candidate(2))
print(get_candidates_by_name('burt'))
print(get_candidates_by_skill('html'))
