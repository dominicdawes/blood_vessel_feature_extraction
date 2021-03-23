# TimeDate Server Assignment README

## About
the TimeDate Server is an exercise in both the use of the `timedate` and `flask` packages. The server has the following endpoints:

* `GET URL/time`
  + returns the current time as a string (see below for info on using dates
    and times with Python)
* `GET URL/date`
  + returns the current date as a string
* `POST URL/age`
  + receives a JSON in the following format:  
  `{'date': "10/10/1999", 'units': "years"}`
  + returns the length of time between the given date and the current time
  + The default return units should be years and should be returned as a
    `float`
    Optional:  If you want to learn more
  about times, allow for different units to be entered and return the results
  in the given units
 * `GET URL/until_next_meal/<meal>`
   + where `<meal>` could be `breakfast`, `lunch`, or `dinner`
   + Returns the number of hours until that meal as a `float`


## Use
* The server is initialized through a GitBash  window >>`python server.py`
* The server is initialized through a 2nd GitBash  window >>`python client.py`
* The user can view the local web service in their web browser using: " http://127.0.0.1:5000 "


## Dependencies
- flask
- numpy
- requests
