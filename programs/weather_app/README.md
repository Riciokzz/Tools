# Weather App

Weather App is a web application that allows users to check current weather in any place of the world by simply inputting city or location name.

## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Project Structure](#project-structure)
- [Design Choices](#design-choices)
- [Video Demo](#video-demo)


## Project Description

Weather App is a Python-based web application built with Flask that enables users to check the current weather and weekly forecast for any desired location. Powered by a reliable weather API, the app fetches accurate and up-to-date weather data. Users can search for a specific location and instantly receive information on temperature, humidity, wind speed, and cloud coverage. The Weather App offers a clean and intuitive interface, making it easy for users to access weather details and plan their activities accordingly. Stay informed about the weather with WeatherApp and never get caught unprepared.

## Features

- Check the current weather for any desired location.
- Get a weekly weather forecast to plan ahead.
- Display essential weather information such as Temperature, UV index, Humidity, Rain, Wind and Cloud coverage.
- User-friendly interface for easy navigation and interaction.
- Registration form.
- User personal tab for changing password.

## Project Structure

The Weather App project is structured as fallows:

- app.py - brains for program, handles all functions.
- helpers.py - additional .py program with apology and login handlers.
- project.db - main database for all users.
- README.md - readme file with all instructions about program.
- requirements.txt - used libraries and frameworks.

### flask_session
Default folder - all sessions are being saved.

### static
Default folder - pictures, images and css files are saved here.

### templates
Default folder - all html files saved here.
- account.html - user personal page for changing his private data.
- apology.html - is made for error handling, it will try to catch errors and show some meme pictures, for example if user input wrong password, etc.
- index.html - template displays the main current day weather data and also location with the map  marker.
- layout.html - bare bones for all html files, containing all necessary tags, handles head, body, footer of pages.
- location.html - page for location search, here use can change location name.
- login.html - template for user login page.
- register.html - template for user registration page.
- week.html - weather page with one week from now weather information with 2 times per day.



## Design Choices

- Flask: Flask was chosen as the web framework for its simplicity, flexibility, and ease of use. It provides a minimalistic approach to web development, allowing for quick setup and easy customization.
- OpenCageData API: The OpenCageData API was selected for obtaining location coordinates (latitude and longitude) based on user input. This API provides accurate and reliable geocoding services, allowing users to search for locations using various parameters such as city name or ZIP code.
- Open-Meteo API: The Open-Meteo API was chosen to fetch weather data based on location coordinates obtained from the OpenCageData API. This API offers a wide range of weather information, including current weather conditions and weekly forecasts. By utilizing this API, Weather App provides up-to-date and reliable weather data to users.
- User Interface: The user interface was designed to be intuitive, visually appealing, and responsive. It provides a seamless user experience, allowing users to easily search for locations and view the weather information. The interface is designed to display the key weather parameters prominently, ensuring that users can quickly access the most relevant information.
- Weekly Forecast: The inclusion of a weekly weather forecast enables users to plan their activities and make informed decisions for the upcoming days. By providing a comprehensive overview of the weather conditions throughout the week, Weather App helps users prepare for different weather scenarios.
- Registration: Registration was made for later versions and also to handle bots for checking weather and scraping data.
- Database: To quick handle of all registered accounts and they data.

## Video Demo
Link to video of project: <https://youtu.be/3U1TLS4_ufg>