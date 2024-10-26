# P2P File Sharing Platform

A Django-based platform for peer-to-peer file sharing, where users can securely upload, download, and manage files with options to cancel uploads and log out. This project is suitable for understanding Django fundamentals, session management, and file handling.

## Features
- User Authentication (Login, Logout, and Register)
- File Upload and Download Management
- Cancel Uploaded Files
- Admin Dashboard for File and User Management

## Requirements
- Python 3.8+
- Django 4.0+
- SQLite3 (default)

## Getting Started

### Clone the Repository
```bash
git clone https://github.com/RockyKGFV/a.git
cd a
```

### Setting Up the Environment
- **Python Installation**: Download Python from [python.org](https://www.python.org/downloads/) and install it.
- **Verify Installation**:
  ```bash
  python --version
  ```
- **Create and Activate Virtual Environment**:
  ```bash
  python -m venv venv
  ```
  - **Windows**: `venv\Scripts\activate`
  - **macOS/Linux**: `source venv/bin/activate`
- **Install Django**:
  ```bash
  pip install django
  ```
- **Verify Django Installation**:
  ```bash
  python -m django --version
  ```

### Initial Setup and Configuration

- **Database Migration**:
  ```bash
  python manage.py migrate
  ```

### Running the Server

To launch the server:
```bash
python manage.py runserver
```
Access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Project Structure

- **p2p_proj/** - Main Django project directory.
- **core/** - Contains app-specific files like views, templates, and static assets.
- **manage.py** - Django’s command-line utility for various administrative tasks.

## Usage

- **Login/Register**: Create or log into an account.
- **File Upload**: Upload files for sharing.
- **Manage Files**: Download or cancel uploaded files.
- **Logout**: End session, redirecting to the login page.

