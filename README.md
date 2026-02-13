<p align="center">
  <img src="medicure/static/images/favicon.png" alt="MediCure Logo" width="120"/>
</p>

<h1 align="center">🏥 MediCure Enhanced</h1>

<p align="center">
  <b>An AI-Powered, Dockerized Healthcare Management Platform</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Django-5.1-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django"/>
  <img src="https://img.shields.io/badge/Docker-24.0-2496ED?style=for-the-badge&logo=docker&logoColor=white" alt="Docker"/>
  <img src="https://img.shields.io/badge/PostgreSQL-15-336791?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL"/>
  <img src="https://img.shields.io/badge/ML-XGBoost-FF6600?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost"/>
</p>

<p align="center">
  <a href="https://medicureenhanced.onrender.com"><img src="https://img.shields.io/badge/🌐_Live_Demo-medicureenhanced.onrender.com-00C853?style=for-the-badge" alt="Live Demo"/></a>
  <img src="https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge" alt="Deployed"/>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-quick-start">Quick Start</a> •
  <a href="#-deployment">Deployment</a>
</p>

---

## 📖 Overview

**MediCure Enhanced** is a comprehensive, full-stack healthcare platform that combines robust patient-doctor management with cutting-edge **Machine Learning** for disease prediction and personalized health recommendations.

It is fully **containerized with Docker**, enabling instant setup and seamless deployment to any cloud platform.

---

## ✨ Features

<table>
<tr>
<td width="33%" align="center">
<h3>🧠 AI/ML Engine</h3>
<ul align="left">
<li>Disease Prediction (XGBoost)</li>
<li>Mental Health Risk Assessment</li>
<li>PCOS Prediction Model</li>
<li>Obesity Risk Analyzer</li>
<li>Smart Diet & Exercise Plans</li>
</ul>
</td>
<td width="33%" align="center">
<h3>👤 User Management</h3>
<ul align="left">
<li>JWT + Session Auth</li>
<li>Email Verification Flow</li>
<li>Role-Based Access (Patient/Doctor/Admin)</li>
<li>Secure Password Reset</li>
</ul>
</td>
<td width="33%" align="center">
<h3>📅 Appointments</h3>
<ul align="left">
<li>Doctor Discovery</li>
<li>Slot Booking System</li>
<li>Accept/Reject Workflow</li>
<li>Email Notifications</li>
</ul>
</td>
</tr>
</table>

---

## 🏗️ Architecture

### High-Level System Architecture

```mermaid
graph LR
    subgraph "Client Layer"
        A[Web Browser]
    end

    subgraph "Application Layer (Docker)"
        B[Gunicorn WSGI Server]
        C[Django Application]
        D[WhiteNoise Static Files]
    end

    subgraph "Data Layer"
        E[(PostgreSQL DB)]
        F[ML Models .pkl]
    end

    subgraph "External Services"
        G[Gmail SMTP]
        H[Razorpay API]
    end

    A --> B --> C
    C --> D
    C --> E
    C --> F
    C --> G
    C --> H
```

### Application Flow

```mermaid
sequenceDiagram
    participant U as User (Patient)
    participant W as Web App
    participant D as Django Backend
    participant ML as ML Engine
    participant DB as PostgreSQL

    U->>W: Enter Symptoms
    W->>D: POST /disease/predict/
    D->>ML: Load XGBoost Model
    ML-->>D: Prediction Result
    D->>DB: Log Prediction
    D-->>W: JSON Response
    W-->>U: Display Results
```

---



## 🚀 Quick Start

### Prerequisites

*   [Docker Desktop](https://www.docker.com/products/docker-desktop/)
*   Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/2004Shivam/MedicureEnhanced.git
cd MedicureEnhanced/medicure

# 2. Create environment file
cp .env.example .env  # Then edit with your credentials

# 3. Build and run with Docker
docker compose up --build

# 4. In a new terminal, run migrations
docker compose exec web python manage.py migrate

# 5. Create superuser
docker compose exec web python manage.py createsuperuser
```

### Access

| Service | URL |
|:--------|:----|
| 🌐 Web App | [http://localhost:8000](http://localhost:8000) |
| 🔧 Admin Panel | [http://localhost:8000/admin](http://localhost:8000/admin) |

### 🛠️ Troubleshooting

**Issue: `ModuleNotFoundError: No module named 'pkg_resources'`**
- This is due to `setuptools` removing `pkg_resources` in recent versions.
- **Fix:** Ensure `Dockerfile` pins `setuptools==69.5.1`.

**Issue: `psycopg2.OperationalError: server does not support SSL`**
- Occurs when running locally with `DEBUG=True`.
- **Fix:** `settings.py` is configured to only require SSL when `DEBUG=False` (Production). ensure your `.env` has `DEBUG=True` for local development.

---

## ☁️ Deployment

This project is optimized for **free-tier cloud deployment**:

| Component | Service | Cost |
|:----------|:--------|:----:|
| **Database** | [Neon.tech](https://neon.tech) | Rs.0 |
| **Application** | [Render.com](https://render.com) | Rs.0 |
| **Keep-Alive** | [UptimeRobot](https://uptimerobot.com) | Rs.0 |

See `deployment_plan.md` for step-by-step instructions.

---

## 🛠️ Tech Stack

<table>
<tr>
<td align="center" width="20%"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/><br/><b>Python 3.12</b></td>
<td align="center" width="20%"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="40"/><br/><b>Django 5.1</b></td>
<td align="center" width="20%"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" width="40"/><br/><b>PostgreSQL</b></td>
<td align="center" width="20%"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="40"/><br/><b>Docker</b></td>
<td align="center" width="20%"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tailwindcss/tailwindcss-original.svg" width="40"/><br/><b>TailwindCSS</b></td>
</tr>
</table>

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1.  **Fork** the repository
2.  **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3.  **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4.  **Push** to the branch (`git push origin feature/AmazingFeature`)
5.  **Open** a Pull Request

---

<p align="center">
  Built with ❤️ by <b>Shivam</b> | © 2026
</p>
