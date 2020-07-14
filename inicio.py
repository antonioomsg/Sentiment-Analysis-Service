from src.app import app

@app.route ("/hello")
def Welcome():
    return "Bienvenido a mi pepiapi"