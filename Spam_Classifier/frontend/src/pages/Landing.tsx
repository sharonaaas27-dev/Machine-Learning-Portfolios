import { Link } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'
import { FiShield, FiZap, FiLock, FiTrendingUp, FiArrowRight, FiStar, FiUsers } from 'react-icons/fi'

export default function Landing() {
  const { user } = useAuth()

  return (
    <div className="min-h-screen gradient-bg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-24 pb-20">
        <div className="text-center mb-16 pt-16">
          <div className="inline-flex items-center justify-center p-2 bg-blue-500/10 rounded-full mb-6 border border-blue-500/20">
            <FiShield className="w-5 h-5 text-blue-400 mr-2" />
            <span className="text-blue-400 text-sm font-medium">AI-Powered Spam Detection</span>
          </div>
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            <span className="bg-gradient-to-r from-blue-400 via-purple-500 to-pink-500 bg-clip-text text-transparent">
              Smart Spam Detection
            </span>
            <br />
            <span className="text-gray-300">for Your Messages</span>
          </h1>
          <p className="text-xl text-gray-400 mb-10 max-w-3xl mx-auto leading-relaxed">
            Protect your inbox with our AI-powered spam classifier. 
            Identify spam messages with high accuracy, get detailed explanations, 
            and keep your communication clean.
          </p>
          <div className="flex justify-center space-x-4">
            {user ? (
              <Link
                to="/dashboard"
                className="inline-flex items-center px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-semibold transition-all shadow-lg shadow-blue-600/25 hover:shadow-blue-600/40"
              >
                Go to Dashboard <FiArrowRight className="ml-2" />
              </Link>
            ) : (
              <>
                <Link
                  to="/register"
                  className="inline-flex items-center px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-xl font-semibold transition-all shadow-lg shadow-blue-600/25 hover:shadow-blue-600/40"
                >
                  Get Started <FiArrowRight className="ml-2" />
                </Link>
                <Link
                  to="/login"
                  className="inline-flex items-center px-8 py-4 bg-gray-800 hover:bg-gray-700 text-gray-300 rounded-xl font-semibold transition-all border border-gray-700"
                >
                  Sign In
                </Link>
              </>
            )}
          </div>
        </div>

        <div className="grid md:grid-cols-3 gap-8 mt-20">
          <div className="glass-card p-8 text-center">
            <div className="w-14 h-14 bg-blue-500/10 rounded-xl flex items-center justify-center mx-auto mb-5 border border-blue-500/20">
              <FiZap className="w-7 h-7 text-blue-400" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-3">Real-time Detection</h3>
            <p className="text-gray-400">Instant spam prediction with millisecond response times using our optimized ML pipeline.</p>
          </div>

          <div className="glass-card p-8 text-center">
            <div className="w-14 h-14 bg-purple-500/10 rounded-xl flex items-center justify-center mx-auto mb-5 border border-purple-500/20">
              <FiLock className="w-7 h-7 text-purple-400" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-3">Explainable AI</h3>
            <p className="text-gray-400">Understand why a message was classified as spam with detailed keyword analysis and explanations.</p>
          </div>

          <div className="glass-card p-8 text-center">
            <div className="w-14 h-14 bg-green-500/10 rounded-xl flex items-center justify-center mx-auto mb-5 border border-green-500/20">
              <FiTrendingUp className="w-7 h-7 text-green-400" />
            </div>
            <h3 className="text-xl font-semibold text-white mb-3">Continuous Learning</h3>
            <p className="text-gray-400">Retrain the model with new data to improve accuracy and adapt to emerging spam patterns.</p>
          </div>
        </div>

        <div className="mt-24 text-center">
          <div className="glass-card p-10 max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-white mb-6">How It Works</h2>
            <div className="grid md:grid-cols-4 gap-6">
              {[
                { step: '1', title: 'Enter Message', desc: 'Type or paste any text message' },
                { step: '2', title: 'AI Analysis', desc: 'ML model analyzes the content' },
                { step: '3', title: 'Get Results', desc: 'Instant spam classification' },
                { step: '4', title: 'Take Action', desc: 'Filter, delete, or report spam' },
              ].map((item) => (
                <div key={item.step} className="text-center">
                  <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center mx-auto mb-3 text-white font-bold text-sm">
                    {item.step}
                  </div>
                  <h4 className="text-white font-semibold mb-1">{item.title}</h4>
                  <p className="text-gray-400 text-sm">{item.desc}</p>
                </div>
              ))}
            </div>
          </div>
        </div>

        <footer className="mt-20 text-center text-gray-500 text-sm">
          <p> SpamGuard - AI-Powered Spam Detection System</p>
        </footer>
      </div>
    </div>
  )
}
