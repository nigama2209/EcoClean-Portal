🧺 EcoClean Portal

The EcoClean Portal is a Django-based web application that allows customers to easily book laundry services online.
It provides a simple and user-friendly interface for customers, managers, and administrators to manage laundry service bookings.

🚀 Features

📝 Customer Booking – Book laundry services online

📅 Order Management – Track and manage bookings

👤 User Authentication – Signup, Login, Password Reset

📊 Admin Panel – Manage services, users, and feedback

⚙️ Tech Stack

Frontend: HTML, CSS, Bootstrap

Backend: Django, Python

Database: SQLite (default, can be changed to PostgreSQL/MySQL)

Version Control: Git & GitHub

🛠️ Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/ecoclean.git
cd ecoclean


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux


Install dependencies:

pip install -r requirements.txt


Run database migrations:

python manage.py migrate


Start the development server:

python manage.py runserver


Open the app in your browser:

http://127.0.0.1:8000/
