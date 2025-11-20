# Django-gis Project

## Overview
This is a Django-based web application for managing farm data. It allows users to perform CRUD operations on farming models, such as Crops and Animals, and integrates GIS functionality using GDAL and SpatiaLite.
The project was completed in three assignments:

- **Assignment 1:** Django models, migrations, and admin customisation

- **Assignment 2:** Wildlife app + Django ORM queries

- **Assignment 3:** Views, templates, and CRUD functionality

- **Assignment 4:** Function-Based Views (FBVs), BaseModel for shared fields, pagination, success messages, and improved UI

## Features
- CRUD operations for Farm Locations, Crops, and Irrigation Zones
- BaseModel with last_update (auto-update timestamp) and last_update_by (tracks user who last modified a record)
- Pagination on list views (10 items per page)
-Success messages on create/update/delete actions
- User-friendly navigation and intuitive interface
- Django Admin integration with read-only tracking fields
- GIS support using GDAL

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
```
### CRUD Views (Assignment 4)

```bash
List View: Paginated lists of Farm Locations, Crops, Irrigation Zones

Detail View: View details of a single record

Create View: Add new records with last_update_by automatically set

Update View: Edit records with last_update and last_update_by auto-updating

Delete View: Remove records with success messages
```

### Example URL patterns (FBVs):
```bash
path("farms/", farm_list, name="farm_list"),
path("farms/add/", farm_create, name="farm_create"),
path("farms/<int:pk>/", farm_detail, name="farm_detail"),
path("farms/<int:pk>/edit/", farm_update, name="farm_update"),
path("farms/<int:pk>/delete/", farm_delete, name="farm_delete"),
```
### Templates
```bash
farm/templates/farm/
    farmlocation_list.html
    farmlocation_detail.html
    farmlocation_form.html
    farmlocation_confirm_delete.html
    crop_list.html
    crop_detail.html
    crop_form.html
    crop_confirm_delete.html
    zone_list.html
    zone_detail.html
    zone_form.html
    zone_confirm_delete.html
```
### Django Admin
```bash
Custom admin classes:
list_display
list_filter
search_fields
readonly_fields for last_update and last_update_by
```

### Branching Structure
```bash
The project follows the lesson-based branching:

django-lesson-1-admin

django-lesson-2-orm

django-lesson-3-cbv

django-lesson4-fbv
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
