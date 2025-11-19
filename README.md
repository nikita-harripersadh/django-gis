# Django Project

## Overview
This is a Django-based web application for managing farm data. It allows users to perform CRUD operations on farming models, such as Crops and Animals, and integrates GIS functionality using GDAL and SpatiaLite.
T
he project was completed in three assignments:

Assignment 1: Django models, migrations, and admin customisation

Assignment 2: Wildlife app + Django ORM queries

Assignment 3: Views, templates, and CRUD functionality

## Features
- **Create**: Add new records for Crops and Animals.
- **Read**: View a list of records and detailed views for individual entries.
- **Update**: Edit existing records.
- **Delete**: Remove records.
- GIS support for spatial data.
- Django views and templates with clean user interface.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/nikita-harripersadh/django-gis.git
cd django-gis
```
### 2. Create and Activate Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate           # Windows
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
### 4. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 5. Create a Superuser
```bash
python manage.py createsuperuser
```
### 6. Run the Development Server
```bash
python manage.py runserver
```
### Running ORM Assignment Tasks (Assignment 2)
```bash
Use the custom Django command:

python manage.py run_orm
```
```bash
All 12 ORM tasks are implemented in:

wildlife/management/commands/run_orm.py
```
### CRUD Views (Assignment 3)
```bash
Two models from the farming app have full CRUD operations using Class-Based Views:

Views Used

ListView

DetailView

CreateView

UpdateView

DeleteView
```
### Template Structure
``` bash 
templates/
    farming/
        model_list.html
        model_detail.html
        model_form.html
        model_confirm_delete.html
```

### URL Example
```bash
path("farms/", FarmListView.as_view(), name="farm-list"),
path("farms/<int:pk>/", FarmDetailView.as_view(), name="farm-detail"),
```

### Django Admin Screens
```bash
Custom admin classes include:

list_display = (...)

list_filter = (...)

search_fields = (...)

raw_id_fields = (...)

This makes the admin interface user-friendly and searchable.
```
### Branching Structure
```bash
The project follows the lesson-based branching:

django-lesson-1-admin

django-lesson-2-orm

django-lesson-3-cbv
```
