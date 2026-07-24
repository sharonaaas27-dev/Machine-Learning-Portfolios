import { Link, useLocation, useNavigate } from 'react-router-dom'
import { useAuth } from '../hooks/useAuth'
import { FiShield, FiHome, FiSearch, FiClock, FiBarChart2, FiUser, FiLogOut, FiSun, FiMoon } from 'react-icons/fi'
import { useState, useEffect } from 'react'

export default function Navbar() {
  const { user, logout } = useAuth()
  const location = useLocation()
  const navigate = useNavigate()
  const [darkMode, setDarkMode] = useState(true)

  useEffect(() => {
    document.documentElement.classList.toggle('dark', darkMode)
  }, [darkMode])

  const isActive = (path: string) => location.pathname === path

  const navLinks = [
    { path: '/dashboard', label: 'Dashboard', icon: FiHome },
    { path: '/check', label: 'Check', icon: FiSearch },
    { path: '/history', label: 'History', icon: FiClock },
    { path: '/metrics', label: 'Metrics', icon: FiBarChart2 },
    { path: '/profile', label: 'Profile', icon: FiUser },
  ]

  const handleLogout = () => {
    logout()
    navigate('/')
  }

  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-gray-900/80 backdrop-blur-xl border-b border-gray-800">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <Link to="/" className="flex items-center space-x-2">
            <FiShield className="w-6 h-6 text-blue-500" />
            <span className="text-xl font-bold bg-gradient-to-r from-blue-400 to-purple-500 bg-clip-text text-transparent">
              SpamGuard
            </span>
          </Link>

          {user && (
            <div className="hidden md:flex items-center space-x-1">
              {navLinks.map((link) => (
                <Link
                  key={link.path}
                  to={link.path}
                  className={`flex items-center px-3 py-2 rounded-lg text-sm font-medium transition-all ${
                    isActive(link.path)
                      ? 'bg-blue-600/20 text-blue-400'
                      : 'text-gray-400 hover:text-white hover:bg-gray-800'
                  }`}
                >
                  <link.icon className="w-4 h-4 mr-1.5" />
                  {link.label}
                </Link>
              ))}
            </div>
          )}

          <div className="flex items-center space-x-3">
            <button
              onClick={() => setDarkMode(!darkMode)}
              className="p-2 rounded-lg text-gray-400 hover:text-white hover:bg-gray-800 transition-all"
            >
              {darkMode ? <FiSun className="w-4 h-4" /> : <FiMoon className="w-4 h-4" />}
            </button>
            {user && (
              <button
                onClick={handleLogout}
                className="flex items-center px-3 py-2 rounded-lg text-sm font-medium text-gray-400 hover:text-red-400 hover:bg-gray-800 transition-all"
              >
                <FiLogOut className="w-4 h-4 mr-1.5" />
                <span className="hidden sm:inline">Logout</span>
              </button>
            )}
          </div>
        </div>
      </div>

      {user && (
        <div className="md:hidden border-t border-gray-800">
          <div className="flex justify-around py-2 px-2">
            {navLinks.map((link) => (
              <Link
                key={link.path}
                to={link.path}
                className={`flex flex-col items-center px-2 py-1 rounded-lg text-xs font-medium transition-all ${
                  isActive(link.path)
                    ? 'text-blue-400'
                    : 'text-gray-500 hover:text-gray-300'
                }`}
              >
                <link.icon className="w-5 h-5 mb-0.5" />
                {link.label}
              </Link>
            ))}
          </div>
        </div>
      )}
    </nav>
  )
}
