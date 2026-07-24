import { useModelMetrics, useRetrain } from '../hooks/usePredictions'
import LoadingSpinner from '../components/LoadingSpinner'
import { FiRefreshCw, FiBarChart2, FiCpu, FiDatabase } from 'react-icons/fi'
import { Bar, Doughnut } from 'react-chartjs-2'
import { Chart as ChartJS, ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title } from 'chart.js'

ChartJS.register(ArcElement, Tooltip, Legend, CategoryScale, LinearScale, BarElement, Title)

export default function Metrics() {
  const { data: metrics, isLoading } = useModelMetrics()
  const retrainMutation = useRetrain()

  if (isLoading) {
    return (
      <div className="min-h-screen flex items-center justify-center pt-16">
        <LoadingSpinner text="Loading metrics..." />
      </div>
    )
  }

  if (!metrics) {
    return (
      <div className="min-h-screen pt-20 pb-10 px-4 max-w-4xl mx-auto text-center">
        <div className="glass-card p-12">
          <FiBarChart2 className="w-16 h-16 text-gray-600 mx-auto mb-4" />
          <h2 className="text-2xl font-bold text-white mb-2">No Metrics Available</h2>
          <p className="text-gray-400 mb-6">Train the model first to see performance metrics.</p>
          <button
            onClick={() => retrainMutation.mutate()}
            disabled={retrainMutation.isPending}
            className="inline-flex items-center px-6 py-3 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-800 text-white rounded-lg font-medium transition-all"
          >
            <FiRefreshCw className={`mr-2 ${retrainMutation.isPending ? 'animate-spin' : ''}`} />
            {retrainMutation.isPending ? 'Training...' : 'Train Model'}
          </button>
        </div>
      </div>
    )
  }

  const confusionMatrix = metrics.confusion_matrix
  const cmData = {
    labels: ['Actual Ham', 'Actual Spam'],
    datasets: [
      {
        label: 'Predicted Ham',
        data: [confusionMatrix[0][0], confusionMatrix[1][0]],
        backgroundColor: '#22c55e',
      },
      {
        label: 'Predicted Spam',
        data: [confusionMatrix[0][1], confusionMatrix[1][1]],
        backgroundColor: '#ef4444',
      },
    ],
  }

  const comparisonLabels = Object.keys(metrics.model_comparison)
  const comparisonAcc = Object.values(metrics.model_comparison).map((m) => m.accuracy)
  const comparisonF1 = Object.values(metrics.model_comparison).map((m) => m.f1_score)

  const comparisonData = {
    labels: comparisonLabels,
    datasets: [
      { label: 'Accuracy', data: comparisonAcc, backgroundColor: '#3b82f6', borderRadius: 4 },
      { label: 'F1 Score', data: comparisonF1, backgroundColor: '#8b5cf6', borderRadius: 4 },
    ],
  }

  return (
    <div className="min-h-screen pt-20 pb-10 px-4 sm:px-6 lg:px-8 max-w-7xl mx-auto">
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-bold text-white">Model Metrics</h1>
          <p className="text-gray-400 mt-1">Performance evaluation of the spam classifier</p>
        </div>
        <button
          onClick={() => retrainMutation.mutate()}
          disabled={retrainMutation.isPending}
          className="flex items-center px-5 py-2.5 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-800 text-white rounded-lg font-medium transition-all shadow-lg shadow-blue-600/25"
        >
          <FiRefreshCw className={`mr-2 ${retrainMutation.isPending ? 'animate-spin' : ''}`} />
          {retrainMutation.isPending ? 'Retraining...' : 'Retrain Model'}
        </button>
      </div>

      <div className="grid sm:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        {[
          { label: 'Accuracy', value: `${(metrics.accuracy * 100).toFixed(2)}%`, color: 'text-blue-400', icon: FiCpu },
          { label: 'Precision', value: `${(metrics.precision * 100).toFixed(2)}%`, color: 'text-green-400', icon: FiBarChart2 },
          { label: 'Recall', value: `${(metrics.recall * 100).toFixed(2)}%`, color: 'text-purple-400', icon: FiBarChart2 },
          { label: 'F1 Score', value: `${(metrics.f1_score * 100).toFixed(2)}%`, color: 'text-yellow-400', icon: FiBarChart2 },
        ].map((stat) => (
          <div key={stat.label} className="glass-card p-6">
            <div className="flex items-center justify-between mb-3">
              <stat.icon className={`w-6 h-6 ${stat.color}`} />
              <span className="text-3xl font-bold text-white">{stat.value}</span>
            </div>
            <p className="text-gray-400 text-sm">{stat.label}</p>
          </div>
        ))}
      </div>

      {metrics.roc_auc && (
        <div className="grid sm:grid-cols-2 gap-6 mb-8">
          <div className="glass-card p-6">
            <span className="text-gray-400 text-sm">ROC-AUC Score</span>
            <p className="text-3xl font-bold text-white">{(metrics.roc_auc * 100).toFixed(2)}%</p>
          </div>
          <div className="glass-card p-6">
            <span className="text-gray-400 text-sm">Cross-Validation (Mean ± Std)</span>
            <p className="text-3xl font-bold text-white">
              {(metrics.cross_val_mean * 100).toFixed(2)}% <span className="text-gray-500 text-lg">± {(metrics.cross_val_std * 100).toFixed(2)}%</span>
            </p>
          </div>
        </div>
      )}

      <div className="grid md:grid-cols-2 gap-8 mb-8">
        <div className="glass-card p-6">
          <h3 className="text-lg font-semibold text-white mb-4">Confusion Matrix</h3>
          <Bar
            data={cmData}
            options={{
              plugins: { legend: { position: 'bottom', labels: { color: '#9ca3af' } } },
              scales: {
                x: { ticks: { color: '#9ca3af' } },
                y: { ticks: { color: '#9ca3af' }, beginAtZero: true },
              },
            }}
          />
        </div>

        <div className="glass-card p-6">
          <h3 className="text-lg font-semibold text-white mb-4">Model Comparison</h3>
          <Bar
            data={comparisonData}
            options={{
              plugins: { legend: { position: 'bottom', labels: { color: '#9ca3af' } } },
              scales: {
                x: { ticks: { color: '#9ca3af', maxRotation: 45 } },
                y: { ticks: { color: '#9ca3af' }, beginAtZero: true, max: 1 },
              },
            }}
          />
        </div>
      </div>

      <div className="glass-card p-6">
        <h3 className="text-lg font-semibold text-white mb-4">Training Details</h3>
        <div className="grid sm:grid-cols-3 gap-4">
          <div className="p-3 bg-gray-800/50 rounded-lg">
            <span className="text-gray-400 text-sm">Best Model</span>
            <p className="text-white font-semibold">{metrics.best_model}</p>
          </div>
          <div className="p-3 bg-gray-800/50 rounded-lg">
            <span className="text-gray-400 text-sm">Training Samples</span>
            <p className="text-white font-semibold">{metrics.training_samples.toLocaleString()}</p>
          </div>
          <div className="p-3 bg-gray-800/50 rounded-lg">
            <span className="text-gray-400 text-sm">Features</span>
            <p className="text-white font-semibold">{metrics.feature_count.toLocaleString()}</p>
          </div>
        </div>
      </div>
    </div>
  )
}
