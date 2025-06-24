from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/fabric-types')
def fabric_types():
    return render_template("fabric_types.html")

@app.route('/weaving-techniques')
def weaving_techniques():
    return render_template("weaving_techniques.html")

@app.route('/modern-trends')
def modern_trends():
    return render_template("modern_trends.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        writer = csv.writer('file')
        print(f"Name: {name}, Email: {email}, Message: {message}")  # You can save this to a file or database

# Save to CSV
        with open('contact_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, email, message])
        return redirect(url_for('home'))
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)
