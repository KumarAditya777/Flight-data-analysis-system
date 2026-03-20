{% extends "base.html" %}

{% block title %}How to Use - Airline Market Analytics{% endblock %}

{% block content %}
<div class="container-fluid">
    <!-- Hero Section -->
    <div class="row bg-primary text-white py-5 mb-4" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
        <div class="col-12 text-center">
            <h1 class="display-4 fw-bold">
                <i data-feather="help-circle" class="me-3"></i>
                How to Use Airline Market Analytics
            </h1>
            <p class="lead">A complete guide to understanding travel demand and market trends</p>
        </div>
    </div>

    <!-- Quick Start Guide -->
    <div class="row">
        <div class="col-lg-8 mx-auto">
            <div class="card shadow">
                <div class="card-body p-5">
                    <h2 class="card-title mb-4">
                        <i data-feather="play-circle" class="me-2 text-primary"></i>
                        Quick Start Guide
                    </h2>
                    
                    <!-- Step 1 -->
                    <div class="mb-4">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge bg-primary rounded-circle me-3 p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">1</span>
                            <h4 class="mb-0">View the Dashboard</h4>
                        </div>
                        <p class="ms-5 text-muted">Start on the main dashboard to see overview statistics of flight data, popular routes, and recent market trends.</p>
                    </div>

                    <!-- Step 2 -->
                    <div class="mb-4">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge bg-primary rounded-circle me-3 p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">2</span>
                            <h4 class="mb-0">Collect Flight Data</h4>
                        </div>
                        <p class="ms-5 text-muted">Click "Collect Flight Data" to gather new information for specific routes. Choose your origin and destination airports from the dropdown menus.</p>
                        <div class="ms-5">
                            <button class="btn btn-outline-primary btn-sm" disabled>
                                <i data-feather="download" class="me-1"></i>
                                Collect Flight Data
                            </button>
                        </div>
                    </div>

                    <!-- Step 3 -->
                    <div class="mb-4">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge bg-primary rounded-circle me-3 p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">3</span>
                            <h4 class="mb-0">Analyze Market Trends</h4>
                        </div>
                        <p class="ms-5 text-muted">Use the Analysis page to filter data by routes, dates, and airlines. View interactive charts showing price trends and market patterns.</p>
                    </div>

                    <!-- Step 4 -->
                    <div class="mb-4">
                        <div class="d-flex align-items-center mb-3">
                            <span class="badge bg-primary rounded-circle me-3 p-2" style="width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">4</span>
                            <h4 class="mb-0">Get AI Insights</h4>
                        </div>
                        <p class="ms-5 text-muted">Visit the Insights page to see AI-generated business intelligence and recommendations for hostel planning and investment decisions.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Feature Explanations -->
    <div class="row mt-5">
        <div class="col-12">
            <h2 class="text-center mb-4">
                <i data-feather="star" class="me-2 text-warning"></i>
                Key Features Explained
            </h2>
        </div>
    </div>

    <div class="row">
        <!-- Dashboard -->
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <i data-feather="home" class="mb-3 text-primary" style="width: 48px; height: 48px;"></i>
                    <h5 class="card-title">Dashboard Overview</h5>
                    <p class="card-text">See total flights analyzed, popular routes, recent data collection activity, and quick market statistics.</p>
                </div>
            </div>
        </div>

        <!-- Data Collection -->
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <i data-feather="download" class="mb-3 text-success" style="width: 48px; height: 48px;"></i>
                    <h5 class="card-title">Smart Data Collection</h5>
                    <p class="card-text">Automatically gathers flight information from multiple sources with intelligent fallback to ensure data availability.</p>
                </div>
            </div>
        </div>

        <!-- Analysis -->
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <i data-feather="bar-chart-2" class="mb-3 text-info" style="width: 48px; height: 48px;"></i>
                    <h5 class="card-title">Interactive Analysis</h5>
                    <p class="card-text">Filter and visualize flight data with charts showing price trends, route popularity, and airline market share.</p>
                </div>
            </div>
        </div>

        <!-- AI Insights -->
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <i data-feather="cpu" class="mb-3 text-warning" style="width: 48px; height: 48px;"></i>
                    <h5 class="card-title">AI-Powered Insights</h5>
                    <p class="card-text">Get intelligent market analysis and business recommendations powered by advanced AI algorithms.</p>
                </div>
            </div>
        </div>

        <!-- Export -->
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <i data-feather="share" class="mb-3 text-secondary" style="width: 48px; height: 48px;"></i>
                    <h5 class="card-title">Data Export</h5>
                    <p class="card-text">Export filtered data to CSV for further analysis in external tools like Excel or Google Sheets.</p>
                </div>
            </div>
        </div>

        <!-- Caching -->
        <div class="col-md-6 col-lg-4 mb-4">
            <div class="card h-100 shadow-sm">
                <div class="card-body text-center">
                    <i data-feather="database" class="mb-3 text-dark" style="width: 48px; height: 48px;"></i>
                    <h5 class="card-title">Smart Caching</h5>
                    <p class="card-text">Intelligent caching system reduces API calls and improves performance while maintaining data freshness.</p>
                </div>
            </div>
        </div>
    </div>

    <!-- Understanding the Data -->
    <div class="row mt-5">
        <div class="col-lg-10 mx-auto">
            <div class="card shadow">
                <div class="card-body p-5">
                    <h2 class="card-title mb-4">
                        <i data-feather="info" class="me-2 text-info"></i>
                        Understanding Your Data
                    </h2>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <h5>Flight Information Includes:</h5>
                            <ul class="list-unstyled">
                                <li><i data-feather="check-circle" class="me-2 text-success"></i>Origin and destination airports</li>
                                <li><i data-feather="check-circle" class="me-2 text-success"></i>Airline and booking class</li>
                                <li><i data-feather="check-circle" class="me-2 text-success"></i>Price and availability</li>
                                <li><i data-feather="check-circle" class="me-2 text-success"></i>Departure dates</li>
                                <li><i data-feather="check-circle" class="me-2 text-success"></i>Data collection timestamps</li>
                            </ul>
                        </div>
                        <div class="col-md-6">
                            <h5>Business Applications:</h5>
                            <ul class="list-unstyled">
                                <li><i data-feather="trending-up" class="me-2 text-primary"></i>Identify peak travel periods</li>
                                <li><i data-feather="map-pin" class="me-2 text-primary"></i>Discover popular destinations</li>
                                <li><i data-feather="dollar-sign" class="me-2 text-primary"></i>Track pricing trends</li>
                                <li><i data-feather="users" class="me-2 text-primary"></i>Understand customer demand</li>
                                <li><i data-feather="calendar" class="me-2 text-primary"></i>Plan hostel capacity</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Tips and Best Practices -->
    <div class="row mt-5">
        <div class="col-lg-10 mx-auto">
            <div class="card shadow border-warning">
                <div class="card-body p-5">
                    <h2 class="card-title mb-4 text-warning">
                        <i data-feather="lightbulb" class="me-2"></i>
                        Tips for Best Results
                    </h2>
                    
                    <div class="row">
                        <div class="col-md-6">
                            <div class="mb-3">
                                <h6><i data-feather="clock" class="me-2"></i>Data Collection Timing</h6>
                                <p class="text-muted small">Collect data at different times to capture price variations and availability changes throughout the day.</p>
                            </div>
                            <div class="mb-3">
                                <h6><i data-feather="repeat" class="me-2"></i>Regular Updates</h6>
                                <p class="text-muted small">Update data weekly to track trends and seasonal patterns in travel demand.</p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="mb-3">
                                <h6><i data-feather="filter" class="me-2"></i>Smart Filtering</h6>
                                <p class="text-muted small">Use date and route filters in analysis to focus on specific market segments relevant to your business.</p>
                            </div>
                            <div class="mb-3">
                                <h6><i data-feather="eye" class="me-2"></i>Monitor Insights</h6>
                                <p class="text-muted small">Check AI insights regularly for emerging trends and business opportunities in the travel market.</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Getting Started Button -->
    <div class="row mt-5">
        <div class="col-12 text-center">
            <a href="{{ url_for('index') }}" class="btn btn-primary btn-lg">
                <i data-feather="arrow-right" class="me-2"></i>
                Start Using the App
            </a>
        </div>
    </div>
</div>
{% endblock %}

{% block scripts %}
<script>
    // Initialize Feather icons
    feather.replace();
</script>
{% endblock %}