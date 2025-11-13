# TaskFlow - Task Management System

## Project Description
Web application for personal and team task management with Kanban board.

## Features
- Task creation and management
- Status tracking (To Do, In Progress, Done) 
- Assign tasks to team members
- REST API for tasks
- Due date tracking

## Technology Stack
- Python 3.x
- Flask web framework
- SQLite database
- SQLAlchemy ORM
- Git version control

## Project Structure
project_Karandasheva/   
├── app/  
│ ├── init.py # Flask application factory   
│ ├── models.py # Database models (Task)   
│ └── routes.py # API endpoints  
├── config.py # Application configuration  
├── requirements.txt # Python dependencies  
└── run.py # Application entry point  


## Quick Start

### Prerequisites
- Python 3.8+
- Git

### Installation & Running
```bash
# Clone repository
git clone https://github.com/seruru/taskflow-system.git
cd project_Karandasheva

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start development server
python run.py

# Health check (in new terminal)
python3 -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5000/').read().decode())"
```

### API Endpoints
GET / - Health check  
GET /api/tasks - Get all tasks  
POST /api/tasks - Create new task  

