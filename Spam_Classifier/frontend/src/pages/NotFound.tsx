import { Link } from 'react-router-dom'
import { FiHome } from 'react-icons/fi'

export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center px-4">
      <div className="text-center">
        <h1 className="text-8xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent mb-4">
          404
        </h1>
        <p className="text-2xl text-gray-300 mb-2">Page Not Found</p>
        <p className="text-gray-500 mb-8">The page you're looking for doesn't exist.</p>
        <Link
          to="/"
          className="inline-flex items-center px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white rounded-lg font-medium transition-all"
        >
          <FiHome className="mr-2" /> Go Home
        </Link>
      </div>
    </div>
  )
}
