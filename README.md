# Django-Personal-Portfolio-Project

1) Enter https://www.pythonanywhere.com/ website and create account, enter dashboard page and go to bash console
3) Clone repository: git clone your_repository
4) Create virtual environment: mkvirtualenv --python=/usr/bin/python3.12 portfoliovenv
5) Close bash console: exit
6) Want to enter virtual environment again: workon portfoliovenv
7) Get out of specific virtual environment: deactivate
8) Check all virtual environments: cd .virtualenvs/
9) Install django and pillow: pip install django pillow
10) Enter https://www.pythonanywhere.com/ website, enter web page and add new web app
11) Use manual configuration and choose python version
12) Enter a path to your web app source code: /home/erturkmemmedli/Django-Personal-Portfolio-Project
13) Change working directory as above as well
14) Enter a path for virtualenv: portfoliovenv
15) Enter wsgi config file and delete everything except django section and uncomment the code
16) Change path to '/home/erturkmemmedli/Django-Personal-Portfolio-Project'
17) Change mysite to 'personal_portfolio'
18) Go to personal_portfolio/settings.py and add 'erturkmemmedli.pythonanywhere.com' to ALLOWED_HOSTS
19) Reload the website after all changes
20) Go to personal_portfolio/settings.py and change DEBUG to False
21) Go to personal_portfolio/settings.py and add STATIC_ROOT = os.path.join(BASE_DIR, "static")
22) Go to bash console to be able to use static files: python manage.py collectstatic
23) Enter url and path for static files: for URL - /static/, for directory - /home/erturkmemmedli/Django-Personal-Portfolio-Project/static
24) Enter url and path for media as well: for URL - /media/, for directory - /home/erturkmemmedli/Django-Personal-Portfolio-Project/media
25) Enable 'Force HTTPS'
26) Databases can be adjusted in https://www.pythonanywhere.com/ website, MySQL is free, PostgreSQL requires upgrade
27) Create local_settings.py file for local work purpose and add it to .gitignore
28) Create requirements file: pip freeze > requirements.txt
29) Install them in production: pip install -r requirements.txt
30) Change your domain name tp your custom domain (Google Domain), add DNS as CNAME