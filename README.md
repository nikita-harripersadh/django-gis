# Django Project

## Overview
This is a Django-based web application for managing farm data. It allows users to perform CRUD operations on farming models, such as Crops and Animals, and integrates GIS functionality using GDAL and SpatiaLite.
The project was completed in three assignments:

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
## 📘 Setting Up GDAL on Windows (Using VS Code + Conda)

GDAL does not install cleanly on Windows with the latest Python versions (e.g., Python 3.12+).
To avoid installation errors, this project uses a dedicated Conda environment with a compatible Python version.

Follow the steps below to set up GDAL and run this Django GIS project successfully.

### 1. Install required tools:
```bash
Download Miniconda (Restart after install)
```
### 2. Create a Conda Environment With a Supported Python Version
GDAL works best with Python 3.10 or 3.11 on Windows.

Open Anaconda Prompt or VS Code terminal
```bash
conda create -n gdal-env python=3.10
```
### 3. Activate the Environment in VS Code
```bash
conda activate gdal-env
```
You should see:
```bash
(gdal-env) C:\Users\yourname>
```
### 4. Install GDAL Using Conda-Forge (Most Important Step)
```bash
conda install -c conda-forge gdal
```
### 5. Install Django and Project Dependencies

Inside the gdal-env environment:
```bash
pip install django
```
### 6. Test GDAL Installation
Inside VS Code terminal:
```bash
python -c "import osgeo; print(osgeo.__version__)"
```
You should see a version number like:
```bash
3.6.2
```
### 7. Run the Django Project (inside VS Code)

Navigate to your project folder:
```bash
cd path/to/your/project
```
Run migrations:
```bash
python manage.py migrate
```
Start the Django development server:
```bash
python manage.py runserver
```
