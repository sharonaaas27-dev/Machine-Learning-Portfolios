import { Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import ProtectedRoute from './components/ProtectedRoute'
import Landing from './pages/Landing'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import SpamChecker from './pages/SpamChecker'
import History from './pages/History'
import Metrics from './pages/Metrics'
import Profile from './pages/Profile'
import NotFound from './pages/NotFound'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-900">
      <Navbar />
      <Routes>
        <Route path="/" element={<Landing />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/dashboard"
          element={<ProtectedRoute><Dashboard /></ProtectedRoute>}
        />
        <Route
          path="/check"
          element={<ProtectedRoute><SpamChecker /></ProtectedRoute>}
        />
        <Route
          path="/history"
          element={<ProtectedRoute><History /></ProtectedRoute>}
        />
        <Route
          path="/metrics"
          element={<ProtectedRoute><Metrics /></ProtectedRoute>}
        />
        <Route
          path="/profile"
          element={<ProtectedRoute><Profile /></ProtectedRoute>}
        />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </div>
  )
}
