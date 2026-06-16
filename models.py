from app import db
from datetime import datetime
from sqlalchemy import Text, JSON

class FlightData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String(10), nullable=False)
    destination = db.Column(db.String(10), nullable=False)
    airline = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    departure_date = db.Column(db.Date)
    booking_class = db.Column(db.String(20))
    availability = db.Column(db.Integer)
    scraped_at = db.Column(db.DateTime, default=datetime.utcnow)
    source_url = db.Column(db.String(500))

    def to_dict(self):
        return {
            'id': self.id,
            'origin': self.origin,
            'destination': self.destination,
            'airline': self.airline,
            'price': self.price,
            'departure_date': self.departure_date.isoformat() if self.departure_date else None,
            'booking_class': self.booking_class,
            'availability': self.availability,
            'scraped_at': self.scraped_at.isoformat() if self.scraped_at else None
        }

class MarketInsight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(50), nullable=False)
    insight_type = db.Column(db.String(50), nullable=False)
    insight_data = db.Column(JSON)
    ai_summary = db.Column(Text)
    confidence_score = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'route': self.route,
            'insight_type': self.insight_type,
            'insight_data': self.insight_data,
            'ai_summary': self.ai_summary,
            'confidence_score': self.confidence_score,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class ApiCache(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cache_key = db.Column(db.String(255), unique=True, nullable=False)
    cache_data = db.Column(JSON)
    expires_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def is_expired(self):
        return datetime.utcnow() > self.expires_at
