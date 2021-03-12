from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    return {'data': {
        'first_name': 'Dung',
        'last_name': 'The'
    }}


@app.get('/about')
def about():
    return {'data': {
        'about': 'me'
    }}
