# How to Run This Django Project

Follow these steps to set up and run the Django project:

## Prerequisites

- Python installed (version 3.x recommended)
- `pip` package manager
- Virtual environment tool (optional but recommended)
- Django installed

## Steps to Run

1. **Clone the Repository**  
   Clone the project repository to your local machine:

```bash
git clone <repository-url>
cd ICONIST
```

2. **Set Up a Virtual Environment** (optional)  
   Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate or .\Scripts\activate
```

3. **Install Dependencies**  
   Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. **Apply Migrations**  
   Run database migrations:

```bash
python manage.py migrate
```

5. **Run the Development Server**  
   Start the Django development server:

```bash
python manage.py runserver
```

```bash
python manage.py tailwind start
```

6. **Access the Application**  
   Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

## Additional Notes

- Ensure you have configured the `.env` file or settings for database and environment variables if required.
- Use `python manage.py createsuperuser` to create an admin user for the Django admin panel.
