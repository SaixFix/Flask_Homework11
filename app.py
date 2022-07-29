from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)


@app.route("/")
def main_page():
    """
    Главная страница со списком всех кандидатов
    """
    list_candidates: list[dict] = load_candidates_from_json()
    return render_template('list.html', candidates=list_candidates)


@app.route("/candidate/<int:uid>")
def personal_page(uid):
    """
    Страница с информацией о кондидате по номеру
    """
    candidate: dict = get_candidate(uid)
    return render_template(' card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidates_by_name(candidate_name):
    """
    Страница с информацией о кондидате по имени
    """
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates)


@app.route("/skill/<candidate_skill>")
def search_candidates_by_skill(candidate_skill):
    """
    Страница с информацией о кондидате по скилу
    """
    candidates: list[dict] = get_candidates_by_skill(candidate_skill)
    return render_template('skill.html', candidates=candidates)



app.run()