# AI-Based Placement Preparation Portal 🚀

A comprehensive, production-ready AI-driven portal designed to prepare students for campus placements and government recruitment examinations.

---

## 🌟 Key Modules & Features

1. **Student Authentication & Profile**: Registration, BCrypt password hashing, target career interest selection, and skills synchronization.
2. **Student Dashboard**: Live readiness progress meter, module quick-links, and activity statistics.
3. **AI Resume Analyzer**: PDF upload, ATS match scoring (0-100), section detection, missing keywords extraction for targeted job roles, strengths/weaknesses breakdown, and actionable improvement recommendations.
4. **Skill Gap Analysis**: Compares candidate profile skills against industry requirements across 6 primary tech career tracks and suggests structured learning pathways.
5. **Quantitative Aptitude Hub**: Timed multi-category quizzes (Quantitative, Logical, Verbal, General Knowledge) with instant scoring and detailed step-by-step explanations.
6. **Coding Practice Sandbox**: Multi-language programming judge (Python, Java, C, C++) with test case execution and status verification (Accepted, Wrong Answer, etc.).
7. **AI Mock Interviews**: Profile-grounded interview question generator (HR and Technical domains) with candidate response evaluation and AI feedback.
8. **AI Placement Chatbot**: Interactive placement preparation career mentor.
9. **Private Job Board**: Filter and search corporate openings with direct application links and bookmarking.
10. **Government Job Portal**: Central and state exam notifications, eligibility tracking, and application deadlines.
11. **Admin Control Console**: Full CRUD management over students, aptitude tests, coding challenges, interview questions, corporate jobs, and government vacancies.

---

## 📂 Project Structure

```text
AI-Placement-Portal/
├── app.py                      # Flask application entry point & Jinja filters
├── config.py                   # Production & environment configuration
├── requirements.txt            # Python production dependencies (Gunicorn, psycopg2, Flask)
├── render.yaml                 # 1-Click Render Blueprint deployment specification
├── Procfile                    # Cloud container process specification
├── verify_setup.py             # System & database verification utility
├── test_routes.py              # Automated 17-route integration test suite
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore rules for secrets, DBs, and virtualenvs
├── database/
│   ├── db_helper.py            # Unified database facade (PostgreSQL, SQLite, MySQL)
│   ├── schema_postgres.sql     # Production PostgreSQL database schema
│   ├── schema_sqlite.sql       # SQLite database schema
│   └── schema.sql              # MySQL database schema
├── routes/
│   ├── admin.py                # Admin console CRUD routes
│   ├── aptitude.py             # Aptitude quiz & test execution routes
│   ├── auth.py                 # Student login, registration, and profile routes
│   ├── chatbot.py              # AI chatbot endpoints
│   ├── coding.py               # Coding practice & test case evaluator routes
│   ├── government_jobs.py      # Govt exam & job listing routes
│   ├── interview.py            # AI Mock interview generation & grading routes
│   ├── jobs.py                 # Corporate job board & bookmarking routes
│   ├── resume.py               # PDF resume parsing & ATS analysis routes
│   ├── skill_gap.py            # Skill gap matching routes
│   └── student.py              # Student dashboard & progress routes
├── services/
│   ├── ai_service.py           # Gemini AI integration with safe mock fallbacks
│   ├── resume_analyzer.py      # PyPDF text extraction & heuristics
│   └── skill_gap_service.py    # Gap calculation & recommendations engine
├── static/
│   ├── css/
│   │   └── styles.css          # Modern dark-mode responsive design system
│   ├── js/
│   │   └── main.js             # Modals, toasts, sidebar, and client interactions
│   └── uploads/
│       └── resumes/            # Local storage for uploaded PDF resumes (.gitkeep)
└── templates/                  # Jinja2 HTML templates
    ├── admin_dashboard.html
    ├── admin_login.html
    ├── aptitude.html
    ├── aptitude_result.html
    ├── aptitude_test.html
    ├── base.html
    ├── chatbot.html
    ├── coding.html
    ├── coding_workspace.html
    ├── dashboard.html
    ├── forgot_password.html
    ├── gov_jobs.html
    ├── home.html
    ├── interview.html
    ├── interview_practice.html
    ├── jobs.html
    ├── login.html
    ├── profile.html
    ├── register.html
    ├── resume.html
    ├── saved_jobs.html
    └── skill_gap.html
```

---

## 🚀 How to Deploy on Render (Step-by-Step)

### Step 1: Upload Project to GitHub
1. Initialize git in your local directory:
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Production Ready AI Placement Portal"
   ```
2. Create a new repository on [GitHub](https://github.com/new) (e.g. `ai-placement-portal`).
3. Link and push your code:
   ```bash
   git remote add origin https://github.com/<your-username>/ai-placement-portal.git
   git branch -M main
   git push -u origin main
   ```

---

### Step 2: Create a Render Account
1. Visit [render.com](https://render.com) and click **Sign Up** (use your GitHub account for easy integration).

---

### Step 3: Deploy via Option A (Recommended: Render Blueprint / 1-Click)
Since this repository includes a `render.yaml` file:
1. In Render Dashboard, click **New +** -> **Blueprint**.
2. Select your `ai-placement-portal` GitHub repository.
3. Render will automatically detect both the **Web Service** (`placement-prep-portal`) and **PostgreSQL Database** (`placement-db`).
4. (Optional) Set your `GEMINI_API_KEY` under Environment Variables.
5. Click **Apply**. Render will automatically build the service, spin up PostgreSQL, initialize the schema, seed the default admin/job data, and launch your live URL!

---

### Step 4: Deploy via Option B (Manual Web Service)
If creating the service manually:
1. **Create a PostgreSQL Database**:
   - Go to **New +** -> **PostgreSQL**.
   - Name: `placement-db`, Database: `placement_portal`, User: `placement_user`, Plan: `Free`.
   - Click **Create Database** and copy the **Internal Database URL**.
2. **Create a Web Service**:
   - Go to **New +** -> **Web Service**.
   - Connect your GitHub repository.
   - Configure:
     - **Name**: `ai-placement-portal`
     - **Runtime**: `Python 3`
     - **Region**: `Oregon (US West)` (or closest region)
     - **Branch**: `main`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
     - **Instance Type**: `Free`
3. **Set Environment Variables**:
   Under **Environment** tab, add:
   | Key | Value | Notes |
   |---|---|---|
   | `FLASK_ENV` | `production` | Enables production mode |
   | `FLASK_DEBUG` | `False` | Disables debug mode |
   | `SECRET_KEY` | `your-secure-random-secret-key` | Random 32-character string |
   | `DATABASE_URL` | `postgresql://...` | Internal/External DB URL from step 1 |
   | `GEMINI_API_KEY` | `your_gemini_api_key` | Optional (runs in Mock Mode if left blank) |
4. Click **Deploy Web Service**.

---

## 🔑 Default Credentials & Access

| Role | Login URL | Default Username / Email | Default Password |
|---|---|---|---|
| **Admin** | `/admin/login` | `admin` | `admin123` |
| **Student** | `/login` or `/register` | Self-registered email | Self-registered password |

---

## 🌐 Custom Domain Configuration (www.placementpreparationportal.com)

The portal is configured for production under the custom domain:
- **Primary Domain**: `www.placementpreparationportal.com`
- **Apex Domain**: `placementpreparationportal.com`
- **Canonical APP_URL**: `https://www.placementpreparationportal.com`

### 1. DNS Setup Guide
To point your custom domain to your production server (e.g. Render, Cloud, VPS):
1. **CNAME Record** (for `www` subdomain):
   - **Name / Host**: `www`
   - **Type**: `CNAME`
   - **Target / Value**: Your host's assigned URL (e.g., `prepportal.onrender.com` or server address)
   - **TTL**: Auto or `3600`
2. **A / ALIAS / ANAME Record** (for root apex domain):
   - **Name / Host**: `@` (or leave blank)
   - **Type**: `A` or `ALIAS`
   - **Target / Value**: Hosting provider IP or apex redirect
   - **TTL**: Auto or `3600`

> ⚠️ **Important DNS Note**: A custom domain will work publicly only after your DNS records are pointed and propagated to the live host server.

### 2. Production Environment Variables (.env)
Ensure the following are set in your production environment:
```env
FLASK_ENV=production
FLASK_DEBUG=False
CUSTOM_DOMAIN=www.placementpreparationportal.com
ALLOWED_HOSTS=www.placementpreparationportal.com,placementpreparationportal.com
APP_URL=https://www.placementpreparationportal.com
CORS_ORIGINS=https://www.placementpreparationportal.com,https://placementpreparationportal.com
PORT=5000
```

---

---

## 📧 Gmail SMTP Email Setup Guide (Production & Local Delivery)

The portal features an enterprise email delivery system supporting direct Gmail SMTP delivery, modular Jinja2 HTML templates, automatic plain-text fallbacks, student opt-in preferences, and zero-crash development safe mode.

### 1. Generating a Google App Password (Step-by-Step)
Standard Gmail passwords will **not** work due to Google's mandatory 2-Factor Authentication security policies. You must generate a dedicated 16-character **Google App Password**:

1. Go to your [Google Account Security Settings](https://myaccount.google.com/security).
2. Under **"How you sign in to Google"**, ensure **2-Step Verification** is turned **ON**.
3. Search for **"App passwords"** or navigate directly to [https://myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
4. Enter an app name (e.g. `PrepPortal`) and click **Create**.
5. Copy the generated **16-character password** (format: `xxxx xxxx xxxx xxxx`).

### 2. Configuring Environment Variables (.env)
Add your credentials to `.env`:

```env
# =========================================================================
# GMAIL SMTP NOTIFICATION SETTINGS
# =========================================================================
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USE_SSL=false
MAIL_USERNAME=your_email@gmail.com
MAIL_PASSWORD=your_16_character_app_password
MAIL_DEFAULT_SENDER="Prep Portal <your_email@gmail.com>"
ADMIN_NOTIFICATION_EMAIL=admin@prepportal.com
APP_URL=http://127.0.0.1:5000
```

> **Development Safe Mode**: If `MAIL_USERNAME` or `MAIL_PASSWORD` are not configured in `.env`, the application automatically operates in zero-crash safe mode. All email notifications are logged to `backend/logs/email_notifications.log` and tracked with status `skipped` in the database without crashing or interrupting student workflows.

### 3. Testing Email Delivery
- **Admin Console**: Navigate to `/admin/email-management` to inspect live SMTP server configuration, review real-time delivery audit logs, retry failed emails, and test end-to-end delivery using the **Send Test Email** tool.
- **Automated Test Suite**: Run `python test_email_notifications_full.py` to verify email triggers across registration, password resets, placement drives, study reminders, and preference toggles.

---

## 🧪 Comprehensive Automated Test Suites

Run the complete test suite locally anytime:

```powershell
.\.venv\Scripts\python.exe test_email_notifications_full.py
.\.venv\Scripts\python.exe test_advanced_features.py
.\.venv\Scripts\python.exe test_routes.py
```

---

## 🛠 Local Development Setup 

To run locally on your machine:
```bash
# 1. Clone repo
git clone https://github.com/<your-username>/ai-placement-portal.git
cd ai-placement-portal

# 2. Activate virtual environment (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. Copy environment template
cp .env.example .env

# 4. Start Flask server
python run.py
```
Open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.
