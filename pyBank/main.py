# Unit 3 | Assignment - Py Me Up, Charlie

# main.py for pyBank

'''
* In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. 
  You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is 
  composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for 
  accounting so the records are simple.)

* Your task is to create a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset

  * The total net amount of "Profit/Losses" over the entire period

  * The average change in "Profit/Losses" between months over the entire period

  * The greatest increase in profits (date and amount) over the entire period

  * The greatest decrease in losses (date and amount) over the entire period

* As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```
* In addition, your final script should both print the analysis to the terminal and 
  export a text file with the results.

    Found @ https://mkaz.blog/code/python-string-format-cookbook/
  

# fininsh converting to CSV (delimiter '|') then read and format the entries!

Number|Format|Output|Description
3.1415926|{:.2f}|3.14|2 decimal places
3.1415926|{:+.2f}	+3.14|2 decimal places with sign
-1|{:+.2f}	-1.00|2 decimal places with sign
2.71828|{:.0f}	3	      No decimal places
5|{:0>2d} 05	    Pad number with zeros (left padding, width 2)
5|{:x<4d}	5xxx	      Pad number with x’s (right padding, width 4)
10|{:x<4d}	10xx	      Pad number with x’s (right padding, width 4)
1000000	  {:,}	  1,000,000	  Number format with comma separator
0.25	{:.2%}	25.00%	Format percentage
1000000000	{:.2e}	1.00e+09	Exponent notation
13	{:10d}	        13	Right aligned (default, width 10)
13	{:<10d}	13	Left aligned (width 10)
13	{:^10d}	    13	Center aligned (width 10)

For even more power in formatting, you can use {} as a variable inside of the formatting 
brackets (Thanks to Peter Beens for this tip). Example:

pi = 3.1415926
precision = 4
print( "{:.{}f}".format( pi, precision ) )
~~ 3.1415

'''
