import json

from flask import Blueprint, render_template

from functions import new_logger

error_bp = Blueprint("errors_bp", __name__)


@error_bp.errorhandler(404)
@error_bp.errorhandler(json.JSONDecodeError)
@error_bp.errorhandler(FileNotFoundError)
@error_bp.errorhandler(TypeError)
def file_not_found(e):
    new_logger.error(f"Файл не найден или не может быть прочитан {e}")
    text = "Файл не найден или не может быть прочитан"
    return render_template('404.html', e=text)


@error_bp.errorhandler(500)
def error_server():
    text = "У нас, что-то сломалось, но мы скоро это починим"
    new_logger.error(f"Поломка на сервере")
    return render_template('500.html', e=text)
