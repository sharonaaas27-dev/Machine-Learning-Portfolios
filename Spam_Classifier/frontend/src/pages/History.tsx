import { useState } from 'react'
import { useHistory, useDeletePrediction } from '../hooks/usePredictions'
import LoadingSpinner from '../components/LoadingSpinner'
import { FiSearch, FiTrash2, FiAlertTriangle, FiCheckCircle, FiDownload, FiChevronLeft, FiChevronRight, FiClock } from 'react-icons/fi'
import toast from 'react-hot-toast'

export default function History() {
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(1)
  const { data, isLoading } = useHistory({ search, page, limit: 20 })
  const deleteMutation = useDeletePrediction()

  const handleDelete = async (id: number) => {
    if (window.confirm('Delete this prediction?')) {
      await deleteMutation.mutateAsync(id)
    }
  }

  const handleExport = async () => {
    try {
      const mod = await import('../services/api')
      const res = await mod.historyApi.export()
      const blob = new Blob([JSON.stringify(res.data.data, null, 2)], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = 'predictions-history.json'
      a.click()
      URL.revokeObjectURL(url)
      toast.success('History exported!')
    } catch {
      toast.error('Export failed')
    }
  }

  return (
    <div className="min-h-screen pt-20 pb-10 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto">
      <div className="flex flex-col sm:flex-row justify-between items-start sm:items-center mb-8 gap-4">
        <div>
          <h1 className="text-3xl font-bold text-white">Prediction History</h1>
          <p className="text-gray-400 mt-1">View and manage your past predictions</p>
        </div>
        <button onClick={handleExport} className="flex items-center px-4 py-2 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-lg transition-all border border-gray-700">
          <FiDownload className="mr-1.5" /> Export
        </button>
      </div>

      <div className="glass-card p-4 mb-6">
        <div className="relative">
          <FiSearch className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-500" />
          <input
            type="text"
            value={search}
            onChange={(e) => { setSearch(e.target.value); setPage(1) }}
            placeholder="Search messages..."
            className="w-full pl-10 pr-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-blue-500 transition-all"
          />
        </div>
      </div>

      {isLoading ? (
        <div className="flex justify-center py-20">
          <LoadingSpinner text="Loading history..." />
        </div>
      ) : data && data.predictions.length > 0 ? (
        <>
          <div className="space-y-4">
            {data.predictions.map((pred) => (
              <div key={pred.id} className="glass-card p-5">
                <div className="flex items-start justify-between">
                  <div className="flex-1 mr-4">
                    <div className="flex items-center space-x-2 mb-2">
                      {pred.prediction === 'spam' ? (
                        <span className="flex items-center text-red-400 text-sm font-medium">
                          <FiAlertTriangle className="w-4 h-4 mr-1" /> Spam
                        </span>
                      ) : (
                        <span className="flex items-center text-green-400 text-sm font-medium">
                          <FiCheckCircle className="w-4 h-4 mr-1" /> Ham
                        </span>
                      )}
                      <span className="text-gray-500 text-sm">{(pred.confidence * 100).toFixed(1)}% confidence</span>
                      <span className="text-gray-600 text-sm flex items-center"><FiClock className="mr-1" />{new Date(pred.created_at).toLocaleString()}</span>
                    </div>
                    <p className="text-gray-300 line-clamp-2">{pred.message}</p>
                    {pred.top_keywords && (
                      <p className="text-gray-500 text-sm mt-1">Keywords: {pred.top_keywords}</p>
                    )}
                  </div>
                  <button
                    onClick={() => handleDelete(pred.id)}
                    className="p-2 text-gray-500 hover:text-red-400 hover:bg-red-500/10 rounded-lg transition-all"
                  >
                    <FiTrash2 className="w-4 h-4" />
                  </button>
                </div>
              </div>
            ))}
          </div>

          <div className="flex justify-between items-center mt-6 text-sm">
            <span className="text-gray-400">
              Showing {((page - 1) * 20) + 1}-{Math.min(page * 20, data.total)} of {data.total}
            </span>
            <div className="flex space-x-2">
              <button
                onClick={() => setPage(Math.max(1, page - 1))}
                disabled={page === 1}
                className="flex items-center px-3 py-2 bg-gray-800 hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed text-gray-300 rounded-lg transition-all"
              >
                <FiChevronLeft className="mr-1" /> Previous
              </button>
              <button
                onClick={() => setPage(page + 1)}
                disabled={page * 20 >= data.total}
                className="flex items-center px-3 py-2 bg-gray-800 hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed text-gray-300 rounded-lg transition-all"
              >
                Next <FiChevronRight className="ml-1" />
              </button>
            </div>
          </div>
        </>
      ) : (
        <div className="glass-card p-12 text-center">
          <FiSearch className="w-12 h-12 text-gray-600 mx-auto mb-4" />
          <p className="text-gray-500">{search ? 'No predictions match your search' : 'No predictions yet. Try checking some messages!'}</p>
        </div>
      )}
    </div>
  )
}
