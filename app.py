import os
import pandas as pd
from flask import Flask, render_template
from datetime import datetime, date

app = Flask(__name__)

@app.route("/")
def load_data():
    filepath = os.path.join("Resources", "cities.csv")
    df = pd.read_csv(filepath, index_col=0)
    df = df.assign(Date=pd.to_datetime(df["Date"], unit="s"))
    df["Date"] = [d.date() for d in df["Date"]]  

    table = df.to_html()
    return render_template("data.html", table=table)

if __name__ == "__main__":
    app.run(debug=True)