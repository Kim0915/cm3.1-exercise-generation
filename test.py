import pandas as pd
sheet_id = "13UjTo_VkpwIndtWCmI_kNr56LHaiLZ2PIdn0jy6u-kw"
sheet_name = "Form-Response"
url = "https://docs.google.com/spreadsheets/d/"+sheet_id+"/gviz/tq?tqx=out:csv&sheet="+sheet_name
data = pd.read_csv(url)
questions_from_data = data.loc[(data['Topic'] == "While Loops") & (data['Difficulty'] == "Advanced")]
questions = questions_from_data['Question']
print(len(questions.to_list()))