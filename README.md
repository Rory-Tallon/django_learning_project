# What is this project?

This project aims to create a Django powered front end where users can enter a coin of their choice and receive the latest price of that coin. 

## What's currently done?

1. The class to query the API has already been created
2. Have a very basic front end
3. Hookup the API requests to the frontend
4. Add a form to the index page
5. Get the form to go to the selection view which calls the api with what they put in the form and then redirect to the details page which shows them the price
6. add error handling for the coin test so it shows an error and lets them re-enter a coin
7. make the way it displays the coin nicer
8. make it look nicer
9. add a background
10. Let the user pick a date so that they can see what the price was then.
11. Add a graph to the site so that the user can see how the price has changed over the last month
    - need to instal matplotlib
    - then get a function to generate the graphs 
    - then send that to the html 
12. Convert unix timestamp to normal times

## What needs doing?

1. add some tests
2. Add error messages for invalid dates
3. Make the graph look better - labels, units, no overlapping text

## Automated tests

1. Verify that a correct coin gives a result
2. Verify that an invalid coin behaves correctly
3. Test that the date is valid 


## Old API Calls

Get the price at a specific date - 
- request_str = "https://api.coingecko.com/api/v3/coins/"+coin+"/history?date="+date

Get the price currently - 
- request_str = "https://api.coingecko.com/api/v3/simple/price?ids="+coin+"&vs_currencies=usd"