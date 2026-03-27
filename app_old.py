from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("hello.html")


#Hello World route
@app.route("/hello")
def hello():
    return render_template("hello.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/about-css')
def about_css():
    return render_template('about-css.html')

@app.route('/favorite-course')
def favorite_course():
    subject = request.args.get('subject', '')
    course_number = request.args.get('course_number', '')

    course = f"{subject} {course_number}".strip()
    return render_template('favorite-course.html', course=course)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name', '')
        last_name = request.form.get('last_name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        return render_template(
            'contact.html',
            submitted=True,
            first_name=first_name,
            last_name=last_name,
            email=email,
            message=message
        )

    return render_template('contact.html', submitted=False)

if __name__ == "__main__":
    app.run(debug=True)