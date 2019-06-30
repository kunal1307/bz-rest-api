# bz-rest-api
Rest API for deletion of brand as per campaign 
Create a virtual environment and activate it

Change to the project root and run the below command to install the dependencies 
>pip install -r requirements.txt

Run below command to migrate 
>python manage.py migrate

Run below command to create a admin
>python manage.py createsuperuser
>username: <your new username>
>email:
>password: <your new password>

Go to the link http://localhost:8000/admin/
Create some brands and campaign using the admin interface
Associate the campaign with one of the brand and try deleting it with the below API endpoint

DELETE http://localhost:8000/api/brands/<brand-id>/delete
