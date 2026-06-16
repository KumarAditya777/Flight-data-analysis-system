import json
import os
import logging
from collections import defaultdict

try:
    from openai import OpenAI
    OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
    openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
except ImportError:
    openai_client = None


def generate_insights(flight_data):
    try:
        return analyze_market_trends(flight_data)
    except Exception as e:
        logging.error(f"Error generating insights: {str(e)}")
        return []


def analyze_market_trends(flight_data):
    try:
        if not openai_client:
            return generate_basic_analysis(flight_data)

        data_summary = prepare_data_summary(flight_data)
        return get_ai_insights(data_summary)

    except Exception as e:
        logging.error(f"Error analyzing market trends: {str(e)}")
        return generate_basic_analysis(flight_data)


def prepare_data_summary(flight_data):
    try:
        summary = {
            'total_flights': len(flight_data),
            'routes': defaultdict(list),
            'airlines': defaultdict(list),
        }

        for flight in flight_data:
            route = f"{flight.origin}-{flight.destination}"
            summary['routes'][route].append({'price': flight.price, 'airline': flight.airline})
            summary['airlines'][flight.airline].append({'price': flight.price, 'route': route})

        summary['stats'] = calculate_statistics(flight_data)
        return summary

    except Exception as e:
        logging.error(f"Error preparing data summary: {str(e)}")
        return {}


def get_ai_insights(data_summary):
    try:
        if not openai_client:
            return []

        prompt = f"""
Analyze the following Australian domestic flight data and provide business insights for hostel planning.
Data: {json.dumps(data_summary, indent=2, default=str)}

Respond as JSON with keys: demand_trends, price_analysis, market_opportunities, hostel_strategy, seasonal_patterns.
Each key maps to an object with: summary (string), insights (list of strings).
"""
        response = openai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert travel industry analyst."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.7
        )

        content = response.choices[0].message.content
        ai_response = json.loads(content)
        return format_insights_for_display(ai_response)

    except Exception as e:
        logging.error(f"Error getting AI insights: {str(e)}")
        return []


def calculate_statistics(flight_data):
    try:
        prices = [f.price for f in flight_data if f.price]
        return {
            'total_flights': len(flight_data),
            'avg_price': sum(prices) / len(prices) if prices else 0,
            'min_price': min(prices) if prices else 0,
            'max_price': max(prices) if prices else 0,
            'unique_routes': len(set(f"{f.origin}-{f.destination}" for f in flight_data)),
            'unique_airlines': len(set(f.airline for f in flight_data if f.airline))
        }
    except Exception as e:
        logging.error(f"Error calculating statistics: {str(e)}")
        return {}


def format_insights_for_display(ai_insights):
    try:
        formatted = []
        for category, data in ai_insights.items():
            insight = {
                'title': category.replace('_', ' ').title(),
                'summary': data.get('summary', ''),
                'details': data.get('insights', []) + data.get('recommendations', []) + data.get('opportunities', []),
                'category': category
            }
            formatted.append(insight)
        return formatted
    except Exception as e:
        logging.error(f"Error formatting insights: {str(e)}")
        return []


def generate_basic_analysis(flight_data):
    try:
        if not flight_data:
            return [{'title': 'No Data Available', 'summary': 'No flight data available for analysis.', 'details': [], 'category': 'error'}]

        stats = calculate_statistics(flight_data)

        route_counts = defaultdict(int)
        for flight in flight_data:
            route_counts[f"{flight.origin}-{flight.destination}"] += 1

        popular_routes = sorted(route_counts.items(), key=lambda x: x[1], reverse=True)[:5]

        insights = [
            {
                'title': 'Popular Routes',
                'summary': f'Analysis of {stats["total_flights"]} flights across {stats["unique_routes"]} routes.',
                'details': [f"{route}: {count} flights" for route, count in popular_routes],
                'category': 'demand_trends'
            }
        ]

        if stats['avg_price'] > 0:
            insights.append({
                'title': 'Price Analysis',
                'summary': f'Average flight price: ${stats["avg_price"]:.2f}',
                'details': [
                    f"Minimum price: ${stats['min_price']:.2f}",
                    f"Maximum price: ${stats['max_price']:.2f}",
                    f"Price range: ${stats['max_price'] - stats['min_price']:.2f}"
                ],
                'category': 'price_analysis'
            })

        return insights

    except Exception as e:
        logging.error(f"Error generating basic analysis: {str(e)}")
        return [{'title': 'Analysis Error', 'summary': 'Error generating analysis.', 'details': [], 'category': 'error'}]
