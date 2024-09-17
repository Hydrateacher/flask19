from flask import Flask, render_template, redirect, url_for, session, request
from pymongo import MongoClient
import requests
from uuid import uuid4 
# MongoDB-ga bog'lanish
client = MongoClient('mongodb+srv://doadmin:56Hx14L97FMUYv23@db-mongodb-fra1-82504-ec7e84b0.mongo.ondigitalocean.com/admin?tls=true&authSource=admin&replicaSet=db-mongodb-fra1-82504')
db = client['NEW']
collection = db['dustim']
collection3 = db['talaba']
collection2 = db['baho']


app = Flask(__name__)
app.secret_key = 'supersecretkey'




@app.route('/')
def index():    
    return render_template('index.html')

# dustlarim
@app.route('/dustlarim', methods=['GET', 'POST'])
def dustlarim():
    if request.method == 'POST':
        name = request.form.get('friend')
        are = request.form.get('are')      
        
        if name  and are:
            collection.insert_one({'name': name, 'are': are})
            
            render_template('dustlarim.html')        
        
    # Ma'lumotlarni olish
    friends = list(collection.find({})) 
    
    # Ma'lumotlarni HTML sahifasiga uzatish
    return render_template('dustlarim.html', friends=friends)



# baho
@app.route('/baho', methods=['GET', 'POST'])
def baho():
    if request.method == 'POST':
        name = request.form.get('name')
        ball = request.form.get('ball')      
        
        if name  and ball:
            collection2.insert_one({'name': name, 'ball': ball})
            
            render_template('baho.html')        
        
    # Ma'lumotlarni olish
    balls = list(collection2.find({}))
    
    # Ma'lumotlarni HTML sahifasiga uzatish
    return render_template('baho.html', balls=balls)    



# students
@app.route('/talaba', methods=['GET', 'POST'])
def talaba():
    if request.method == 'POST':
        name = request.form.get('student')
        are = request.form.get('are')
        course = request.form.get('course')
              
        
        if name  and are and course:
            collection3.insert_one({'name': name, 'are': are, 'course': course})
            
            render_template('talaba.html')        
        
    # Ma'lumotlarni olish
    students = list(collection3.find({}))
    
    # Ma'lumotlarni HTML sahifasiga uzatish
    return render_template('talaba.html', students=students)







  
  

if __name__ == '__main__':
    app.run(debug=True)




