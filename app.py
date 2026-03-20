{% extends "base.html" %}

{% block title %}Dashboard - Airline Market Analytics{% endblock %}

{% block content %}
<div class="row">
    <div class="col-12">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2">
                <i data-feather="dashboard" class="me-2"></i>
                Market Dashboard
            </h1>
            <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#dataCollectionModal">
                <i data-feather="download" class="me-2"></i>
                Collect New Data
            </button>
        </div>
    </div>
</div>

<!-- Stats Cards -->
<div class="row mb-4">
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <div class="d-flex align-items-center">
                    <div class="flex-grow-1">
                        <h6 class="card-title text-muted mb-1">Total Flights</h6>
                        <h3 class="mb-0">{{ "{:,}".format(total_flights | default(0)) }}</h3>
                    </div>
                    <div class="text-primary">
                        <i data-feather="airplane" style="width: 32px; height: 32px;"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <div class="d-flex align-items-center">
                    <div class="flex-grow-1">
                        <h6 class="card-title text-muted mb-1">Recent Flights</h6>
                        <h3 class="mb-0">{{ recent_flights | default(0) }}</h3>
                        <small class="text-muted">Last 7 days</small>
                    </div>
                    <div class="text-success">
                        <i data-feather="trending-up" style="width: 32px; height: 32px;"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <div class="d-flex align-items-center">
                    <div class="flex-grow-1">
                        <h6 class="card-title text-muted mb-1">Popular Routes</h6>
                        <h3 class="mb-0">{{ popular_routes | length }}</h3>
                        <small class="text-muted">Active routes</small>
                    </div>
                    <div class="text-info">
                        <i data-feather="map" style="width: 32px; height: 32px;"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
    
    <div class="col-md-3">
        <div class="card">
            <div class="card-body">
                <div class="d-flex align-items-center">
                    <div class="flex-grow-1">
                        <h6 class="card-title text-muted mb-1">AI Insights</h6>
                        <h3 class="mb-0">{{ recent_insights | length }}</h3>
                        <small class="text-muted">Generated</small>
                    </div>
                    <div class="text-warning">
                        <i data-feather="brain" style="width: 32px; height: 32px;"></i>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Popular Routes -->
<div class="row mb-4">
    <div class="col-md-6">
        <div class="card h-100">
            <div class="card-header">
                <h5 class="card-title mb-0">
                    <i data-feather="map-pin" class="me-2"></i>
                    Most Popular Routes
                </h5>
            </div>
            <div class="card-body">
                {% if popular_routes %}
                    <div class="list-group list-group-flush">
                        {% for route in popular_routes[:5] %}
                        <div class="list-group-item bg-transparent border-0 px-0">
                            <div class="d-flex justify-content-between align-items-center">
                                <div>
                                    <h6 class="mb-1">{{ route.origin }} → {{ route.destination }}</h6>
                                    <small class="text-muted">{{ route.count }} flights tracked</small>
                                </div>
                                <span class="badge bg-primary rounded-pill">{{ route.count }}</span>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                {% else %}
                    <div class="text-center py-4">
                        <i data-feather="inbox" class="text-muted mb-3" style="width: 48px; height: 48px;"></i>
                        <p class="text-muted">No route data available yet. Start by collecting flight data.</p>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
    
    <div class="col-md-6">
        <div class="card h-100">
            <div class="card-header">
                <h5 class="card-title mb-0">
                    <i data-feather="zap" class="me-2"></i>
                    Recent AI Insights
                </h5>
            </div>
            <div class="card-body">
                {% if recent_insights %}
                    <div class="list-group list-group-flush">
                        {% for insight in recent_insights[:5] %}
                        <div class="list-group-item bg-transparent border-0 px-0">
                            <div class="d-flex justify-content-between align-items-start">
                                <div class="flex-grow-1">
                                    <h6 class="mb-1">{{ insight.insight_type.replace('_', ' ').title() }}</h6>
                                    <p class="mb-1 small">{{ insight.ai_summary[:100] }}{% if insight.ai_summary|length > 100 %}...{% endif %}</p>
                                    <small class="text-muted">{{ insight.created_at.strftime('%m/%d %H:%M') }}</small>
                                </div>
                            </div>
                        </div>
                        {% endfor %}
                    </div>
                    <div class="text-center mt-3">
                        <a href="{{ url_for('insights') }}" class="btn btn-outline-primary btn-sm">
                            View All Insights
                        </a>
                    </div>
                {% else %}
                    <div class="text-center py-4">
                        <i data-feather="brain" class="text-muted mb-3" style="width: 48px; height: 48px;"></i>
                        <p class="text-muted">No insights generated yet. Collect flight data to generate AI insights.</p>
                    </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>

<!-- Quick Actions -->
<div class="row">
    <div class="col-12">
        <div class="card">
            <div class="card-header">
                <h5 class="card-title mb-0">
                    <i data-feather="activity" class="me-2"></i>
                    Quick Actions
                </h5>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="col-md-4 mb-3">
                        <div class="d-grid">
                            <a href="{{ url_for('analysis') }}" class="btn btn-outline-primary">
                                <i data-feather="bar-chart-2" class="me-2"></i>
                                View Analysis
                            </a>
                        </div>
                    </div>
                    <div class="col-md-4 mb-3">
                        <div class="d-grid">
                            <a href="{{ url_for('insights') }}" class="btn btn-outline-info">
                                <i data-feather="zap" class="me-2"></i>
                                Generate Insights
                            </a>
                        </div>
                    </div>
                    <div class="col-md-4 mb-3">
                        <div class="d-grid">
                            <button type="button" class="btn btn-outline-success" data-bs-toggle="modal" data-bs-target="#dataCollectionModal">
                                <i data-feather="download" class="me-2"></i>
                                Collect Data
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<!-- Data Collection Modal -->
<div class="modal fade" id="dataCollectionModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">
                    <i data-feather="download" class="me-2"></i>
                    Collect Flight Data
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
            </div>
            <form method="POST" action="{{ url_for('collect_data') }}" id="dataCollectionForm">
                <div class="modal-body">
                    <div class="mb-3">
                        <label for="origin" class="form-label">Origin Airport</label>
                        <select class="form-select" id="origin" name="origin" required>
                            <option value="SYD">Sydney (SYD)</option>
                            <option value="MEL">Melbourne (MEL)</option>
                            <option value="BNE">Brisbane (BNE)</option>
                            <option value="PER">Perth (PER)</option>
                            <option value="ADL">Adelaide (ADL)</option>
                            <option value="DRW">Darwin (DRW)</option>
                            <option value="CNS">Cairns (CNS)</option>
                            <option value="OOL">Gold Coast (OOL)</option>
                            <option value="CBR">Canberra (CBR)</option>
                            <option value="HBA">Hobart (HBA)</option>
                        </select>
                    </div>
                    <div class="mb-3">
                        <label for="destination" class="form-label">Destination Airport</label>
                        <select class="form-select" id="destination" name="destination" required>
                            <option value="MEL">Melbourne (MEL)</option>
                            <option value="SYD">Sydney (SYD)</option>
                            <option value="BNE">Brisbane (BNE)</option>
                            <option value="PER">Perth (PER)</option>
                            <option value="ADL">Adelaide (ADL)</option>
                            <option value="DRW">Darwin (DRW)</option>
                            <option value="CNS">Cairns (CNS)</option>
                            <option value="OOL">Gold Coast (OOL)</option>
                            <option value="CBR">Canberra (CBR)</option>
                            <option value="HBA">Hobart (HBA)</option>
                        </select>
                    </div>
                    <div class="alert alert-info">
                        <i data-feather="info" class="me-2"></i>
                        <strong>Note:</strong> This will collect comprehensive flight data including sample data for demonstration and attempt to gather real market data.
                    </div>
                    
                    <div class="mb-3">
                        <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="showLogs" name="show_logs" value="1">
                            <label class="form-check-label" for="showLogs">
                                Show real-time collection logs
                            </label>
                        </div>
                    </div>
                    
                    <!-- Loading state (hidden by default) -->
                    <div id="collectionLoading" class="text-center py-3" style="display: none;">
                        <div class="spinner-border text-primary me-3" role="status">
                            <span class="visually-hidden">Loading...</span>
                        </div>
                        <div>
                            <h6>Collecting Flight Data...</h6>
                            <p class="text-muted mb-0">Please wait while we gather flight information from multiple sources.</p>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal" id="cancelBtn">Cancel</button>
                    <button type="submit" class="btn btn-primary" id="collectBtn">
                        <i data-feather="download" class="me-2"></i>
                        <span id="collectBtnText">Start Collection</span>
                    </button>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
// Handle data collection form submission with loading state
document.getElementById('dataCollectionForm').addEventListener('submit', function(e) {
    // Show loading state
    document.getElementById('collectionLoading').style.display = 'block';
    document.getElementById('collectBtn').disabled = true;
    document.getElementById('cancelBtn').disabled = true;
    document.getElementById('collectBtnText').innerHTML = 'Collecting...';
    
    // Update button with spinner
    const collectBtn = document.getElementById('collectBtn');
    collectBtn.innerHTML = `
        <div class="spinner-border spinner-border-sm me-2" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        Collecting Data...
    `;
});

// Load sample data on page load if no data exists
document.addEventListener('DOMContentLoaded', function() {
    const totalFlights = {{ total_flights | default(0) }};
    if (totalFlights === 0) {
        showSampleDataPrompt();
    }
    feather.replace();
});

function showSampleDataPrompt() {
    // Auto-show collection modal if no data exists
    setTimeout(() => {
        const modal = new bootstrap.Modal(document.getElementById('dataCollectionModal'));
        modal.show();
        
        // Add helpful message
        const alertDiv = document.createElement('div');
        alertDiv.className = 'alert alert-warning mt-3';
        alertDiv.innerHTML = `
            <i data-feather="info" class="me-2"></i>
            <strong>Welcome!</strong> Start by collecting flight data to see market analytics in action.
        `;
        document.querySelector('.modal-body').appendChild(alertDiv);
        feather.replace();
    }, 1000);
}

// Auto-load popular routes data
function loadPopularRoutesData() {
    const popularRoutes = [
        { origin: 'SYD', destination: 'MEL' },
        { origin: 'MEL', destination: 'SYD' },
        { origin: 'SYD', destination: 'BNE' },
        { origin: 'BNE', destination: 'SYD' },
        { origin: 'MEL', destination: 'BNE' }
    ];
    
    // This would trigger collection for each popular route
    // Implementation can be added based on requirements
}
</script>
{% endblock %}
