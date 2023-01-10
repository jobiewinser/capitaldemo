# capitaldemo

These instructions have only been tested on debian 10 environments (both my server and a WSL debian virtual machine):

I have hosted this demo if you'd like to skip the install: http://capitaldemo.winser.uk/ (this is a very basic deployment running in an isolated container, I would never run a real system like this...) 

1. git clone git@github.com:jobiewinser/capitaldemo.git
2. cd capitaldemo/capitaldemoproject
3. sudo apt-get install python3-venv
4. python3 -m venv venv
5. source venv/bin/activate
5. pip install -r requirements.txt
6. python manage.py runserver 0.0.0.0:8000
7. Open broswer and go to http://127.0.0.1:8000/


This took about an hour then the deployment onto a container took about 10 minutes. I considered adding a score counter, but instead kept just to the spec