To complete your Django “Mini Booking System” project and push it to GitHub while setting up PostgreSQL in Docker and running the Django website on your local system, follow these step-by-step instructions:

### Step 1: Prepare the Django Project Locally

1. **Create a New Django Project**  
   If you haven't created the project yet, you can do so with the following command:

   ```bash
   django-admin startproject mini_booking_system
   cd mini_booking_system
   ```

2. **Create a Django App for the Booking System**

   ```bash
   python manage.py startapp booking
   ```

3. **Install Required Packages**  
   Install the required dependencies, including PostgreSQL (`psycopg2`) and Docker-related tools.

   ```bash
   pip install django psycopg2-binary
   ```

4. **Configure PostgreSQL Database in Django**  
   Edit your `settings.py` to connect Django to PostgreSQL:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'booking_db',
           'USER': 'postgres',
           'PASSWORD': 'yourpassword',
           'HOST': 'db',  # name of the container
           'PORT': '5432',
       }
   }
   ```

   Make sure to replace `yourpassword` with a secure password for PostgreSQL.

### Step 2: Set Up Docker Environment

1. **Create `Dockerfile` for the Django Application**

   Inside your project directory, create a file named `Dockerfile` with the following content:

   ```dockerfile
   # Use the official Python image from the Docker Hub
   FROM python:3.11-slim

   # Set the working directory inside the container
   WORKDIR /app

   # Install system dependencies
   RUN apt-get update \
       && apt-get install -y \
       libpq-dev \
       && rm -rf /var/lib/apt/lists/*

   # Copy the requirements file into the container
   COPY requirements.txt /app/

   # Install Python dependencies
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy the Django project code into the container
   COPY . /app/

   # Set the environment variable to tell Django not to use the cached queries
   ENV PYTHONUNBUFFERED 1

   # Run migrations and start the Django app
   CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
   ```

2. **Create `docker-compose.yml`**

   Create a `docker-compose.yml` file in the root directory of your project:

   ```yaml
   version: '3.9'

   services:
     web:
       build: .
       command: python manage.py runserver 0.0.0.0:8000
       volumes:
         - .:/app
       ports:
         - "8000:8000"
       depends_on:
         - db

     db:
       image: postgres:13
       environment:
         POSTGRES_DB: booking_db
         POSTGRES_USER: postgres
         POSTGRES_PASSWORD: yourpassword
       volumes:
         - postgres_data:/var/lib/postgresql/data
       ports:
         - "5432:5432"

   volumes:
     postgres_data:
   ```

   Replace `yourpassword` with the actual password you'd like to set for your PostgreSQL container.

3. **Create `.env` File for Environment Variables (Optional)**

   It's good practice to manage sensitive data like passwords via environment variables. Create a `.env` file with the following:

   ```env
   POSTGRES_DB=booking_db
   POSTGRES_USER=postgres
   POSTGRES_PASSWORD=yourpassword
   ```

   And make sure to update `docker-compose.yml` to use this `.env` file by adding the following lines under `db` service:

   ```yaml
   env_file:
     - .env
   ```

4. **Create `requirements.txt`**

   Create a `requirements.txt` file with the following content:

   ```txt
   django
   psycopg2-binary
   ```

### Step 3: Initialize Git and Push to GitHub

1. **Initialize Git Repository**

   In your project directory, initialize the Git repository:

   ```bash
   git init
   ```

2. **Create `.gitignore`**

   Create a `.gitignore` file to avoid pushing unnecessary files to GitHub. Add the following:

   ```gitignore
   __pycache__/
   *.pyc
   *.pyo
   *.pyd
   .env
   .venv/
   myenv/
   *.db
   *.sqlite3
   node_modules/
   ```

3. **Add Files to Git**

   Add all the project files to the Git repository:

   ```bash
   git add .
   ```

4. **Commit Changes**

   Commit the changes with a message:

   ```bash
   git commit -m "Initial commit with Docker setup and basic Django app"
   ```

5. **Create a GitHub Repository**

   Go to GitHub and create a new repository. Copy the repository URL.

6. **Push to GitHub**

   Link your local repository to GitHub and push the changes:

   ```bash
   git remote add origin https://github.com/your-username/mini-booking-system.git
   git branch -M main
   git push -u origin main
   ```

### Step 4: Run the Application with Docker

1. **Start Containers Using Docker Compose**

   To build and start your Django and PostgreSQL containers, run the following command:

   ```bash
   docker-compose up --build
   ```

2. **Access the Django Application**

   Once the containers are up and running, you can access the Django website at:

   ```
   http://localhost:8000/
   ```

3. **Migrate Database**

   Run the Django migrations to set up your database schema:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. **Create a Superuser**

   If you want to create an admin user to access the Django admin panel, run:

   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

### Step 5: Write the README.md

Create a `README.md` file with the following content:

```markdown
# Mini Booking System

This is a Django-based mini booking system where users can book available slots for facilities.

## Features
- User Registration & Authentication
- Facility Model with name, location, and capacity
- Booking Model with user, facility, date, and status
- Forms for booking creation
- Class-Based Views (CBVs) for booking management
- Django admin panel customization (optional)
- Unit tests for critical functionality
- Dockerized application with PostgreSQL

## Requirements
- Docker
- Docker Compose

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/mini-booking-system.git
   cd mini-booking-system
   ```

2. Build and start the containers:
   ```bash
   docker-compose up --build
   ```

3. Run migrations:
   ```bash
   docker-compose exec web python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

5. Access the app at:
   ```
   http://localhost:8000/
   ```

6. Access the Django admin panel at:
   ```
   http://localhost:8000/admin
   ```

## Notes
- The application uses PostgreSQL as the database.
- The `docker-compose.yml` file sets up both Django and PostgreSQL containers.
- For development, the app runs with Docker and can be accessed locally on your machine.

```

### Step 6: Test and Verify

- Test your app by navigating to `http://localhost:8000/`.
- Log in to the admin panel at `http://localhost:8000/admin` using the superuser credentials.

---

This should set you up with a Django app running in Docker, connected to PostgreSQL, and properly version-controlled with Git and GitHub. Let me know if you run into any issues!
