# 🧠 Student Performance & Analytics API

## 📌 Overview
This project is a backend system for managing and analyzing student academic performance.

It was developed as a final project for the FlexiSAF Internship, demonstrating backend engineering, data analytics, and basic machine learning integration.

The system goes beyond CRUD by providing intelligent insights into student performance using Pandas and Scikit-learn.

---

## 🚀 What This Project Does

- Role-based access (Admin, Teacher, Student)  
- Record scores, attendance, courses  
- Auto-create student profiles via signals  
- Analytics using Pandas  
- Risk detection (rule-based + ML)  
- Attendance trends (student, course, global)  

---

## 📊 Core Analytics Capabilities

### 🎓 Student-Level
- Insights (average, best, weakest)  
- Risk detection  
- ML prediction  
- Attendance trend  

### 📚 Course-Level
- Course statistics  
- At-risk students  
- Best students  
- Attendance trend  

### 🏫 Global
- Attendance trends  
- Best students  
- At-risk students  

---

## 📡 API Endpoints

### 🔐 Auth
```
POST /api/auth/register/
POST /api/auth/login/
GET /api/auth/me/
```

### 📚 Records
```
GET /api/records/students/
POST /api/records/courses/
GET /api/records/courses/list/
POST /api/records/scores/
POST /api/records/attendance/
```

### 📊 Analytics
```
GET /api/analytics/students/{id}/
GET /api/analytics/courses/{course_name}/
GET /api/analytics/overview/
```

---

## ⚙️ Tech Stack
```
Django + DRF
SQLite / PostgreSQL
Pandas
Scikit-learn
Docker
JWT Auth
```

---

## ▶️ Local Setup

```
git clone <repo-url>
cd project

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Seed Data
```
python seed_data.py
```

### Run Tests
```
python manage.py test
```

---

## 🐳 Docker Setup

```
docker-compose build
docker-compose up

docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
docker-compose exec web python seed_data.py
```

---

## ✨ Highlights
- Clean architecture  
- Pandas analytics  
- ML prediction  
- Aggregated APIs  
- Dockerized  

---

## 👨‍💻 Author
Udeagha Mark Mang
