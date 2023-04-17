# user-auth-API

Clone the repo to your system.  
install django-rest-framework {pip install djangorestframework}.  
3 URLs to check upon-  
1. http://127.0.0.1:8000/myapp/user/, to get the list of users in database.  
2. http://127.0.0.1:8000/login/, login/signup page. you need to provide two parameters, {username, password} and a specific token will be generated and assigned.  
3. http://127.0.0.1:8000/myapp/getdetails/, to check authentication. If correct token is provided which is already present in database, API will authenticate you and will display your username.

