from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
app = Flask(__name__)

sheet_id = "13UjTo_VkpwIndtWCmI_kNr56LHaiLZ2PIdn0jy6u-kw"
sheet_name = "Form-Response"
url = "https://docs.google.com/spreadsheets/d/"+sheet_id+"/gviz/tq?tqx=out:csv&sheet="+sheet_name
df = pd.read_csv(url)

@app.route("/", methods=['GET', 'POST'])
def selection_form():
    if request.method == "POST":
        selected_topic = request.form['topic']
        selected_difficulty = request.form['difficulty']
        #If mixed retrieve only by topic
        if selected_difficulty == "Mixed":
            data = df.loc[df['Topic'] == selected_topic]
        else:
        #Retrieve Data with given topic and difficulty
            data = df.loc[(df['Topic'] == selected_topic) & (df['Difficulty'] == selected_difficulty)]
        questions = data['Question'].to_list()
        return render_template('template.html', questions=questions, topic=selected_topic)
    return render_template('selection-form.html')

@app.route("/template", methods=['GET', 'POST'])
def template():
    return render_template('template.html', questions=[], topic=None )

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)