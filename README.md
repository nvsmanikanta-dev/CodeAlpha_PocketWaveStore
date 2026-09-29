# 🛍️ PocketWaveStore

### Full-Stack E-Commerce Web Application

**PocketWaveStore** is a full-stack e-commerce web application developed as **Task 1 – Simple E-commerce Store** for the **CodeAlpha Full Stack Development Internship**.

The application provides a complete shopping workflow including product browsing, product details, cart management, user authentication, and order processing through a clean and responsive interface.

---

## 🎥 Project Demo

A complete project walkthrough is available below.

### ▶ Watch Demo

[**View PocketWaveStore Demo Video**](demo/PocketWaveStore_Demo.mp4)

> The demo showcases the user interface, product browsing, authentication, cart flow, order process, and project implementation.

---

## 📌 Project Overview

PocketWaveStore demonstrates the core workflow of a modern e-commerce platform.

Users can create an account, browse available products, view product information, add products to their cart, and proceed through the order workflow.

The project combines frontend development, backend processing, authentication, and database management into a complete full-stack application.

---

## ✨ Key Features

### 👤 User Authentication
- User registration
- User login
- User logout
- Secure authenticated sessions

### 🛒 Product Shopping
- Browse available products
- View individual product details
- Product information and pricing
- Add products to shopping cart

### 🧺 Shopping Cart
- Add products to cart
- View selected products
- Update cart contents
- Remove products from cart
- View order total

### 📦 Order Management
- Create orders
- Process selected cart items
- Maintain order information
- Store order-related data in the database

### 🗄️ Database Integration
The application manages data for:

- Users
- Products
- Shopping cart
- Orders

### 💻 Responsive Interface
- Clean navigation
- Structured product presentation
- User-friendly shopping workflow
- Responsive web interface

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Django

### Database

- Django ORM
- SQLite

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 🏗️ Application Workflow

```text
User
 │
 ├── Register / Login
 │
 ▼
Product Catalogue
 │
 ├── Browse Products
 ├── View Product Details
 │
 ▼
Shopping Cart
 │
 ├── Add Items
 ├── Update Items
 ├── Remove Items
 │
 ▼
Order Processing
 │
 ▼
Database
```

---

## 📂 Project Structure

```text
CodeAlpha_PocketWaveStore/
│
├── manage.py
├── requirements.txt
├── README.md
│
├── pocketwavestore/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── store/
│   ├── migrations/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── templates/
│   └── ...
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
└── demo/
    └── PocketWaveStore_Demo.mp4
```

> The exact internal folder structure may vary depending on the final project version.

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/nvsmanikanta-dev/CodeAlpha_PocketWaveStore.git
```

### 2. Open the Project Folder

```bash
cd CodeAlpha_PocketWaveStore
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Database Migrations

```bash
python manage.py migrate
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Open the Application

```text
http://127.0.0.1:8000/
```

---

## 🔐 Admin Access

To create a Django admin account:

```bash
python manage.py createsuperuser
```

Then open:

```text
http://127.0.0.1:8000/admin/
```

The admin interface can be used to manage application data such as users, products, and orders.

---

## 📋 CodeAlpha Task 1 Requirements

This project was developed for:

### ✅ Task 1 – Simple E-commerce Store

The task required the implementation of:

- Product listings
- Shopping cart
- Product details page
- Order processing
- User registration and login
- Database integration for products, users, and orders

PocketWaveStore was developed around these core requirements as part of the **CodeAlpha Full Stack Development Internship**.

---

## 🎯 Learning Outcomes

This project provided hands-on experience with:

- Full-stack web application development
- Django backend development
- User authentication
- Database models and relationships
- Django ORM
- CRUD operations
- Shopping cart workflows
- Order processing
- Frontend and backend integration
- Git and GitHub version control

---

## 🔗 Project Links

### GitHub Repository

[**CodeAlpha_PocketWaveStore**](https://github.com/nvsmanikanta-dev/CodeAlpha_PocketWaveStore)

### LinkedIn

[**Nunna Venkata Sai Manikanta**](https://www.linkedin.com/in/nunna-venkata-sai-manikanta-6a5506356/)

---

## 👨‍💻 Author

### Nunna Venkata Sai Manikanta

**Full Stack Development Intern**

GitHub:  
[github.com/nvsmanikanta-dev](https://github.com/nvsmanikanta-dev)

LinkedIn:  
[linkedin.com/in/nunna-venkata-sai-manikanta-6a5506356](https://www.linkedin.com/in/nunna-venkata-sai-manikanta-6a5506356/)

---

## 🏢 Internship

This project was completed as part of the **CodeAlpha Full Stack Development Internship**.

The internship focuses on gaining practical experience in frontend development, backend development, authentication, database integration, and building complete web applications.

---

## 📄 License

This project is created for educational and internship purposes.

---

## ⭐ Support

If you found this project useful, consider giving the repository a **star ⭐**.

---

<p align="center">
  <b>PocketWaveStore</b><br>
  Full-Stack E-Commerce Application<br>
  CodeAlpha Task 1
</p>
