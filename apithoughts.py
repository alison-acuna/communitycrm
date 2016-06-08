# User crafts new filter
# Save function initiates formation and log of get request
# to craft member.html, get request must pull and populate

# I think this code will ulimately go in views.py in the new() method

meetup_id = member.meetuplink

r = requests.get("{}{}".format("https://api.meetup.com/members/", meetup_id))

# Question to pick up - what happens with the request?  what initiates it?


#  Working from:  https://ultimatedjango.com/blog/how-to-consume-rest-apis-with-django-python-reques/
#  Created serializer in the ap folder


# changes made to views.py - added process_api
# added memberapi.html
# added serializer.py

#We worked with an API in python with command line interface + with Jquery.  I need to know where to put the  API elements and check my thinking on the ID
#
# When rendering info from the database + and an API should these be housed in separate forms, views, etc?
#
# Should the views.py component be in new() or its own function?
