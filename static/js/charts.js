document.addEventListener('DOMContentLoaded', () => {
    const analyticsContainer = document.getElementById('analytics-charts-container');
    if (!analyticsContainer) return;

    fetch('/api/analytics-data')
        .then(response => response.json())
        .then(data => {
            renderTopicChart(data.topics);
            renderDifficultyChart(data.difficulties);
            renderMonthlyChart(data.monthly);
            renderContestChart(data.contests);
            renderGoalChart(data.goals);
        })
        .catch(err => console.error('Error fetching analytics data:', err));
});

function renderTopicChart(data) {
    const ctx = document.getElementById('topicChart').getContext('2d');
    const labels = Object.keys(data);
    const values = Object.values(data);
    
    if (labels.length === 0) {
        document.getElementById('topicChart').parentElement.innerHTML += '<div class="no-data" style="color:#94a3b8;margin-top:20px;">No solving history yet</div>';
        return;
    }

    new Chart(ctx, {
        type: 'polarArea',
        data: {
            labels: labels,
            datasets: [{
                data: values,
                backgroundColor: [
                    'rgba(99, 102, 241, 0.6)',
                    'rgba(6, 182, 212, 0.6)',
                    'rgba(245, 158, 11, 0.6)',
                    'rgba(16, 185, 129, 0.6)',
                    'rgba(244, 63, 94, 0.6)',
                    'rgba(168, 85, 247, 0.6)'
                ],
                borderColor: 'rgba(255, 255, 255, 0.1)',
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                r: {
                    grid: { color: 'rgba(255, 255, 255, 0.05)' },
                    angleLines: { color: 'rgba(255, 255, 255, 0.05)' },
                    pointLabels: { color: '#94a3b8' }
                }
            },
            plugins: {
                legend: { position: 'bottom', labels: { color: '#94a3b8' } }
            }
        }
    });
