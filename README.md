# BrainBuddy — Web Pitch Deck

## Deploy to Heroku

### Prerequisites
- [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) installed
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

### Local development
```bash
pip install flask gunicorn
python app.py
# Open http://localhost:5000
```
