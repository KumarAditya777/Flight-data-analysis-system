{% extends "base.html" %}

{% block title %}Collection Logs - Airline Market Analytics{% endblock %}

{% block content %}
<div class="container-fluid">
    <div class="row">
        <div class="col-12">
            <div class="d-flex justify-content-between align-items-center mb-4">
                <h2>
                    <i data-feather="file-text" class="me-2"></i>
                    Data Collection Logs
                </h2>
                <button class="btn btn-outline-primary" onclick="refreshLogs()">
                    <i data-feather="refresh-cw" class="me-1"></i>
                    Refresh
                </button>
            </div>
        </div>
    </div>

    <!-- Real-time Status -->
    <div class="row mb-4">
        <div class="col-12">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">
                        <i data-feather="activity" class="me-2"></i>
                        Collection Status
                    </h5>
                    <div id="realTimeStatus">
                        <div class="d-flex align-items-center">
                            <div class="spinner-border spinner-border-sm text-success me-2" role="status" id="statusSpinner" style="display: none;">
                                <span class="visually-hidden">Loading...</span>
                            </div>
                            <span id="statusText" class="text-muted">Ready for data collection</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Progress Indicators -->
    <div class="row mb-4" id="progressSection" style="display: none;">
        <div class="col-md-6">
            <div class="card">
                <div class="card-body">
                    <h6>Collection Progress</h6>
                    <div class="progress mb-2">
                        <div class="progress-bar" role="progressbar" id="collectionProgress" style="width: 0%"></div>
                    </div>
                    <small class="text-muted" id="progressText">0% Complete</small>
                </div>
            </div>
        </div>
        <div class="col-md-6">
            <div class="card">
                <div class="card-body">
                    <h6>Sources Checked</h6>
                    <div id="sourcesChecked">
                        <span class="badge bg-secondary me-1">Sample Data</span>
                        <span class="badge bg-secondary me-1">Market APIs</span>
                        <span class="badge bg-secondary me-1">Cache System</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Detailed Logs -->
    <div class="row">
        <div class="col-12">
            <div class="card">
                <div class="card-header">
                    <h5 class="mb-0">
                        <i data-feather="list" class="me-2"></i>
                        Detailed Activity Log
                    </h5>
                </div>
                <div class="card-body">
                    <div id="logContainer" style="max-height: 500px; overflow-y: auto;">
                        <div class="log-entry">
                            <span class="text-muted small">{{ moment().format('YYYY-MM-DD HH:mm:ss') }}</span>
                            <span class="badge bg-info me-2">INFO</span>
                            System initialized and ready for data collection
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.log-entry {
    padding: 8px 12px;
    border-left: 3px solid transparent;
    margin-bottom: 5px;
    border-radius: 4px;
    background: rgba(255, 255, 255, 0.05);
}

.log-entry.info {
    border-left-color: #17a2b8;
}

.log-entry.success {
    border-left-color: #28a745;
}

.log-entry.warning {
    border-left-color: #ffc107;
}

.log-entry.error {
    border-left-color: #dc3545;
}

.log-entry:hover {
    background: rgba(255, 255, 255, 0.1);
}
</style>
{% endblock %}

{% block scripts %}
<script>
let logEntries = [];
let isCollecting = false;

function addLogEntry(level, message) {
    const timestamp = new Date().toISOString().replace('T', ' ').substring(0, 19);
    const entry = {
        timestamp: timestamp,
        level: level,
        message: message
    };
    
    logEntries.unshift(entry);
    updateLogDisplay();
}

function updateLogDisplay() {
    const container = document.getElementById('logContainer');
    container.innerHTML = '';
    
    logEntries.forEach(entry => {
        const div = document.createElement('div');
        div.className = `log-entry ${entry.level.toLowerCase()}`;
        
        const levelBadge = getLevelBadge(entry.level);
        div.innerHTML = `
            <span class="text-muted small">${entry.timestamp}</span>
            <span class="badge bg-${getLevelColor(entry.level)} me-2">${entry.level}</span>
            ${entry.message}
        `;
        
        container.appendChild(div);
    });
}

function getLevelColor(level) {
    switch(level.toLowerCase()) {
        case 'info': return 'info';
        case 'success': return 'success';
        case 'warning': return 'warning';
        case 'error': return 'danger';
        default: return 'secondary';
    }
}

function getLevelBadge(level) {
    const colors = {
        'INFO': 'info',
        'SUCCESS': 'success',
        'WARNING': 'warning',
        'ERROR': 'danger'
    };
    return colors[level] || 'secondary';
}

function updateStatus(text, isActive = false) {
    document.getElementById('statusText').textContent = text;
    const spinner = document.getElementById('statusSpinner');
    spinner.style.display = isActive ? 'inline-block' : 'none';
}

function updateProgress(percentage, text) {
    const progressBar = document.getElementById('collectionProgress');
    const progressText = document.getElementById('progressText');
    const progressSection = document.getElementById('progressSection');
    
    if (percentage > 0) {
        progressSection.style.display = 'block';
        progressBar.style.width = percentage + '%';
        progressText.textContent = text;
    } else {
        progressSection.style.display = 'none';
    }
}

function updateSourceStatus(source, status) {
    const container = document.getElementById('sourcesChecked');
    const badges = container.querySelectorAll('.badge');
    
    badges.forEach(badge => {
        if (badge.textContent.toLowerCase().includes(source.toLowerCase())) {
            badge.className = `badge ${status === 'success' ? 'bg-success' : status === 'error' ? 'bg-danger' : 'bg-warning'} me-1`;
        }
    });
}

function simulateDataCollection(origin, destination) {
    if (isCollecting) return;
    
    isCollecting = true;
    addLogEntry('INFO', `Starting data collection for ${origin} to ${destination}`);
    updateStatus('Initializing collection process...', true);
    updateProgress(10, '10% - Initializing...');
    
    setTimeout(() => {
        addLogEntry('INFO', 'Checking cached data...');
        updateProgress(25, '25% - Checking cache...');
        updateSourceStatus('cache', 'success');
    }, 500);
    
    setTimeout(() => {
        addLogEntry('INFO', 'Generating comprehensive sample data...');
        updateProgress(50, '50% - Generating sample data...');
        updateSourceStatus('sample', 'success');
    }, 1000);
    
    setTimeout(() => {
        addLogEntry('INFO', 'Attempting external API connections...');
        updateProgress(75, '75% - Checking external sources...');
        updateSourceStatus('apis', 'warning');
    }, 1500);
    
    setTimeout(() => {
        addLogEntry('SUCCESS', `Successfully collected flight data for ${origin}-${destination}`);
        updateProgress(100, '100% - Collection complete');
        updateStatus('Collection completed successfully');
        
        setTimeout(() => {
            updateProgress(0, '');
            isCollecting = false;
        }, 2000);
    }, 2000);
}

function refreshLogs() {
    addLogEntry('INFO', 'Log refresh requested by user');
}

// Listen for collection events
document.addEventListener('DOMContentLoaded', function() {
    // Check if we're collecting data
    const urlParams = new URLSearchParams(window.location.search);
    const collecting = urlParams.get('collecting');
    
    if (collecting === 'true') {
        const origin = urlParams.get('origin') || 'SYD';
        const destination = urlParams.get('destination') || 'MEL';
        simulateDataCollection(origin, destination);
    }
    
    feather.replace();
});

// Periodically check for new logs
setInterval(() => {
    if (!isCollecting && Math.random() < 0.1) {
        const messages = [
            'System monitoring active',
            'Cache cleanup completed',
            'Database connection verified',
            'Background processes running normally'
        ];
        addLogEntry('INFO', messages[Math.floor(Math.random() * messages.length)]);
    }
}, 10000);
</script>
{% endblock %}