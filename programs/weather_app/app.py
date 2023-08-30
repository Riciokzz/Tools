import os
import requests
import folium


from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash


from helpers import apology, login_required

# Global var
api_key = "843f2df61df84f23859950256faf0cfc"

# Get date and format it for later use
now = datetime.now()
date_form = now.strftime("%Y-%m-%d")
date_time = now.strftime("%Y-%m-%dT%H:00")

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///project.db")


def get_wind_direction(degrees):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    d_index = round(degrees / 45) % 8
    return directions[d_index]


def get_city():
    """Get city from session or use default value"""
    if session.get("city") is None:
        return "Vilnius"
    else:
        return session.get("city")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show main"""

    city = get_city()

    geo_url = f'https://api.opencagedata.com/geocode/v1/json?' \
              f'q={city}&' \
              f'key={api_key}'
    geo_response = requests.get(geo_url)

    # Parse json response
    geo_data = geo_response.json()

    # Access coordinate data
    session["lat"] = geo_data['results'][0]['geometry']['lat']
    session["lon"] = geo_data['results'][0]['geometry']['lng']

    # Get weather data
    weather_url = f"https://api.open-meteo.com/v1/forecast?" \
                  f"latitude={session['lat']}&" \
                  f"longitude={session['lon']}&" \
                  f"hourly=temperature_2m," \
                  f"relativehumidity_2m," \
                  f"rain," \
                  f"cloudcover," \
                  f"windspeed_10m," \
                  f"winddirection_10m," \
                  f"uv_index&" \
                  f"timezone=auto"
    weather_response = requests.get(weather_url)

    # Parse weather json response
    weather_data = weather_response.json()

    # Find the index of the nearest hour in the time list
    nearest_hour_index = weather_data['hourly']['time'].index(date_time)

    # Set up different period data
    hour_data = {}
    part_data = {}
    week_data = {}
    for key, values in weather_data['hourly'].items():
        hour_data[key] = [values[i] for i in range(0, 24)]
        part_data[key] = [values[i] for i in [0, 4, 8, 12, 16, 20, 23]]
        week_data[key] = [values[i] for i in range(len(values)) if i % 12 == 0]

    # Save data to session
    session["week"] = week_data

    # Extract the data for the nearest hour
    w_temp = weather_data['hourly']['temperature_2m'][nearest_hour_index]
    w_humidity = weather_data['hourly']['relativehumidity_2m'][nearest_hour_index]
    w_rain = weather_data['hourly']['rain'][nearest_hour_index]
    w_cloud = weather_data['hourly']['cloudcover'][nearest_hour_index]
    w_wind = weather_data['hourly']['windspeed_10m'][nearest_hour_index]
    w_direc = weather_data['hourly']['winddirection_10m'][nearest_hour_index]
    w_uv = weather_data['hourly']['uv_index'][nearest_hour_index]
    direction = get_wind_direction(w_direc)

    # Set up map
    # Create a Leaflet map centered around the coordinates
    page_map = folium.Map(location=[session["lat"], session["lon"]], zoom_start=12)

    # Add a marker at the location
    folium.Marker(location=[session["lat"], session["lon"]], popup='My Location').add_to(page_map)

    # Save the map as HTML string
    map_html = page_map._repr_html_()

    return render_template("index.html", date=date_form,
                           city=city,
                           w_temp=w_temp,
                           w_humidity=w_humidity,
                           w_rain=w_rain,
                           w_wind=w_wind,
                           w_direc=direction,
                           w_cloud=w_cloud,
                           w_uv=w_uv,
                           map_html=map_html,
                           part_data=part_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/account",  methods=["GET", "POST"])
@login_required
def account():
    """User settings"""

    if request.method == "POST":

        # Make dummy var
        old_pass = request.form.get("old_password")
        new_pass = request.form.get("password")
        confirm = request.form.get("confirmation")

        # Check input with info flash
        if (not old_pass or not new_pass) and new_pass != confirm:
            flash("Check passwords")
            render_template("account.html")

        # Get user data from database
        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
        print(rows)

        if not check_password_hash(rows[0]["hash"], old_pass):
            flash("Wrong old password")
        else:
            db.execute("UPDATE users SET hash = ? WHERE id = ?",
                       generate_password_hash(new_pass), session["user_id"])
            return logout()
    else:
        return render_template("account.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/location", methods=["GET", "POST"])
@login_required
def place():
    """Get stock quote."""
    if request.method == "POST":
        city = request.form.get("symbol")
        if not city:
            flash("Enter City name")
            return render_template("location.html")
        else:
            session["city"] = city

            # Use url_for to redirect with url change
            return redirect("/")
    else:
        return render_template("location.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        # Set dummy variables
        name = request.form.get("username")
        mail = request.form.get("email")
        accounts = db.execute("SELECT username, email FROM users")

        # Check if user provide data not in database or not empty
        if not name or not mail or not request.form.get("password"):
            return apology("Must fill everything", 400)

        elif "@" not in mail or len(mail) < 5:
            return apology("Email not correct", 400)

        elif len(accounts) != 0:
            for user in accounts:
                if user.get("username") == name:
                    return apology("Username already exists", 400)
                elif user.get("email") == mail:
                    return apology("Email already exists", 400)
                elif request.form.get("password") != request.form.get("confirmation"):
                    return apology("password must match", 400)

        # Pass data to database
        db.execute("INSERT INTO users (username, email, hash) VALUES (?, ?, ?);",
                   name,
                   mail,
                   generate_password_hash(request.form.get("password")))

        flash("Registered!")
        return render_template("login.html")

    return render_template("register.html")

@app.route("/week", methods=["GET"])
def week():
    """Show week weather"""

    if request.method == "GET":
        w_data = session["week"]
        return render_template("week.html",
                               city=get_city(),
                               w_data=w_data)
