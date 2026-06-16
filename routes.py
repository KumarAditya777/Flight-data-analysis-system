import json
import logging
from datetime import datetime, timedelta
from collections import defaultdict
from flask import render_template, request, redirect, url_for, flash, jsonify
from app import app, db
from models import FlightData, MarketInsight
from sqlalchemy import func


@app.route('/')
def index():
    total_flights = FlightData.query.count()
    week_ago = datetime.utcnow() - timedelta(days=7)
    recent_flights = FlightData.query.filter(FlightData.scraped_at >= week_ago).count()

    popular_routes = db.session.query(
        FlightData.origin,
        FlightData.destination,
        func.count(FlightData.id).label('count')
    ).group_by(FlightData.origin, FlightData.destination)\
     .order_by(func.count(FlightData.id).desc()).limit(5).all()

    recent_insights = MarketInsight.query.order_by(MarketInsight.created_at.desc()).limit(5).all()

    return render_template('index.html',
        total_flights=total_flights,
        recent_flights=recent_flights,
        popular_routes=popular_routes,
        recent_insights=recent_insights
    )


@app.route('/analysis')
def analysis():
    origin = request.args.get('origin', '')
    destination = request.args.get('destination', '')
    days = int(request.args.get('days', 30))

    query = FlightData.query
    if origin:
        query = query.filter(FlightData.origin == origin.upper())
    if destination:
        query = query.filter(FlightData.destination == destination.upper())

    cutoff = datetime.utcnow() - timedelta(days=days)
    query = query.filter(FlightData.scraped_at >= cutoff)

    flights = query.order_by(FlightData.scraped_at.desc()).limit(500).all()
    chart_data = _build_chart_data(flights)

    return render_template('analysis.html',
        flights=flights,
        chart_data=json.dumps(chart_data),
        origin=origin,
        destination=destination,
        days=days
    )


@app.route('/insights')
def insights():
    from ai_analyzer import generate_insights

    flight_data = FlightData.query.order_by(FlightData.scraped_at.desc()).limit(200).all()

    insights_list = []
    if flight_data:
        insights_list = generate_insights(flight_data)

    if not insights_list:
        db_insights = MarketInsight.query.order_by(MarketInsight.created_at.desc()).limit(10).all()
        insights_list = [
            {
                'title': i.insight_type.replace('_', ' ').title(),
                'summary': i.ai_summary or '',
                'details': [],
                'category': i.insight_type
            }
            for i in db_insights
        ]

    return render_template('insights.html', insights=insights_list)


@app.route('/tutorial')
def tutorial():
    return render_template('tutorial.html')


@app.route('/logs')
def logs():
    return render_template('logs.html')


@app.route('/collect', methods=['POST'])
def collect_data():
    from data_collector import collect_flight_data

    origin = request.form.get('origin', 'SYD')
    destination = request.form.get('destination', 'MEL')

    try:
        flights = collect_flight_data(origin, destination)
        flash(f'Successfully collected {len(flights)} flight records for {origin} → {destination}', 'success')
    except Exception as e:
        logging.error(f"Data collection error: {str(e)}")
        flash(f'Error collecting data: {str(e)}', 'error')

    return redirect(url_for('index'))


def _build_chart_data(flights):
    price_trends = []
    route_counts = defaultdict(int)
    airline_counts = defaultdict(int)

    for f in flights:
        route = f"{f.origin}-{f.destination}"
        route_counts[route] += 1
        if f.airline:
            airline_counts[f.airline] += 1
        if f.price and f.departure_date:
            price_trends.append({
                'route': route,
                'date': f.departure_date.isoformat(),
                'price': f.price
            })

    popular_routes = [{'route': r, 'count': c} for r, c in sorted(route_counts.items(), key=lambda x: -x[1])[:10]]
    airline_share = [{'airline': a, 'count': c} for a, c in sorted(airline_counts.items(), key=lambda x: -x[1])[:8]]

    return {
        'price_trends': price_trends[:100],
        'popular_routes': popular_routes,
        'airline_share': airline_share
    }
