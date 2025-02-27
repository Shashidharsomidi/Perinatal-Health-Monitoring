from flask import Flask, render_template, request
import pandas as pd
import pickle 

app = Flask(__name__)  

# Load the saved model  
with open('model2.pkl', 'rb') as file:
    randomForest = pickle.load(file)

train_accuracy = 0.90
test_accuracy = 0.95

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'admin@gmail.com' and password == 'admin':
            msg = "Logged in successfully !"
            return render_template('index.html', msg=msg)
        else:
            msg = "Invalid credentials or error"
            return render_template('login.html', msg=msg)
    return render_template('login.html')





@app.route('/insert', methods=['POST'])
def insert():  
    if request.method == 'POST':
        Age = int(request.form['age'])
        Feeling_sad_or_Tearful = int(request.form['feeling_sad_or_Tearful'])
        Irritable_towards_baby_and_partner = int(request.form['irritable_towards_baby_or_partner'])
        Trouble_sleeping_at_night = int(request.form['trouble_sleeping_at_night'])
        Problems_concentrating_or_making_decision = int(request.form['problems_concentrating_or_making_decision'])
        Overeating_or_loss_of_appetite = int(request.form['overeating_or_loss_of_appetite'])
        Feeling_anxious = int(request.form['feeling_anxious'])
        Feeling_of_guilt = int(request.form['feeling_of_guilt'])
        Problems_of_bonding_with_baby = int(request.form['problems_of_bonding_with_baby'])
        
        # Create a DataFrame from user input
        new_data = pd.DataFrame({
            'Age': [Age],
            'Feeling sad or Tearful': [Feeling_sad_or_Tearful],
            'Irritable towards baby & partner': [Irritable_towards_baby_and_partner],
            'Trouble sleeping at night': [Trouble_sleeping_at_night],
            'Problems concentrating or making decision': [Problems_concentrating_or_making_decision],
            'Overeating or loss of appetite': [Overeating_or_loss_of_appetite],
            'Feeling anxious': [Feeling_anxious],
            'Feeling of guilt': [Feeling_of_guilt],
            'Problems of bonding with baby': [Problems_of_bonding_with_baby],
        })

        # Prediction step
        prediction = randomForest.predict(new_data)
        
        if prediction == 0:
            result = "No Anxiety-No Depression"
        elif prediction == 1:
            result = "Anxiety and/or Depression"
        else:
            result = "Normal"
        
        return render_template('index.html', prediction=result)
    
    
    
    
    
    


@app.route('/performance')
def performance():
    return render_template('performance.html', train_accuracy=train_accuracy, test_accuracy=test_accuracy)

@app.route("/logout")
def logout():
    return render_template("home.html")



if __name__ == '__main__':  
   app.run(debug=False)  