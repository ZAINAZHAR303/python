

from flask import Flask,render_template,request,redirect,url_for,flash

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:''@localhost/list_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.secret_key='secret key'
db=SQLAlchemy(app)

class Task(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    emp_name=db.Column(db.String(120),nullable=False)
    task=db.Column(db.String(200),nullable=False)
    def __init__(self,emp_name,task):
        self.emp_name=emp_name
        self.task=task

@app.route('/')
def first_page():
    return render_template("first_page.html")


    

@app.route('/add_task', methods=['get','POST'])
def add_task():
    if request.method=='POST':
        
        emp_name = request.form['emp_name']
        task=request.form['task']
        new_task = Task(emp_name,task)
        db.session.add(new_task)
        db.session.commit()
        
        flash("Task Has Been Successfully submitted!")
        return redirect(url_for('add_task'))
    return render_template('add_task.html')

@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        task_id = request.form.get('task.id')
        old_task = Task.query.get(task_id)
        
        old_task.emp_name = request.form['emp_name']
        old_task.task = request.form['task']
        db.session.commit()
        flash("Task updated successfully!")
    
            
    return redirect(url_for('view_task'))  # Redirect to view tasks after update

@app.route("/delete/<int:id>/", methods = ['GET','POST'])
def delete(id):
    my_data = Task.query.get(id)
    
    if my_data:
        db.session.delete(my_data)
        db.session.commit()
        flash("Task deleted successfully.")
    else:
        flash("Task not found.")
    
    return redirect(url_for("delete_task"))

@app.route("/view_task")
def view_task():
    task = Task.query.all()
    return render_template("view_task.html",tasks=task)
@app.route("/edit_task")
def edit_task():
    tasks= Task.query.all()
    return render_template("edit_task.html",tasks=tasks)

@app.route("/delete_task")
def delete_task():
    tasks= Task.query.all()
    return render_template("delete_task.html",tasks=tasks)

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
app.run(debug=True)
