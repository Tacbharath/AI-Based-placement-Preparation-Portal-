# Local PostgreSQL 18.6 & pgAdmin 4 Setup Guide

This guide details how to configure, initialize, and verify the **Local PostgreSQL 18.6** database and **pgAdmin 4** management console for the **AI-Based Placement Preparation Portal**.

---

## 1. Prerequisites & Installation

1. **PostgreSQL 18.6 (Windows x64)**
   - Download the official installer from [PostgreSQL Official Downloads](https://www.postgresql.org/download/windows/).
   - During installation, note the **super-user password** you set for user `postgres`.
   - Default Port: `5432`.
   - Verify the Windows service `postgresql-x64-18` is running via Windows Services (`services.msc`).

2. **pgAdmin 4**
   - Installed automatically with PostgreSQL or available from [pgAdmin Download](https://www.pgadmin.org/download/).
   - Open **pgAdmin 4** from your Windows Start Menu.

---

## 2. Create the Database in pgAdmin 4

1. Launch **pgAdmin 4** and connect to your local server:
   - Expand `Servers` in the left tree.
   - Click `PostgreSQL 18` and enter your master password when prompted.
2. Create the database:
   - Right-click on **Databases** > **Create** > **Database...**
   - **Database Name**: `placement_portal`
   - **Owner**: `postgres`
   - Click **Save**.

Alternatively, via PowerShell / Command Prompt:
```powershell
# Using PostgreSQL psql CLI
psql -U postgres -c "CREATE DATABASE placement_portal;"
```

---

## 3. Configure Environment Variables (`.env`)

In the project root, open your `.env` file (or copy from `.env.example` if not created yet):
```env
# Database Settings - PostgreSQL 18.6 Local
DB_HOST=localhost
DB_PORT=5432
DB_NAME=placement_portal
DB_USER=postgres
DB_PASSWORD=YOUR_ACTUAL_POSTGRES_PASSWORD

# Optional Consolidated Connection String
DATABASE_URL=postgresql://postgres:YOUR_ACTUAL_POSTGRES_PASSWORD@localhost:5432/placement_portal

# Gemini AI API Key (Required for AI Analysis, Chat & Mock Interviews)
GEMINI_API_KEY=your_gemini_api_key_here
```

> **Security Note:** Never commit your `.env` file to Git. The `.gitignore` file is already pre-configured to ignore `.env`.

---

## 4. Install Python Dependencies

Activate your Python virtual environment and ensure all PostgreSQL database drivers are installed:
```powershell
# Activate your virtual environment
.venv\Scripts\Activate.ps1

# Install requirements
pip install -r requirements.txt
```

Core database packages:
- `psycopg2-binary>=2.9.11` (High-performance PostgreSQL driver for Python)
- `python-dotenv==1.2.3` (Environment variable loader)
- `bcrypt==5.0.0` (Cryptographic password hashing)

---

## 5. Initialize Database Schema & Seed Data

Execute the automated initialization script to build all 55+ production tables and seed initial job roles, interview banks, aptitude questions, and admin access:

```powershell
.venv\Scripts\python.exe -c "from backend.database import db_helper; db_helper.initialize_database()"
```

Output:
```text
[DATABASE] Initializing PostgreSQL database...
[DATABASE] PostgreSQL schema executed and verified successfully.
[OPPORTUNITIES SEED] Total 350 opportunities processed...
Database seeding completed.
```

---

## 6. Test Database Connectivity

Run the connection verification utility to confirm that Flask can talk to PostgreSQL 18.6:

```powershell
.venv\Scripts\python.exe backend/database/connection.py
```

Expected output:
```text
============================================================
AI PLACEMENT PORTAL -- POSTGRESQL 18 CONNECTION TEST
============================================================
Host:     127.0.0.1
Port:     5432
Database: placement_portal
User:     postgres
Status:   CONNECTED (SUCCESS)
Version:  PostgreSQL 18.6 on x86_64-windows...
Tables:   56 tables present in schema 'public'
------------------------------------------------------------
pgAdmin 4 Inspection Path:
  Servers > PostgreSQL 18 > Databases > placement_portal > Schemas > public > Tables
============================================================
```

---

## 7. Verify Tables Inside pgAdmin 4

In pgAdmin 4, navigate through the Object Explorer tree:
```text
Servers
  └── PostgreSQL 18
        └── Databases
              └── placement_portal
                    └── Schemas
                          └── public
                                └── Tables
```

You will see all application tables:
- `students` (Student authentication & credentials)
- `student_profiles` (College, department, target role, Private vs Government sector)
- `student_skills` (Extracted & declared candidate skills)
- `resumes` (Uploaded PDF references and extracted plain text)
- `resume_analysis` (ATS scores, strengths, weaknesses, missing keywords)
- `resume_versions` (Historical resume drafts & scores)
- `skill_gap_results` (Candidate vs target role gap percentages)
- `aptitude_questions` & `aptitude_results` (Practice tests)
- `coding_questions` & `coding_submissions` (Coding compiler evaluator)
- `interview_questions` & `student_interview_progress` (Mock interview responses)
- `opportunities`, `private_jobs`, `government_jobs` (Placement drives & listings)
- `notifications` & `email_queue` (Alerts & scheduled reminders)
- `student_progress` & `readiness_history` (Readiness calculation metrics)

To view live data in any table (e.g. `students`):
- Right-click the table > **View/Edit Data** > **All Rows**.

---

## 8. Run the Flask Web Application

Start the Flask development server:
```powershell
.venv\Scripts\python.exe run.py
```
Or:
```powershell
.venv\Scripts\python.exe -m backend.app
```

Access the portal in your browser:
- **Student / Public Portal**: `http://localhost:5000`
- **Student Login**: `http://localhost:5000/login`
- **Student Registration**: `http://localhost:5000/register`
- **Admin Portal**: `http://localhost:5000/admin/login`

---

## 9. Troubleshooting

| Issue | Likely Cause | Solution |
| :--- | :--- | :--- |
| `connection refused / 10061` | PostgreSQL service is stopped | Start service `postgresql-x64-18` in `services.msc` or via `net start postgresql-x64-18` |
| `password authentication failed` | Incorrect password in `.env` | Update `DB_PASSWORD` in `.env` to match your `postgres` master password |
| `database "placement_portal" does not exist` | Database not created | Open pgAdmin 4 and create database named `placement_portal` |
| `psycopg2 driver missing` | Environment missing dependencies | Run `.venv\Scripts\pip install -r requirements.txt` |
