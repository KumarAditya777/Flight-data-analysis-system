{% extends "base.html" %}

{% block title %}AI Insights - Airline Market Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2">
                <i data-feather="brain" class="me-2"></i>
                AI-Generated Market Insights
            </h1>
            <button type="button" class="btn btn-primary" onclick="generateNewInsights()">
                <i data-feather="refresh-cw" class="me-2"></i>
                Generate New Insights
            </button>
        </div>
    </div>
</div>

<!-- Insights Overview -->
{% if insights %}
<div class="row mb-4">
    <div class="col-12">
        <div class="alert alert-info">
            <div class="d-flex align-items-center">
                <i data-feather="info" class="me-3"></i>
                <div>
                    <h6 class="alert-heading mb-1">Market Intelligence Summary</h6>
                    <p class="mb-0">Our AI has analyzed recent flight data to provide actionable insights for your hostel business strategy. These insights are based on real-time market trends and booking patterns.</p>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Insights Cards -->
<div class="row">
    {% for insight in insights %}
    <div class="col-md-6 mb-4">
        <div class="card h-100 {% if insight.category in ['demand_trends', 'market_opportunities'] %}border-primary{% elif insight.category in ['price_analysis', 'hostel_strategy'] %}border-success{% else %}border-info{% endif %}">
            <div class="card-header {% if insight.category in ['demand_trends', 'market_opportunities'] %}bg-primary{% elif insight.category in ['price_analysis', 'hostel_strategy'] %}bg-success{% else %}bg-info{% endif %} text-white">
                <h5 class="card-title mb-0">
                    {% if insight.category == 'demand_trends' %}
                        <i data-feather="trending-up" class="me-2"></i>
                    {% elif insight.category == 'price_analysis' %}
                        <i data-feather="dollar-sign" class="me-2"></i>
                    {% elif insight.category == 'market_opportunities' %}
                        <i data-feather="target" class="me-2"></i>
                    {% elif insight.category == 'hostel_strategy' %}
                        <i data-feather="home" class="me-2"></i>
                    {% elif insight.category == 'seasonal_patterns' %}
                        <i data-feather="calendar" class="me-2"></i>
                    {% else %}
                        <i data-feather="zap" class="me-2"></i>
                    {% endif %}
                    {{ insight.title }}
                </h5>
            </div>
            <div class="card-body">
                <p class="card-text">{{ insight.summary }}</p>
                
                {% if insight.details %}
                <h6 class="mt-3 mb-2">Key Points:</h6>
                <ul class="list-unstyled">
                    {% for detail in insight.details %}
                    <li class="mb-2">
                        <i data-feather="check" class="text-success me-2" style="width: 16px; height: 16px;"></i>
                        {{ detail }}
                    </li>
                    {% endfor %}
                </ul>
                {% endif %}
            </div>
            <div class="card-footer bg-transparent">
                <small class="text-muted">
                    <i data-feather="clock" class="me-1" style="width: 14px; height: 14px;"></i>
                    Category: {{ insight.category.replace('_', ' ').title() }}
                </small>
            </div>
        </div>
    </div>
    {% endfor %}
</div>

<!-- Business Strategy Section -->
<div class="row mt-4">
    <div class="col-12">
        <div class="card border-warning">
            <div class="card-header bg-warning text-dark">
                <h5 class="card-title mb-0">
                    <i data-feather="briefcase" class="me-2"></i>
                    Recommended Business Actions
                </h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-6">
                        <h6 class="text-primary">High Priority Actions</h6>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item border-0 px-0">
                                <i data-feather="arrow-right" class="text-primary me-2" style="width: 16px; height: 16px;"></i>
                                Focus on cities with growing airline connectivity
                            </li>
                            <li class="list-group-item border-0 px-0">
                                <i data-feather="arrow-right" class="text-primary me-2" style="width: 16px; height: 16px;"></i>
                                Adjust pricing strategy based on flight cost trends
                            </li>
                            <li class="list-group-item border-0 px-0">
                                <i data-feather="arrow-right" class="text-primary me-2" style="width: 16px; height: 16px;"></i>
                                Prepare for seasonal demand fluctuations
                            </li>
                        </ul>
                    </div>
                    <div class="col-md-6">
                        <h6 class="text-info">Medium Priority Actions</h6>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item border-0 px-0">
                                <i data-feather="arrow-right" class="text-info me-2" style="width: 16px; height: 16px;"></i>
                                Monitor underserved routes for expansion opportunities
                            </li>
                            <li class="list-group-item border-0 px-0">
                                <i data-feather="arrow-right" class="text-info me-2" style="width: 16px; height: 16px;"></i>
                                Develop partnerships with airlines for guest benefits
                            </li>
                            <li class="list-group-item border-0 px-0">
                                <i data-feather="arrow-right" class="text-info me-2" style="width: 16px; height: 16px;"></i>
                                Optimize marketing spend based on travel patterns
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

{% else %}
<!-- No Insights Available -->
<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-body text-center py-5">
                <i data-feather="brain" class="text-muted mb-4" style="width: 80px; height: 80px;"></i>
                <h3 class="text-muted mb-3">No Insights Available</h3>
                <p class="text-muted mb-4">
                    To generate AI insights, we need flight data to analyze. Start by collecting flight data from the dashboard.
                </p>
                <div class="d-flex justify-content-center gap-3">
                    <a href="{{ url_for('index') }}" class="btn btn-primary">
                        <i data-feather="home" class="me-2"></i>
                        Go to Dashboard
                    </a>
                    <button type="button" class="btn btn-outline-primary" onclick="generateNewInsights()">
                        <i data-feather="refresh-cw" class="me-2"></i>
                        Try Generate Insights
                    </button>
                </div>
            </div>
        </div>
    </div>
</div>
{% endif %}

<!-- Loading Modal -->
<div class="modal fade" id="loadingModal" tabindex="-1" data-bs-backdrop="static" data-bs-keyboard="false">
    <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content">
            <div class="modal-body text-center py-4">
                <div class="spinner-border text-primary mb-3" role="status">
                    <span class="visually-hidden">Loading...</span>
                </div>
                <h5>Generating AI Insights</h5>
                <p class="text-muted">Our AI is analyzing flight data and market trends. This may take a few moments...</p>
            </div>
        </div>
    </div>
</div>

{% endblock %}

{% block scripts %}
<script>
function generateNewInsights() {
    // Show loading modal
    const loadingModal = new bootstrap.Modal(document.getElementById('loadingModal'));
    loadingModal.show();
    
    // Simulate insight generation (in real app, this would be an AJAX call)
    setTimeout(() => {
        loadingModal.hide();
        // Refresh the page to show new insights
        window.location.reload();
    }, 3000);
}

// Initialize feather icons when page loads
document.addEventListener('DOMContentLoaded', function() {
    feather.replace();
});

// Auto-refresh insights every 30 minutes
setInterval(() => {
    console.log('Auto-refreshing insights...');
    // In a real application, you might want to check for new data
    // and regenerate insights automatically
}, 30 * 60 * 1000);
</script>
{% endblock %}
