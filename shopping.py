from myapp import create_app
from myapp.logs import create_logger

app=create_app()

if __name__=="__main__":
    create_logger()
    app.run(debug=True)