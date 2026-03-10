from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
<title>Credit Card Spending Analyzer</title>
<style>
body{
font-family:Arial;
background:#eef2f7;
text-align:center;
padding:40px;
}
.container{
background:white;
padding:30px;
border-radius:10px;
width:65%;
margin:auto;
box-shadow:0 0 10px rgba(0,0,0,0.1);
}
button{
padding:10px 20px;
background:#007bff;
border:none;
color:white;
cursor:pointer;
border-radius:5px;
}
button:hover{
background:#0056b3;
}
</style>
</head>
<body>
<div class="container">
<h1>Credit Card Spending Analyzer</h1>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="file" required>
<br><br>
<button type="submit">Analyze Spending</button>
</form>

{% if total %}
<h2>Total Spending: ₹{{total}}</h2>
<h3>Largest Transaction: ₹{{largest}}</h3>
<h3>Category-wise Spending</h3>
<ul>
{% for c,a in categories.items() %}
<li>{{c}} : ₹{{a}}</li>
{% endfor %}
</ul>
{% endif %}

</div>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def home():
    total = None
    largest = None
    categories = None

    if request.method == "POST":
        file = request.files["file"]
        df = pd.read_csv(file)

        total = df["Amount"].sum()
        largest = df["Amount"].max()
        categories = df.groupby("Category")["Amount"].sum().to_dict()

    return render_template_string(HTML_PAGE,
                                  total=total,
                                  largest=largest,
                                  categories=categories)

if __name__ == "__main__":
    app.run(debug=True)