#!/usr/bin/env python3
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

def get_user():
    login_as = request.args.get('login_as')
    if login_as:
        user = users.get(int(login_as))
        return user
    return None

@app.before_request
def before_request():
    g.user = get_user()

@babel.localeselector
def get_locale():
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    # 3. Locale from request header
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.context_processor
def inject_locale():
    return dict(get_locale=get_locale)

@app.route('/')
def index():
    return render_template('6-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

