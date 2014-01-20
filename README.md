# Demo app

demo app, AngularJS + Django + Django Rest Framework + Class Based Views.

### Running backend
``` bash
git clone git@github.com:chris-ramon/django_angularjs_demo_cbv.git

cd backend/
virtualenv demo_app_venv
source demo_app_venv/bin/activate
pip install -r requirements.txt
./manage.py runserver
```

### Running frontend
``` bash
cd frontend/
npm install
bower install
grunt serve
```

Go to http://127.0.0.1:9000/