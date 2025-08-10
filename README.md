# 📚 Campus Connect – College Portal

Campus Connect is a **Django-based college portal** designed to simplify campus management.  
It provides separate roles for **Students**, **Teachers**, and **Administrators**, enabling smooth handling of academic and campus-related activities.

---

## 🚀 Features

- 👩‍🎓 **Student Management** – Add, update, and view student profiles.
- 👨‍🏫 **Teacher Management** – Manage faculty details.
- 🏢 **Department & Subject Management** – Assign subjects to specific departments.
- 🔒 **Secure Authentication** – User login and role-based access.
- 📊 **Admin Dashboard** – Manage all data from one place.
- 📅 **Attendance Tracking** – Mark and monitor student attendance.
- 📝 **Assignment Management** – Upload, assign, and review student assignments.
- 🗓 **Schedule Management** – View and update class timetables.
- 🔔 **Notifications** – Send important announcements to students and staff.
- 🎨 **Clean UI** – Simple and easy-to-use interface.

---

## 🛠 Tech Stack

- **Backend:** Django, Python  
- **Frontend:** HTML, CSS  
- **Database:** SQLite (can be switched to PostgreSQL/MySQL)  
- **Tools:** Git, GitHub, Virtual Environment  

---

## 📥 Installation Guide

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/sivalingamperla123/campus_connect.git
cd campus_connect

Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate (for Windows)
source venv/bin/activate (for macOS/Linux)

Install Django
pip install Django
pip install -r requirments.txt

Run Migrations
python manage.py makemigrations
python manage.py migrate

Start the Server
python manage.py runserver

Access the App
Visit http://127.0.0.1:8000/ in your browser
