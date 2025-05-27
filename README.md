# 🚀 Blinkit Automation Script

## 📌 About

Hey everyone! 👋  
I’m currently learning web automation using Selenium for the first time, and this is one of my very first hands-on mini projects. This simple automation script interacts with the Blinkit website to simulate a basic user flow — from selecting a delivery location to searching for a product and adding it to the cart.

This project was built to explore how Selenium works with dynamic web elements and how to handle real-time interactions like dropdowns, buttons, and form inputs.

---

## 🎯 What the Script Does

Here’s a step-by-step breakdown of what this script automates:

1. Launches the Blinkit website  
2. Enters a delivery location – Searches for **“Jaypee Institute”** and selects the first suggestion  
3. Searches for a product – Enters **“aata”** into the search bar and hits enter  
4. Adds the first item from the search results to the cart  
5. Clicks the **“Add to Cart”** button (if available) for that item  

---

## 🛠️ Tech Stack

- Python 3  
- Selenium WebDriver  
- Google Chrome (used with default profile)  
- Chromedriver (Make sure it’s compatible with your browser version)  

---

## 📝 Prerequisites

- Python installed on your system  
- Install dependencies:  
  ```bash
  pip install selenium

## 💡 Learning Goals

This project helped me understand:
 -	How to locate elements using class names, XPaths, and CSS selectors
 -	How to handle dynamic suggestions and clicks
 -	How to work with delays, waits, and form inputs in Selenium




While starting appium server enter : 
appium --allow-insecure=deepLink

Install this in PYTHON
pip install Appium-Python-Client selenium
