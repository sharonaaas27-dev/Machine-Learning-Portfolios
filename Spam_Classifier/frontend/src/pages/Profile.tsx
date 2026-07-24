import { useAuth } from '../hooks/useAuth'
import { FiUser, FiMail, FiCalendar, FiShield } from 'react-icons/fi'

export default function Profile() {
  const { user } = useAuth()

  if (!user) return null

  const infoCards = [
    { icon: FiUser, label: 'Username', value: user.username },
    { icon: FiMail, label: 'Email', value: user.email },
    { icon: FiCalendar, label: 'Member Since', value: new Date(user.created_at).toLocaleDateString() },
    { icon: FiShield, label: 'Account Status', value: user.is_active ? 'Active' : 'Inactive' },
  ]

  return (
    <div className="min-h-screen pt-20 pb-10 px-4 sm:px-6 lg:px-8 max-w-4xl mx-auto">
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-white">Profile</h1>
        <p className="text-gray-400 mt-1">Your account information</p>
      </div>

      <div className="glass-card p-8 mb-8">
        <div className="flex items-center space-x-6 mb-8">
          <div className="w-20 h-20 rounded-full bg-gradient-to-br from-blue-500 to-purple-600 flex items-center justify-center">
            <span className="text-3xl font-bold text-white">
              {user.username.charAt(0).toUpperCase()}
            </span>
          </div>
          <div>
            <h2 className="text-2xl font-bold text-white">{user.username}</h2>
            <p className="text-gray-400">{user.email}</p>
          </div>
        </div>

        <div className="grid sm:grid-cols-2 gap-6">
          {infoCards.map((card) => (
            <div key={card.label} className="p-4 bg-gray-800/50 rounded-xl">
              <div className="flex items-center space-x-3">
                <card.icon className="w-5 h-5 text-blue-400" />
                <div>
                  <p className="text-gray-400 text-sm">{card.label}</p>
                  <p className="text-white font-medium">{card.value}</p>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
