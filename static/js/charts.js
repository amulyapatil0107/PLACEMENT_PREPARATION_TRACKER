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
