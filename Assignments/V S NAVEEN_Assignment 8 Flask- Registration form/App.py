from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML Template
html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Registration Form</title>
</head>
<body>

    <h2>Student Registration Form</h2>

    <form method="POST">

        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>

        <label>Password:</label><br>
        <input type="password" name="password" required><br><br>

        <input type="submit" value="Register">

    </form>

    <h3>{{ message }}</h3>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def register():

    message = ""

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Simple Validation
        if name == "" or email == "" or password == "":
            message = "Please fill all fields"

        else:
            message = f"Registration Successful for {name}"

    return render_template_string(html_page, message=message)

# Run app
if __name__ == "__main__":
    app.run(debug=True)