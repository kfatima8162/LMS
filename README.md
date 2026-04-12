# LMS
Learning Management System using django framework.

# 🔐 Authentication & Role-Based Access System (LMS)

## 📌 Overview

This module implements a **basic authentication system** for the LMS using Django's built-in authentication framework. It supports **login functionality** and **role-based access control** for Teachers and Students.

---

## 🚀 Features Implemented

### ✅ 1. User Authentication

* Login functionality using Django's `authenticate()` and `login()`
* Session-based authentication
* CSRF protection enabled in login form

---

### ✅ 2. Role-Based Access Control

* Users are assigned roles via database models:

  * `Teacher` (OneToOne with User)
  * `Student` (OneToOne with User)

* Role is automatically detected after login:

```python
if hasattr(user, 'teacher'):
    # Teacher access
elif hasattr(user, 'student'):
    # Student access
```

---

### ✅ 3. Protected Routes

* Custom decorator `teacher_required` ensures:

  * Only authenticated users can access the dashboard
  * Only users with Teacher role are allowed

```python
@teacher_required
def teacher_dashboard(request):
```

---

### ✅ 4. Unauthorized Access Handling

* Anonymous users → redirected to login page
* Non-teacher users → access denied or redirected

---

## 📂 File Structure

```
TeacherApp/
│
├── views.py              # Login + Dashboard logic
├── decorators.py         # Role-based access decorators
├── models.py             # Teacher, Student models
├── templates/
│   └── teacher/
│       ├── login.html
│       └── dashboard.html
```

---

## ⚙️ How It Works

### 🔹 Login Flow

1. User enters username & password
2. Django authenticates user
3. Session is created
4. Role is detected
5. User is redirected accordingly

---

### 🔹 Dashboard Access Flow

1. User tries to access dashboard
2. `teacher_required` decorator checks:

   * Is user logged in?
   * Is user a Teacher?
3. If valid → access granted
4. Else → redirect / deny access

---

## ⚠️ Temporary Notes

* Student module is **not yet implemented**
* Student login currently:

  * Redirects to placeholder OR teacher dashboard (temporary)
* Dummy handling may exist for testing

---

## 🔒 Security Notes

* CSRF protection is enabled
* Passwords handled securely via Django auth
* Role cannot be manually overridden from frontend

---

## 🛠️ Future Improvements
* More is yet to come (UNDER DDEVELOPMENT)
* Add Student dashboard & routing
* Implement signup/registration system
* Add logout functionality
* Use Django Groups/Permissions for scalability
* Add middleware for global role handling

---

## 🧠 Key Design Decisions

* ❌ No role selection in login form
* ✅ Role determined from database (secure & scalable)

---

## 👨‍💻 Usage (For Developers)

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

### Access

* Login: `http://127.0.0.1:8000/login/`
* Dashboard: `http://127.0.0.1:8000/`

---

## 📌 Summary

This module establishes a **secure foundation** for the LMS by:

* Authenticating users
* Enforcing role-based access
* Protecting sensitive routes

It is designed to be **scalable and extendable** for future modules.

