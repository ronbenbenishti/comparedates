# Compare dates
A simple script designed to find out which ages the Jewish date and the Gregorian date apply on the same day.
Two parameters are required to run the code:
* Gregorian date of birth (dd/mm/yyyy)
* Were you born after sunset? (y / n)

The code goes through all the years (up to 100) and compares the Jewish date of that day to the Gregorian date.
If a match is found, the age and year of the birthday will be displayed.
The Jewish date is based on the data at shoresh.org.il

## Prerequisites: ##
* python 2.7
* requests module
* hebrew encoding (utf-8)
  
## Installing ##
```sh
git clone https://github.com/ronbenbenishti/comparedates.git
```

## Screenshot
![Image](https://raw.githubusercontent.com/ronbenbenishti/comparedates/master/ss.png)
