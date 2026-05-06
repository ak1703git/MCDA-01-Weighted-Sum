# MCDA 01 - Multiple Criteria Decision Analysis - Weighted Sum Model Dashboard

This is a Streamlit based decision making tool designed to aid with making a decision when there are
multiple criteria to consider.

## Quick note on running the file

type **"streamlit run mcda.py"** in the terminal to run the app and it should open up on the browser.

**Senario Example**

Lets say you need to buy a car and you have different models of cars and various conditions to consider such as 
fuel efficiency, safety, seating capacity and price.

Now you want to choose the best option after considering all the conditions. This tool helps in making
the decision using a weighted sum model.


## What is the weighted sum model?

The **Weighted Sum Model (WSM)** is the simplest multi-criteria decision-making method for evaluating a 
number of alternatives in terms of a number of decision criteria.


## Features
Initial run of the dashboard will only have two entry fields on the left with some help text in the center of the dashoard
once you enter the data into the entry field, it will then create a data frame where you can see your criteria and your options that you have entered. You can aditionally also start ranking them. **Once you are done ranking your options. It will display the winning choice.**



## Tech Stack
1. Language: Python
2. UI/Front End: Streamlit
3. Data Handeling: Pandas
