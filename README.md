# Django Item Management Application

This is a Django application for managing items with CRUD (Create, Read, Update, Delete) operations. The application also includes a search functionality to find items by name with a case-insensitive exact match.

## Features

- Add new items
- View a list of all items
- Edit existing items
- Delete items
- Search for items by name (case-insensitive)

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation

1. Clone the repository:

```bash
git clone https://github.com/1666sApple/django-project-1.git
cd django-project-1
```
### Create and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
### Install the required packages:

```
pip install -r requirements.txt

### Apply the migrations:
```
python manage.py migrate

### Create a superuser to access the Django admin:

```
python manage.py createsuperuser
```
### Start the development server:
```
python manage.py runserver
```
Open your web browser and navigate to http://127.0.0.1:8000 to access the application.
### Usage
#### Home Page
The home page provides links to the following functionalities:
```
1. View all items
2. Create a new item
3. Edit an existing item
4. Delete an item
5. Search for items
```
### Creating an Item

To create a new item, navigate to http://127.0.0.1:8000/item/create/ and fill out the form. Click the "Save" button to create the item.

### Viewing Items
To view all items, navigate to http://127.0.0.1:8000/item/. You will see a list of all items in the database.

### Editing an Item
To edit an item, navigate to http://127.0.0.1:8000/item/edit/<item_id>/ (replace <item_id> with the actual ID of the item you want to edit). Make the desired changes and click the "Save" button.

### Deleting an Item
To delete an item, navigate to http://127.0.0.1:8000/item/delete/<item_id>/ (replace <item_id> with the actual ID of the item you want to delete). Confirm the deletion.

### Searching for Items
To search for items, use the search form in the navigation bar. Enter the name of the item you are looking for and click the "Search" button. The search results will be displayed on the search results page.

### Project Structure
```
django-project-1/
│
├── app101/
│   ├── migrations/
│   ├── static/
│   │   └── app101/
│   │       └── style.css
│   ├── templates/
│   │   └── app101/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── item.html
│   │       ├── create_item.html
│   │       ├── detail.html
│   │       ├── delete_item.html
│   │       └── search_results.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── firstsite/
│   ├── templates/
│   │   └── app101/
│   │       ├── base.html
│   │       ├── home.html
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── users/
│   ├── migrations/
│   ├── templates/
│   │   └── app101/
│   │       ├── login.html
│   │       ├── logout.html
│   │       ├── register.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── README.md
```
### Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

### License
This project is licensed under the MIT License. See the LICENSE file for more information.
