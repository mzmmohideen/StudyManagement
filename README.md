## Study Management Web Application

This project is a small web application designed to manage clinical study records, fulfilling all **CRUD (Create, Read, Update, Delete)** operations. It is built using the Django Model-View-Template (MVT) architecture with a decoupled frontend consuming a REST API, demonstrating essential full-stack development skills.

---

### Technologies Used

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Backend Framework** | **Django** (Python) | Core MVT framework and server logic. |
| **API Layer** | **Django Rest Framework (DRF)** | Provides clean RESTful API endpoints for CRUD. |
| **Database** | **SQLite** | Simple, file-based database for development. |
| **Frontend** | **HTML5, CSS3, Bootstrap 5** | Structure, responsive styling, and presentation. |
| **Interactivity** | **JavaScript (Fetch API)** | Client-side logic to communicate with the DRF API. |

---

### Getting Started

Follow these steps to set up and run the project locally.

#### 1. Clone the Repository

```bash
git clone [YOUR_REPO_URL]
cd StudyManagement
```

#### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies

Install all dependencies using the requirements file:


```bash
pip install -r requirements.txt
```

#### 4. Setup the Database

Apply migrations to create the database schema:

```bash
python manage.py makemigrations studies
python manage.py migrate
```

#### 5. Run the Server
Start the Django development server:

```bash
python manage.py runserver
```