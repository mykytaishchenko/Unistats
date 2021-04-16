import flask
import aiofiles



app = flask.Flask('__main__',
                  static_folder='./front/build/static',
                  template_folder='./front/build')

@app.route('/')
def main():
    ### Process
    data = 'Main page' # Fetched data from db or api
    ###
    return flask.render_template('index.html', token=data) 

@app.route('/registration')
def registration():
    ### Process
    data = 'Registration'
    ###
    return flask.render_template('index.html', token=data)

@app.route('/profile')
def profile():
    ### Process
    data = 'Profile' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/universities')
def universities():
    ### Process
    data = 'Universities' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/lecturers')
def lecturers():
    ### Process
    data = 'Lecturers' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/login')
def login():
    ### Process
    data = 'Login' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/universities/<id>')
def university():
    ### Process
    data = 'Universities' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/lecturers/<id>')
def lecturer():
    ### Process
    data = 'Lecturers' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/lecturer/<id>/survey')
def lecturer_survey():
    ### Process
    data = 'Login' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/surveys/<id>')
def survey():
    ### Process
    data = 'Universities' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)

@app.route('/surveys')
def surveys():
    ### Process
    data = 'Lecturers' # Fetched data from db or api
    ### 
    return flask.render_template('index.html', token=data)


@app.route('/media/<id>')
def plotly_graph(id):
    ### Process
    data = 'Media' + str(id) # Fetched data from db or api
    ### 
    return flask.render_template('plotly_graph.html', token=data)


app.run(debug=True)
