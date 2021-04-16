import flask
from flask_login import LoginManager

import auth

app = flask.Flask('__main__',
                  static_folder='./front/build/static',
                  template_folder='./front/build')
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.secret_key = "something_secret"

app.register_blueprint(auth.app)

login_manager = LoginManager(app)


@app.route('/')
def main():
    data = 'Main page'
    return flask.render_template('index.html', token=data)


@app.route('/registration')
def registration():
    data = 'Registration'
    return flask.render_template('index.html', token=data)


@app.route('/profile')
def profile():
    data = 'Profile'
    return flask.render_template('index.html', token=data)


@app.route('/universities')
def universities():
    data = 'Universities'
    return flask.render_template('index.html', token=data)


@app.route('/lecturers')
def lecturers():
    data = 'Lecturers'
    return flask.render_template('index.html', token=data)


@app.route('/university_<m_id>')
def university(m_id):
    data = 'Universities'
    return flask.render_template('index.html', token=data)


@app.route('/lecturer_<m_id>')
def lecturer(m_id):
    data = 'Lecturers'
    return flask.render_template('index.html', token=data)


@app.route('/lecturersurvey_<m_id>')
def lecturer_survey(m_id):
    data = 'Login'
    return flask.render_template('index.html', token=data)


@app.route('/survey_<m_id>')
def survey(m_id):
    data = 'Universities'
    return flask.render_template('index.html', token=data)


@app.route('/surveys')
def surveys():
    data = 'Lecturers'
    return flask.render_template('index.html', token=data)


@app.route('/media/<m_id>')
def plotly_graph(m_id):
    data = 'Media' + str(m_id)
    return flask.render_template('plotly_graph.html', token=data)


if __name__ == "__main__":
    app.run(debug=True)
