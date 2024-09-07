from flask import Flask, Response, render_template, request, redirect, flash, session
from model import User, Event, connect_to_db, db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# @app.route('/')
# def homepage():
#     """View homepage."""

#     return render_template("homepage.html")

@app.route("/", methods=["GET", "POST"])
def homepage():
    """Display homepage"""
    # email = session.get("email")
    # if email:
    #     return redirect("/schedule")
    return render_template("homepage.html")

# @app.route("/get-email")
# def get_email():
#     """Store the name in a session"""
#     email = request.args.get("email")
#     session["email"] = email
#     return redirect("/schedule")

def get_user_from_session() -> User | None:
    user_email = session.get("user_email")
    if user_email:
        return crud.get_user_by_email(user_email)
    else:
        return None

@app.route("/signup", methods=["POST", "GET"])
def register_user():
    """Create a new user."""

    user_email = request.form.get("user_email")
    if crud.get_user_by_email(user_email):
        flash("Email already in use. Try using a different password.")
        return redirect("/login")
    else:
        user = crud.create_user(user_email)
        flash("Account created!")
        return redirect("/login")

@app.route("/login")
def show_login_page():
    """Show login page."""
    return render_template("login.html")

@app.route("/login", methods=["POST", "GET"])
def process_login():
    """Process user login."""

    user_email = request.form.get("user_email")
    user = crud.get_user_by_email(user_email)


    return render_template("schedule.html", user=user)

@app.route('/schedule', methods=["GET","POST"])
def schedule():
    """Show calendar scheduling form."""
    email = session.get("email")
    if email:
        return render_template('schedule.html', email=email)

@app.route('/booking')
def booking():
    """Show the results from the scheduling form."""

    return render_template('booking.html')

# @app.route('/events')
# def events():
#     """Show events homepage."""
#     user = get_user_from_session()
#     if not user:
#         flash(f"Please login first")
#         return render_template('login.html')
#     user_booked_events = crud.get_events_for_a_given_user(user)
#     return render_template('favorites.html', user_booked_events=user_booked_events)

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=6060)