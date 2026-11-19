\# CampusHubERP



\*\*CampusHubERP\*\* is a Python-based Campus Management System developed using Object-Oriented Programming, SQLite, SQLAlchemy ORM, and FastAPI.



The application manages student, faculty, course, and enrollment records. It also includes reporting, data validation, JSON serialization, asynchronous operations, multithreading, and multiprocessing.



\## Features



\### 1. Student Management

\- Add, view, update, and delete student records.

\- Store student ID, name, age, email, and department.

\- Search and filter student records.



\### 2. Faculty Management

\- Add, view, update, and delete faculty records.

\- Store faculty ID, name, age, email, and department.



\### 3. Course Management

\- Add, view, update, and delete courses.

\- Store course code, course name, and credits.



\### 4. Enrollment Management

\- Enroll students in courses.

\- View enrollment records.

\- Update and remove enrollments.

\- Retrieve related student and course information.



\### 5. Object-Oriented Programming

\- Classes and objects

\- Inheritance and abstraction

\- Descriptors and metaclasses

\- Abstract base classes

\- Decorators and generators



\### 6. Database Integration

\- SQLite database

\- SQLAlchemy ORM

\- Database models and repository pattern

\- CRUD operations through the database layer



\### 7. REST API

\- Developed using FastAPI.

\- Provides CRUD operations for students, faculty, courses, and enrollments.

\- Interactive API documentation through Swagger UI.



\### 8. Additional Features

\- JSON data serialization

\- Data validation

\- File handling and report generation

\- Student iteration

\- Logging and execution-time decorators

\- Asynchronous programming using asyncio

\- Multithreading

\- Multiprocessing



\## Technologies Used



\- Python

\- SQLite

\- SQLAlchemy

\- FastAPI

\- Uvicorn

\- JSON

\- Object-Oriented Programming



\## Project Structure



```text

CampusHubERP/

│

├── app/

│   ├── api/

│   │   ├── main.py

│   │   ├── You.py

│   │   ├── faculty.py

│   │   ├── courses.py

│   │   └── enrollments.py

│   │

│   ├── core/

│   ├── database/

│   │   ├── db.py

│   │   ├── models.py

│   │   └── repository.py

│   │

│   ├── models/

│   ├── services/

│   ├── utils/

│   └── main.py

│

├── data/

├── reports/

├── campushub.db

└── README.md

```



\## Installation and Setup



\### 1. Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

```



\### 2. Navigate to the Project Folder



```bash

cd campusHubERP

```



\### 3. Install Dependencies



```bash

pip install fastapi uvicorn sqlalchemy

```



\## Running the Application



\### Run the Main Application



From the project root directory:



```bash

python -m app.main

```



This runs the main CampusHubERP application, including database operations, reports, JSON serialization, asynchronous tasks, threading, and multiprocessing.



\### Run the REST API



```bash

python -m uvicorn app.api.main:app --reload

```



The API will be available at:



```text

http://127.0.0.1:8000

```



\### Swagger API Documentation



Open the following URL in your browser:



```text

http://127.0.0.1:8000/docs

```



Use Swagger UI to test the API endpoints for students, faculty, courses, and enrollments.



\## Database



CampusHubERP uses SQLite with SQLAlchemy ORM.



The database stores:

\- Students

\- Faculty

\- Courses

\- Enrollments



The repository layer handles database operations, while the service layer manages application functionality.



\## Application Architecture



```text

User

&#x20; |

&#x20; v

FastAPI

&#x20; |

&#x20; v

Service Layer

&#x20; |

&#x20; v

Repository Layer

&#x20; |

&#x20; v

SQLAlchemy ORM

&#x20; |

&#x20; v

SQLite Database

```



\## Project Objective



The objective of CampusHubERP is to develop a modular campus management application that demonstrates Python programming concepts, database integration, REST API development, and advanced programming techniques in a single project.



\## Author



Developed as an academic Python project.

