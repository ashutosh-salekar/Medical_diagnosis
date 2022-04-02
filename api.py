from flask import Flask, render_template, request
from joblib import load

app = Flask(__name__)

@app.route('/',methods=['POST','GET'])
def hello():
    return render_template('home.html')

@app.route('/Select_disease',methods=['POST','GET'])
def select():
    select = request.form['Disease']
    print(select)
    if select == 'breastcancer':
        return render_template('BreastCancer.html')
    elif select == 'diabetes':
        return render_template('Diabetes.html')
    elif select == 'liver':
        return render_template('Liver.html')

# 1. Breast Cancer
@app.route('/breastcancer_data',methods=['POST','GET'])
def breast_cancer():
    feat = request.form.to_dict()
    feat = list(feat.values())
    model = load('E:\Ashu\My Codes\Tutorials\Machine Learning\Projects ML\Health_App\Models\BreastCancer_Model.joblib')
    result = model.predict([feat])
    if result == 0:
        diagnosis = 'No Breast cancer detected'
    else:
        diagnosis = 'Breast cancer detected'
    return render_template('Output.html',key= diagnosis)

# 2. Diabetes
@app.route('/diabetes_data',methods=['POST','GET'])
def diabetes():
    feat = request.form.to_dict()
    feat = list(feat.values())
    model = load('E:\Ashu\My Codes\Tutorials\Machine Learning\Projects ML\Health_App\Models\Diabetes_Model.joblib')
    result = model.predict([feat])
    if result == 0:
        diagnosis = 'No Diabetes detected'
    else:
        diagnosis = 'Diabetes detected'
    return render_template('Output.html',key= diagnosis)

# 3. Liver disease 
@app.route('/liver_data',methods=['POST','GET'])
def liver():
    feat = request.form.to_dict()
    feat = list(feat.values())
    model = load('E:\Ashu\My Codes\Tutorials\Machine Learning\Projects ML\Health_App\Models\Liver_Model.joblib')
    result = model.predict([feat])
    if result == 1:
        diagnosis = 'No Liver disease detected'
    else:
        diagnosis = 'Liver disease detected'
    return render_template('Output.html',key= diagnosis)
    
if __name__ == "__main__":
    app.run(debug=True)
