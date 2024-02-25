from flask import Flask, render_template, request
import smtplib
import requests

response = requests.get(url="https://api.npoint.io/78dc61d8bc398d944eac")
data = response.json()

app = Flask(__name__)

CONTACT_MESSAGE1 = "Contact Me"
CONTACT_MESSAGE2 = "Successfully sent message"
MY_EMAIL = '100dctestemail@gmail.com'
PASSWORD = 'jgixqoedcqpsukam'


@app.route('/')
def homepage():
    return render_template("index.html", blog_data=data)


@app.route('/about')
def about_page():
    return render_template("about.html")


# Method 'GET' identifies user opening up the page normally. Method 'POST' detects when user submits the contact form.
# Therefore, 'GET' will return the default contact.html file, 'POST' will return contact.html with different h1, and
# gets the user input using request.form[]. User input using smtplib sent through email for documentation.

@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'GET':
        return render_template("contact.html", message=CONTACT_MESSAGE1)
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs='marcellusgerson@gmail.com',
                                msg=f"Subject:{name} Data\n\n Name:{name}\nEmail:{email}\nPhone Number:{phone}\n"
                                    f"Message:{message}")
        return render_template("contact.html", message=CONTACT_MESSAGE2)


@app.route('/post/<int:num>')
def post_page(num):
    return render_template("post.html", blog_data=data, post_num=num)


if __name__ == "__main__":
    app.run(debug=True)
