# Setup and Installation

Prerequisites
        Python 3.8+
        Django 4.x
        Virtual environment

1.Clone the repository:
    https://github.com/Suhas822/blog_website_exercise.git
    
    cd blog_website_exercise

2.Create a virtual environment:
    python -m venv env
    on LinuX :source env/bin/activate  
    On Windows: env\Scripts\activate

3.Install dependencies:
    pip install -r requirements.txt

4.Set up the database:
    python manage.py migrate
    

5.Run the server:
    python manage.py runserver

##  Endpoints

      http://127.0.0.1:8000/

## Management command to upload the csv file data :

        python manage.py import_blog_posts data/blog_posts.csv