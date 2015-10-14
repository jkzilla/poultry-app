#Poultry Watch

*Poultry Watch Consumer Guide for Walmart* is a web app designed for Walmart customers to easily communicate their preferences on poultry meat items sold at their local store.

##Overview

How does a giant like Walmart listen to your opinions on how your chicken is raised? How do they satisfy all of their customers when we are unique snowflakes, and we all have our own preferences? How do they adjust in order to communicate their values to their unique consumer? Enter Poultry Watch.

##Search for your item

Poultry Watch allows a user to login and logout, and records all user activity within the app once a user logs in. The user types the item they would like to learn more about, such as 'canned chicken'. Poultry Watch calls the Walmart Search API, and then filters out any item that does not fall in the category of 'Food'. The user then chooses the item that they are interested in, which calls up the brand detail webpage. Based on whether or not the brand falls in the category of having 'organic' food items, the *Poultry Farming* Wikipedia webpage is scraped to show the appropriate information on the brand. Users can then choose to communicate with the brand through several avenues, such as Facebook, Twitter, and Instagram, which helps the brand establish a personal connection with their consumer. The consumer is led through a short, three question survey based on a Likert scale, set up for the data to be analysized properly based on psychological preference studies. The questions in the database are presented to the user based on a random choice of questions that have not been answered by the user, until all questions have been answered. The search activity and user preferences are then displayed on the user dashboard.

##Recommendation Engine [currently building 10/9/15]

Poultry Watch creates a community where real conversation about our meat products come from, and where you can get recommendations about chicken products based on:

-Non-personalized summary statistics (average product rating/review)

-Ephemeral personalization (users that shop for one item also commonly buy another item)

-Persistent personalization based on preferences (the user homepage and recommended items)

##Getting started

- [ ] Clone this repo
- [ ] Install requirements.txt
- [ ] Run server.py and access the web app at localhost:5000/
- [ ] Register
- [ ] Have fun exploring your preferences and the poultry items that Walmart has to offer!