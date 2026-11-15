from flask import Flask, request, render_template_string
app = Flask(__name__)
students = []
HTML = """
<h2>Student Result Management</h2>
<form method="POST">Name:<input name="name"><br>Marks:<input name="marks" type="number"><br><button>Add</button></form>
<hr>{% for s in students %}<p>{{s.name}} - {{s.marks}} - {{s.grade}}</p>{% endfor %}
"""
@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        m=int(request.form['marks']); g="A" if m>=90 else "B" if m>=75 else "C" if m>=50 else "F"
        students.append({"name":request.form['name'],"marks":m,"grade":g})
    return render_template_string(HTML, students=students)
if __name__=="__main__": app.run(debug=True)
