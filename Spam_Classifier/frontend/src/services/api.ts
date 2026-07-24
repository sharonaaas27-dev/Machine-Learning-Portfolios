import axios from 'axios'
import type {
  AuthResponse,
  LoginCredentials,
  RegisterData,
  User,
  PredictResponse,
  PredictRequest,
  PredictionList,
  ModelMetrics,
  HealthStatus,
  BulkPredictRequest,
  BulkPredictResponse,
} from '../types'

const API_BASE = import.meta.env.VITE_API_URL || '/api'

const api = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
})

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      window.location.href = '/login'
    }
    return Promise.reject(error)
  }
)

export const authApi = {
  register: (data: RegisterData) => api.post<User>('/register', data),
  login: (data: LoginCredentials) => api.post<AuthResponse>('/login', data),
  getProfile: () => api.get<User>('/profile'),
}

export const predictApi = {
  predict: (data: PredictRequest) => api.post<PredictResponse>('/predict', data),
  predictBulk: (data: BulkPredictRequest) => api.post<BulkPredictResponse>('/predict/bulk', data),
}

export const historyApi = {
  getAll: (params?: { search?: string; page?: number; limit?: number }) =>
    api.get<PredictionList>('/history', { params }),
  delete: (id: number) => api.delete(`/history/${id}`),
  export: () => api.get('/history/export'),
}

export const modelApi = {
  getHealth: () => api.get<HealthStatus>('/health'),
  getMetrics: () => api.get<ModelMetrics>('/metrics'),
  retrain: () => api.post('/retrain'),
  getInfo: () => api.get('/model/info'),
}

export default api
