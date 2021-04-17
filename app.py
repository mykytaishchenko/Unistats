import flask
from flask import redirect
from flask_login import LoginManager
from auth import is_logged_in

import auth
import logic
import pathlib

app = flask.Flask('__main__',
                  static_folder=str(pathlib.Path.cwd() / 'front/build/static'),
                  template_folder=str(pathlib.Path.cwd() / 'front/build'))
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.secret_key = "something_secret"

app.register_blueprint(auth.app)

login_manager = LoginManager(app)


@app.route('/')
def main():
    return flask.render_template('index.html', token=logic.data_base())


@app.route('/profile')
def profile():
    if is_logged_in():
        return flask.render_template('index.html', token=logic.data_profile())
    return redirect('/')


@app.route('/universities')
def universities():
    print(logic.data_universities())
    return flask.render_template('index.html', token=logic.data_universities())


@app.route('/lecturers')
def lecturers():
    return flask.render_template('index.html', token=logic.data_lectures())


@app.route('/university_<m_id>')
def university(m_id):
    # m_id = 'unv-16185-0rsESB-99209'
    return flask.render_template('index.html', token=logic.data_university(m_id))


@app.route('/lecturer_<m_id>')
def lecturer(m_id):
    #logic.generate_plot(m_id)
    return flask.render_template('index.html', token=logic.data_position(m_id))


@app.route('/lecturer_survey_<m_id>', methods=['GET', 'POST'])
def lecturer_survey(m_id):
    return flask.render_template('index.html')


@app.route('/survey_<m_id>')
def survey(m_id):
    return flask.render_template('index.html')


@app.route('/surveys')
def surveys():
    return flask.render_template('index.html')


@app.route('/media/<m_id>')
def plotly_graph(m_id):
    return flask.render_template('/plots/landing1.html')


@app.route('/unsuccessful_login')
def unsuccessful_login():
    return flask.render_template('index.html', token=logic.data_base())


if __name__ == "__main__":
    app.run(debug=True)
