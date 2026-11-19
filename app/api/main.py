from fastapi import FastAPI
from app.api import You, faculty, courses, enrollments

# Create FastAPI application
app = FastAPI(
    title="CampusHubERP API",
    description="REST API for CampusHubERP Student Management System",
    version="1.0.0"
)


# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to CampusHubERP API",
        "status": "API is running successfully"
    }


# Test Route
@app.get("/test")
def test_api():
    return {
        "message": "CampusHubERP API is working!"
    }


# Register Student API
# Register API Routers
app.include_router(You.router)
app.include_router(faculty.router)
app.include_router(courses.router)
app.include_router(enrollments.router)