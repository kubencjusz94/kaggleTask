from flask import Flask, render_template
import pandas as pd
#from models import PoliceDepCalls
from settings import app

@app.route('/')
def show_data():
        file_path = "san-francisco/sf-police-calls-for-service-and-incidents/police-department-calls-for-service.csv"
        data = pd.read_csv(file_path)
        small_data = data.head(10)
        return render_template("data.html", data=small_data.to_html())

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
