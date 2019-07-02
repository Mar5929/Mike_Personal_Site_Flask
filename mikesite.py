from flask import Flask, render_template, url_for
app = Flask(__name__)

#set route for page
@app.route("/")
@app.route("/home")
def home():
    # set template here so that you don't need to have html all on this python file.
    return render_template('home.html', title='Home')

#set route for page
@app.route("/about")
def about():
    return render_template('about.html', title='About')

# "__name__" is a variable that python sets to '__main__' if the program is run directly and not imported
if __name__ == '__main__':
    app.run(debug=True)