export interface User {
  id: number
  username: string
  email: string
  is_active: boolean
  created_at: string
}

export interface LoginCredentials {
  username: string
  password: string
}

export interface RegisterData {
  username: string
  email: string
  password: string
}

export interface AuthResponse {
  access_token: string
  token_type: string
}

export interface PredictRequest {
  message: string
}

export interface PredictResponse {
  prediction: string
  confidence: number
  spam_probability: number
  ham_probability: number
  processing_time: number
  top_keywords: string[]
  explanation: string
}

export interface Prediction {
  id: number
  message: string
  prediction: string
  confidence: number
  spam_probability: number
  ham_probability: number
  processing_time: number
  top_keywords: string
  explanation: string
  created_at: string
}

export interface PredictionList {
  total: number
  predictions: Prediction[]
}

export interface ModelMetrics {
  best_model: string
  accuracy: number
  precision: number
  recall: number
  f1_score: number
  roc_auc: number
  cross_val_mean: number
  cross_val_std: number
  confusion_matrix: number[][]
  model_comparison: Record<string, ModelComparisonEntry>
  training_samples: number
  feature_count: number
}

export interface ModelComparisonEntry {
  accuracy: number
  precision: number
  recall: number
  f1_score: number
  roc_auc?: number
}

export interface HealthStatus {
  status: string
  model_trained: boolean
}

export interface BulkPredictRequest {
  messages: string[]
}

export interface BulkPredictResponse {
  results: PredictResponse[]
}
