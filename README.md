# Flight Data Analysis System

A Flask web application that collects and analyzes Australian domestic flight data, generating AI-powered market insights to help with business strategy and travel planning.

## Features

- **Market Dashboard** — live stats on total flights, popular routes, and AI-generated insights
- **AI Analysis** — uses GPT-4o to identify demand trends, price patterns, and market opportunities
- **Route Analytics** — tracks and visualizes the most popular Australian domestic routes
- **Data Collection** — fetches real-time flight data with sample data pre-loaded for demo
- **SQLite Storage** — persistent database for flight records and generated insights

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask, Flask-SQLAlchemy |
| Database | SQLite |
| AI | OpenAI GPT-4o |
| Frontend | Jinja2 templates, Bootstrap 5, Feather Icons |

## Project Structure

```
Flight-data-analysis-system/
├── app.py              # Flask app initialization and DB setup
├── main.py             # Entry point
├── routes.py           # URL routes and view logic
├── models.py           # SQLAlchemy database models
├── ai_analyzer.py      # OpenAI integration for market insights
├── data_collector.py   # Flight data collection and sample data
├── web_scraper.py      # Web scraping utilities
├── base.html           # Base HTML template
├── insights.html       # Insights page template
├── tutorial.html       # Tutorial page template
└── custom.css          # Custom styles
```

## Getting Started

### Prerequisites

- Python 3.11+
- OpenAI API key (optional — falls back to basic analysis without it)

### Installation

```bash
git clone https://github.com/KumarAditya777/Flight-data-analysis-system.git
cd Flight-data-analysis-system
pip install flask flask-sqlalchemy werkzeug openai
```

### Running the App

```bash
# Optional: set your OpenAI API key for AI-powered insights
export OPENAI_API_KEY=your_key_here   # Linux/Mac
set OPENAI_API_KEY=your_key_here      # Windows

python main.py
```

Open your browser at `http://localhost:5000`

## How It Works

1. **Collect Data** — click "Collect New Data" on the dashboard, select origin and destination airports
2. **View Analytics** — the dashboard shows route popularity, flight counts, and recent insights
3. **AI Insights** — the system uses GPT-4o to analyze patterns and generate hostel/travel business recommendations
4. **Explore Routes** — browse the most popular Australian domestic routes (SYD, MEL, BNE, PER, etc.)

## Supported Airports

Sydney (SYD), Melbourne (MEL), Brisbane (BNE), Perth (PER), Adelaide (ADL), Darwin (DRW), Cairns (CNS), Gold Coast (OOL), Canberra (CBR), Hobart (HBA)

## Author

**Kumar Aaditya** — [GitHub](https://github.com/KumarAditya777)
