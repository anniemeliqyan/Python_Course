"""8. Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.
Examples
"11/12/2019" ➞ "20191211"
"12/31/2019" ➞ "20193112"
"01/15/2019" ➞ "20191501"
"""

date = "11/12/2019"
dateList = date.split("/")
date_reverse = dateList [::-1]
convertion = date_reverse[0] + date_reverse[1] + date_reverse[2]
print(convertion)