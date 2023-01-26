#Gunicorn config for "qa" application
#Config for application just sets up the variables for python environment

pythonpath = '/home/box/web/ask' #path for default Django application in server
bind = "0.0.00:8000"
workers = 4
