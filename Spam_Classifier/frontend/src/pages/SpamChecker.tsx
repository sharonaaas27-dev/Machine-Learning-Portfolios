import { useState } from 'react'
import { usePredict } from '../hooks/usePredictions'
import ConfidenceMeter from '../components/ConfidenceMeter'
import LoadingSpinner from '../components/LoadingSpinner'
import { FiSend, FiTrash2, FiInfo, FiAlertTriangle, FiCheckCircle, FiClock } from 'react-icons/fi'
import type { PredictResponse } from '../types'

export default function SpamChecker() {
  const [message, setMessage] = useState('')
  const [result, setResult] = useState<PredictResponse | null>(null)
  const predictMutation = usePredict()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!message.trim()) return
    try {
      const res = await predictMutation.mutateAsync({ message })
      setResult(res.data)
    } catch (err) {
      console.error(err)
    }
  }

  const handleClear = () => {
    setMessage('')
    setResult(null)
  }

  return (
    <div className="min-h-screen pt-20 pb-10 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-white">Spam Checker</h1>
        <p className="text-gray-400 mt-1">Enter a message to check if it's spam or not</p>
      </div>

      <div className="glass-card p-6 mb-8">
        <form onSubmit={handleSubmit}>
          <label className="block text-sm font-medium text-gray-300 mb-2">Message</label>
          <textarea
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            rows={5}
            className="w-full px-4 py-3 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-500 focus:border-blue-500 focus:ring-1 focus:ring-blue-500 transition-all resize-none"
            placeholder="Type or paste a message here..."
          />
          <div className="flex justify-between items-center mt-4">
            <span className="text-gray-500 text-sm">{message.length} characters</span>
            <div className="flex space-x-3">
              <button
                type="button"
                onClick={handleClear}
                className="flex items-center px-4 py-2 text-gray-400 hover:text-white hover:bg-gray-800 rounded-lg transition-all"
              >
                <FiTrash2 className="mr-1.5" /> Clear
              </button>
              <button
                type="submit"
                disabled={!message.trim() || predictMutation.isPending}
                className="flex items-center px-6 py-2 bg-blue-600 hover:bg-blue-700 disabled:bg-blue-800 disabled:cursor-not-allowed text-white rounded-lg font-medium transition-all shadow-lg shadow-blue-600/25"
              >
                {predictMutation.isPending ? <LoadingSpinner size="sm" /> : <><FiSend className="mr-1.5" /> Check</>}
              </button>
            </div>
          </div>
        </form>
      </div>

      {predictMutation.isPending && (
        <div className="glass-card p-8 flex justify-center">
          <LoadingSpinner text="Analyzing message..." />
        </div>
      )}

      {result && !predictMutation.isPending && (
        <div className="space-y-6">
          <div className={`glass-card p-6 border-l-4 ${result.prediction === 'spam' ? 'border-red-500' : 'border-green-500'}`}>
            <div className="flex items-center space-x-3 mb-4">
              {result.prediction === 'spam' ? (
                <div className="w-12 h-12 rounded-full spam-gradient flex items-center justify-center">
                  <FiAlertTriangle className="w-6 h-6 text-white" />
                </div>
              ) : (
                <div className="w-12 h-12 rounded-full ham-gradient flex items-center justify-center">
                  <FiCheckCircle className="w-6 h-6 text-white" />
                </div>
              )}
              <div>
                <h2 className={`text-xl font-bold ${result.prediction === 'spam' ? 'text-red-400' : 'text-green-400'}`}>
                  {result.prediction === 'spam' ? 'Spam Detected!' : 'Message is Safe'}
                </h2>
                <p className="text-gray-400 text-sm">Processed in {(result.processing_time * 1000).toFixed(0)}ms</p>
              </div>
              <div className="ml-auto flex items-center text-gray-400 text-sm">
                <FiClock className="mr-1" />
                {(result.processing_time * 1000).toFixed(0)}ms
              </div>
            </div>

            <ConfidenceMeter confidence={result.confidence} prediction={result.prediction} />

            <div className="grid sm:grid-cols-2 gap-4 mt-6">
              <div className="p-3 bg-gray-800/50 rounded-lg">
                <span className="text-gray-400 text-sm">Spam Probability</span>
                <p className="text-red-400 font-bold">{(result.spam_probability * 100).toFixed(2)}%</p>
              </div>
              <div className="p-3 bg-gray-800/50 rounded-lg">
                <span className="text-gray-400 text-sm">Ham Probability</span>
                <p className="text-green-400 font-bold">{(result.ham_probability * 100).toFixed(2)}%</p>
              </div>
            </div>
          </div>

          <div className="glass-card p-6">
            <div className="flex items-center space-x-2 mb-4">
              <FiInfo className="w-5 h-5 text-blue-400" />
              <h3 className="text-lg font-semibold text-white">Why this classification?</h3>
            </div>
            <p className="text-gray-300 mb-4">{result.explanation}</p>
            {result.top_keywords.length > 0 && (
              <div>
                <p className="text-sm text-gray-400 mb-2">Top contributing words:</p>
                <div className="flex flex-wrap gap-2">
                  {result.top_keywords.map((word, i) => (
                    <span key={i} className="px-3 py-1 bg-gray-800 text-gray-300 rounded-full text-sm border border-gray-700">
                      {word}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      )}

      {!result && !predictMutation.isPending && (
        <div className="glass-card p-12 text-center">
          <FiSend className="w-12 h-12 text-gray-600 mx-auto mb-4" />
          <p className="text-gray-500">Enter a message above and click Check to analyze it</p>
        </div>
      )}
    </div>
  )
}
