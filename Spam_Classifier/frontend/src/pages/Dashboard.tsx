import { useEffect, useState } from 'react'
import { useHealth, useModelMetrics } from '../hooks/usePredictions'
import { FiShield, FiMessageSquare, FiAlertTriangle, FiCheckCircle, FiCpu, FiRefreshCw } from 'react-icons/fi'
import { Doughnut, Bar } from 'react-chartjs-2'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title } from 'chart.js'
import LoadingSpinner from '../components/LoadingSpinner'

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title)

export default function Dashboard() {
  const { data: health, isLoading: healthLoading } = useHealth()
  const { data: metrics, isLoading: metricsLoading } = useModelMetrics()
  const [stats, setStats] = useState({ total: 0, spam: 0, ham: 0 })

  useEffect(() => {
    import('../services/api').then((mod) =>
      mod.historyApi.getAll({ limit: 1000 }).then((res) => {
        const predictions = res.data.predictions
        setStats({
          total: predictions.length,
          spam: predictions.filter((p) => p.prediction === 'spam').length,
          ham: predictions.filter((p) => p.prediction === 'ham').length,
        })
      })
    )
  }, [])

  if (healthLoading || metricsLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16">
        <LoadingSpinner text="Loading dashboard..." />
      </div>
    )
  }

  const pieData = {
    labels: ['Spam', 'Ham'],
    datasets: [{
      data: [stats.spam || 1, stats.ham || 1],
      backgroundColor: ['#ef4444', '#22c55e'],
      borderColor: ['#dc2626', '#16a34a'],
      borderWidth: 2,
    }],
  }

  const comparisonData = metrics?.model_comparison ? {
    labels: Object.keys(metrics.model_comparison),
    datasets: [{
      label: 'Accuracy',
      data: Object.values(metrics.model_comparison).map((m) => m.accuracy),
      backgroundColor: '#3b82f6',
      borderRadius: 6,
    }],
  } : null

  const cards = [
    { label: 'Total Predictions', value: stats.total, icon: FiMessageSquare, color: 'blue' },
    { label: 'Spam Detected', value: stats.spam, icon: FiAlertTriangle, color: 'red' },
    { label: 'Ham Messages', value: stats.ham, icon: FiCheckCircle, color: 'green' },
    { label: 'Model Accuracy', value: metrics ? `${(metrics.accuracy * 100).toFixed(1)}%` : 'N/A', icon: FiCpu, color: 'purple' },
  ]

  return (
    <div className="min-h-screen pt-20 pb-10 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-white">Dashboard</h1>
          <p className="text-gray-400 mt-1">Overview of your spam detection system</p>
        </div>
        <div className="flex items-center space-x-2 text-sm">
          <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse" />
          <span className="text-gray-400">{health?.model_trained ? 'Model Active' : 'No Model'}</span>
        </div>
      </div>

      <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {cards.map((card) => (
          <div key={card.label} className="glass-card p-6">
            <div className="flex items-center justify-between mb-4">
              <card.icon className={`w-8 h-8 text-${card.color}-400`} />
            </div>
            <p className="text-3xl font-bold text-white mb-1">{card.value}</p>
            <p className="text-gray-400 text-sm">{card.label}</p>
          </div>
        ))}
      </div>

      <div className="grid md:grid-cols-2 gap-8 mb-8">
        <div className="glass-card p-6">
          <h3 className="text-lg font-semibold text-white mb-4">Prediction Distribution</h3>
          <div className="max-w-xs mx-auto">
            <Doughnut
              data={pieData}
              options={{
                plugins: { legend: { position: 'bottom', labels: { color: '#9ca3af' } } },
              }}
            />
          </div>
        </div>

        <div className="glass-card p-6">
          <h3 className="text-lg font-semibold text-white mb-4">Model Comparison</h3>
          {comparisonData ? (
            <Bar
              data={comparisonData}
              options={{
                plugins: { legend: { display: false } },
                scales: {
                  x: { ticks: { color: '#9ca3af', maxRotation: 45 } },
                  y: { ticks: { color: '#9ca3af' }, beginAtZero: true, max: 1 },
                },
              }}
            />
          ) : (
            <p className="text-gray-400 text-center py-8">No model comparison data available</p>
          )}
        </div>
      </div>

      {metrics && (
        <div className="glass-card p-6">
          <h3 className="text-lg font-semibold text-white mb-4">Model Information</h3>
          <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
            <div className="p-3 bg-gray-800/50 rounded-lg">
              <span className="text-gray-400 text-sm">Best Model</span>
              <p className="text-white font-semibold">{metrics.best_model}</p>
            </div>
            <div className="p-3 bg-gray-800/50 rounded-lg">
              <span className="text-gray-400 text-sm">Precision</span>
              <p className="text-white font-semibold">{(metrics.precision * 100).toFixed(2)}%</p>
            </div>
            <div className="p-3 bg-gray-800/50 rounded-lg">
              <span className="text-gray-400 text-sm">Recall</span>
              <p className="text-white font-semibold">{(metrics.recall * 100).toFixed(2)}%</p>
            </div>
            <div className="p-3 bg-gray-800/50 rounded-lg">
              <span className="text-gray-400 text-sm">F1 Score</span>
              <p className="text-white font-semibold">{(metrics.f1_score * 100).toFixed(2)}%</p>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
