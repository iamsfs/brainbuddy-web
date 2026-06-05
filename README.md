# BrainBuddy Web

BrainBuddy Web is an AI-powered clinical decision support and physician documentation platform designed to assist healthcare professionals with differential diagnosis generation, clinical workflows, medical scoring systems, and structured physician chart creation.

## Features

- Clinical decision support engine
- Differential diagnosis generation
- Physician chart generation
- Interactive medical workflow dashboard
- Syndrome and scoring engines
- Ophthalmology templates
- Emergency medicine workflows
- AI-assisted clinical documentation

## Technology Stack

- Python
- Flask
- HTML/CSS/JavaScript
- Clinical knowledge engines
- Dynamic physician chart generation

## Live Demo

BrainBuddy is actively deployed and maintained with continuous feature updates and clinical workflow improvements.

## Roadmap

- FHIR export support
- Mobile UI optimization
- Advanced physician analytics
- Expanded specialty templates
- Improved diagnosis ranking algorithms

## Deployment

## Deployment to Heroku

### Prerequisites

- Heroku CLI installed
- Heroku account

### Deploy in 4 commands

```bash
# 1. Login to Heroku
heroku login

# 2. Create app
heroku create brainbuddy-pitch

# 3. Deploy
git init
git add .
git commit -m "BrainBuddy pitch deck"
git push heroku main

# 4. Open
heroku open
```

### Files

- `index.html` — Full pitch deck / landing page (self-contained, screenshots embedded)
- `app.py` — Flask server
- `Procfile` — Heroku process definition
- `requirements.txt` — Python dependencies
- `runtime.txt` — Python version

### Local Development

```bash
pip install flask gunicorn
python app.py

# Open http://localhost:5000
```
