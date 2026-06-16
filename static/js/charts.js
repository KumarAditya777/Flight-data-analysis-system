// Chart.js configuration and initialization
let priceChart, routeChart, airlineChart, patternChart;

function initializeCharts(data) {
    try {
        // Initialize all charts with the provided data
        initializePriceChart(data.price_trends || []);
        initializeRouteChart(data.popular_routes || []);
        initializeAirlineChart(data.airline_share || []);
        initializePatternChart(data.price_trends || []);
    } catch (error) {
        console.error('Error initializing charts:', error);
        showNoDataCharts();
    }
}

function initializePriceChart(priceData) {
    const ctx = document.getElementById('priceChart');
    if (!ctx) return;

    // Group data by route for multiple lines
    const routeData = {};
    priceData.forEach(item => {
        if (!routeData[item.route]) {
            routeData[item.route] = [];
        }
        routeData[item.route].push({
            x: item.date,
            y: item.price
        });
    });

    const datasets = Object.keys(routeData).slice(0, 5).map((route, index) => {
        const colors = ['#007bff', '#28a745', '#ffc107', '#dc3545', '#6f42c1'];
        return {
            label: route,
            data: routeData[route],
            borderColor: colors[index],
            backgroundColor: colors[index] + '20',
            fill: false,
            tension: 0.1
        };
    });

    priceChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Flight Price Trends'
                },
                legend: {
                    display: true,
                    position: 'bottom'
                }
            },
            scales: {
                x: {
                    type: 'time',
                    time: {
                        parser: 'YYYY-MM-DD',
                        tooltipFormat: 'MMM DD, YYYY',
                        displayFormats: {
                            day: 'MMM DD'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price (AUD)'
                    },
                    ticks: {
                        callback: function(value) {
                            return '$' + value.toFixed(0);
                        }
                    }
                }
            },
            interaction: {
                intersect: false,
                mode: 'index'
            }
        }
    });
}

function initializeRouteChart(routeData) {
    const ctx = document.getElementById('routeChart');
    if (!ctx) return;

    const labels = routeData.slice(0, 10).map(item => item.route);
    const data = routeData.slice(0, 10).map(item => item.count);
    const colors = generateColors(labels.length);

    routeChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: labels,
            datasets: [{
                data: data,
                backgroundColor: colors,
                borderWidth: 2,
                borderColor: '#fff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Most Popular Routes'
                },
                legend: {
                    display: true,
                    position: 'bottom'
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            const label = context.label || '';
                            const value = context.parsed;
                            const total = context.dataset.data.reduce((a, b) => a + b, 0);
                            const percentage = ((value / total) * 100).toFixed(1);
                            return `${label}: ${value} flights (${percentage}%)`;
                        }
                    }
                }
            }
        }
    });
}

function initializeAirlineChart(airlineData) {
    const ctx = document.getElementById('airlineChart');
    if (!ctx) return;

    const labels = airlineData.slice(0, 8).map(item => item.airline);
    const data = airlineData.slice(0, 8).map(item => item.count);
    const colors = generateColors(labels.length);

    airlineChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Flights',
                data: data,
                backgroundColor: colors,
                borderColor: colors.map(color => color.replace('0.8', '1')),
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Airline Market Share'
                },
                legend: {
                    display: false
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Flights'
                    }
                },
                x: {
                    title: {
                        display: true,
                        text: 'Airlines'
                    }
                }
            }
        }
    });
}

function initializePatternChart(priceData) {
    const ctx = document.getElementById('patternChart');
    if (!ctx) return;

    // Group data by day of week
    const dayData = Array(7).fill(0);
    const dayLabels = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    
    priceData.forEach(item => {
        const date = new Date(item.date);
        const dayOfWeek = date.getDay();
        dayData[dayOfWeek]++;
    });

    patternChart = new Chart(ctx, {
        type: 'radar',
        data: {
            labels: dayLabels,
            datasets: [{
                label: 'Booking Frequency',
                data: dayData,
                backgroundColor: 'rgba(54, 162, 235, 0.2)',
                borderColor: 'rgba(54, 162, 235, 1)',
                borderWidth: 2,
                pointBackgroundColor: 'rgba(54, 162, 235, 1)',
                pointBorderColor: '#fff',
                pointHoverBackgroundColor: '#fff',
                pointHoverBorderColor: 'rgba(54, 162, 235, 1)'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'Booking Patterns by Day'
                }
            },
            scales: {
                r: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Number of Bookings'
                    }
                }
            }
        }
    });
}

function showNoDataCharts() {
    // Show placeholder charts when no data is available
    const chartIds = ['priceChart', 'routeChart', 'airlineChart', 'patternChart'];
    
    chartIds.forEach(chartId => {
        const ctx = document.getElementById(chartId);
        if (ctx) {
            new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: ['No Data'],
                    datasets: [{
                        label: 'No Data Available',
                        data: [0],
                        backgroundColor: 'rgba(108, 117, 125, 0.3)',
                        borderColor: 'rgba(108, 117, 125, 1)',
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        title: {
                            display: true,
                            text: 'No Data Available'
                        },
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            max: 1
                        }
                    }
                }
            });
        }
    });
}

function generateColors(count) {
    const baseColors = [
        'rgba(255, 99, 132, 0.8)',
        'rgba(54, 162, 235, 0.8)',
        'rgba(255, 205, 86, 0.8)',
        'rgba(75, 192, 192, 0.8)',
        'rgba(153, 102, 255, 0.8)',
        'rgba(255, 159, 64, 0.8)',
        'rgba(199, 199, 199, 0.8)',
        'rgba(83, 102, 255, 0.8)'
    ];
    
    const colors = [];
    for (let i = 0; i < count; i++) {
        colors.push(baseColors[i % baseColors.length]);
    }
    return colors;
}

// Utility function to update charts with new data
function updateCharts(newData) {
    try {
        if (priceChart) {
            priceChart.destroy();
        }
        if (routeChart) {
            routeChart.destroy();
        }
        if (airlineChart) {
            airlineChart.destroy();
        }
        if (patternChart) {
            patternChart.destroy();
        }
        
        initializeCharts(newData);
    } catch (error) {
        console.error('Error updating charts:', error);
    }
}

// Export functions for external use
window.chartUtils = {
    initializeCharts,
    updateCharts,
    showNoDataCharts
};
