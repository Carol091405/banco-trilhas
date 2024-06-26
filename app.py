from fastapi import FastAPI
import sqlite3

app = FastAPI()
DATABASE = 'banco.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

@app.get('/')
def home():
    return 'Bem-vindo à API CRUD com FastAPI'

@app.on_event('startup')
async def startup_db():
    init_db()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('banco.db', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.get('/usiarios')
def initialize_database():
    init_db()
    return 'Banco de dados inicializado'
