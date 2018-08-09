# CSCI S-33a - Final Project
# Ethan Bates

App Name: Did you Get Avocados
Main Components: Django, Postgres, Bootrap, JQuery/JqueryUI, AJAX

Data Citation:
US Department of Agriculture, Agricultural Research Service, Nutrient Data Laboratory.
USDA National Nutrient Database for Standard Reference, Legacy. Version Current:  April 2018

0) Landing Page with the application name and Logo
1) User Registration and Login controls - built in Django and some custom error handling
3) Home Page
--- users can see and view previous lists that they made
--- utlizes jquery and ajax to make call to DB and refresh list modal on show

4) New List
--- category drop down assists with search of large DB - additional filter
--- search bar uses JQueryUI for autocomplete and Jquery to Append items to a list
--- Form submitted creates a new user list with items