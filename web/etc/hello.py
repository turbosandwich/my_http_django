#gunicorn config_file for simple static back-end application

pythonpath = /home/box/web/
bind = "0.0.0.0:8080"
workers = 4

