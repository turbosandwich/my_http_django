sudo pip3 install virtualenv
sudo pip3 install pathlib2
virtual env -p python3 venv
source venv/bin/activate
pip3 install django

sudo /etc/init.d/nginx restart

gunicorn -w 2 -c /home/max/git_server/web/etc/hello.py hello:app & gunicorn -w 2 -c /home/box/web/etc/qa.py ask.wsgi:application & curl -vv 'http://127.0.0.1:8000/login/'
