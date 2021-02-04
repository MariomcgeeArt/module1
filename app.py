# imports the flask library
from flask import Flask

#app variable so that we can start writing routes
app = Flask(__name__)



# # indicates the URL of the web page we’ll need to visit in order to see our result. In this case, it’s / or the home page.
# @app.route('/')
# #  defines the route function. Whatever this function returns will show up in your browser when you visit the appropriate URL!
# def homepage():
#     """Shows a greeting to the user."""
#     # returns the page contents.
#     return 'Are you there, world? It\'s me, Ducky!'

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'


@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Displays users favorite animal"""
    return f"Cool, {users_animal} is my favorite too! "


@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    """Displays users favorite dessert"""
    return f"How did tyou know i liked {users_dessert} ? "


   # Write a route for the URL /madlibs/<adjective>/<noun> which takes in 2 strings and displays a funny (but work-appropriate) story using them!

@app.route('/madlibs/<adjective>/<noun>')
def mad_lib(adjective, noun):
    """takes and adjective and a noun returns a madlib"""
    return f" The ships {adjective} over the head of {noun} until it crashed into the moon."










#telly python how to run the server 
if __name__ == '__main__':
    app.run(debug=True)
