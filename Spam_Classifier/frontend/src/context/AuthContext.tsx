import React, { createContext, useState, useEffect, type ReactNode } from 'react'
import { authApi } from '../services/api'
import type { User, LoginCredentials, RegisterData } from '../types'
import toast from 'react-hot-toast'

interface AuthContextType {
  user: User | null
  token: string | null
  isLoading: boolean
  login: (credentials: LoginCredentials) => Promise<void>
  register: (data: RegisterData) => Promise<void>
  logout: () => void
}

export const AuthContext = createContext<AuthContextType>({
  user: null,
  token: null,
  isLoading: true,
  login: async () => {},
  register: async () => {},
  logout: () => {},
})

export function AuthProvider({ children }: { children: ReactNode }) {
  const [user, setUser] = useState<User | null>(null)
  const [token, setToken] = useState<string | null>(localStorage.getItem('token'))
  const [isLoading, setIsLoading] = useState(true)

  useEffect(() => {
    if (token) {
      authApi.getProfile()
        .then((res) => setUser(res.data))
        .catch(() => {
          localStorage.removeItem('token')
          setToken(null)
        })
        .finally(() => setIsLoading(false))
    } else {
      setIsLoading(false)
    }
  }, [token])

  const login = async (credentials: LoginCredentials) => {
    const res = await authApi.login(credentials)
    localStorage.setItem('token', res.data.access_token)
    setToken(res.data.access_token)
    const profileRes = await authApi.getProfile()
    setUser(profileRes.data)
    toast.success('Welcome back!')
  }

  const register = async (data: RegisterData) => {
    await authApi.register(data)
    toast.success('Account created! Please log in.')
  }

  const logout = () => {
    localStorage.removeItem('token')
    setToken(null)
    setUser(null)
    toast.success('Logged out')
  }

  return (
    <AuthContext.Provider value={{ user, token, isLoading, login, register, logout }}>
      {children}
    </AuthContext.Provider>
  )
}
