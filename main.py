from dash import Dash, dcc, html
from dash import *
from dash.dependencies import Input, Output
import opentok
from flask import Flask, session

# app = Dash(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

server = Flask(__name__)
server.config['SECRET_KEY'] = 'super secret key'
app = Dash(server=server, external_stylesheets=external_stylesheets)

# app.config['SESSION_TYPE'] = 'memcached'

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-example',
        value='',
        style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])

# @app.callback(
#     Output('textarea-example-output', 'children'),
#     Input('textarea-example', 'value')
# )
# def update_output(value):
#     print('start call back')
#     print(f"this is session {session.get('my_sess', None)}")
#     if not session.get('my_sess'):
#         session['my_sess'] = 4332
#     else:
#         session['my_sess'] = value
#
#     # return 'You have entered: \n{}'.format(value)
#     return 'You have entered: \n\n\n\n\n{}'.format(session.get('my_sess', 'None'))


app.layout = html.Div([
    html.Div(dcc.Input(id='input-box', type='text')),
    html.Button('Submit', id='button-example-1'),
    html.Div(id='output-container-button',
             children='Enter a value and press submit')
])


@app.callback(
    dependencies.Output('output-container-button', 'children'),
    [dependencies.Input('button-example-1', 'n_clicks')],
    [dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
    if session.get('my_sess'):
        session['my_sess'] = 'old'
    else:
        session['my_sess'] = 'new'

    return f'This {session["my_sess"]}'




if __name__ == '__main__':
    app.run_server(debug=False)
