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

app.index_string = '''<!DOCTYPE html>
<html>
<head>
<title>My app title</title>
<link rel="manifest" href="./assets/manifest.json" />
{%metas%}
{%favicon%}
{%css%}
</head>
<script type="module">
   import 'https://cdn.jsdelivr.net/npm/@pwabuilder/pwaupdate';
   const el = document.createElement('pwa-update');
   document.body.appendChild(el);
</script>
<body>
<script>
  if ('serviceWorker' in navigator) {
    window.addEventListener('load', ()=> {
      navigator
      .serviceWorker
      .register('./assets/sw01.js')
      .then(()=>console.log("Ready."))
      .catch(()=>console.log("Err..."));
    });
  }
</script>
{%app_entry%}
<footer>
{%config%}
{%scripts%}
{%renderer%}
</footer>
</body>
</html>
'''

app.layout = html.Div([
    dcc.Textarea(
        id='textarea-example',
        value='',
        style={'width': '100%', 'height': 300},
    ),
    html.Div(id='textarea-example-output', style={'whiteSpace': 'pre-line'})
])

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

    return f'This session is {session["my_sess"]}'




if __name__ == '__main__':
    app.run_server(debug=False)
