import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { predictApi, historyApi } from '../services/api'
import type { PredictRequest, BulkPredictRequest } from '../types'
import toast from 'react-hot-toast'

export function usePredict() {
  return useMutation({
    mutationFn: (data: PredictRequest) => predictApi.predict(data),
    onError: () => toast.error('Prediction failed. Please try again.'),
  })
}

export function useBulkPredict() {
  return useMutation({
    mutationFn: (data: BulkPredictRequest) => predictApi.predictBulk(data),
    onError: () => toast.error('Batch prediction failed.'),
  })
}

export function useHistory(params?: { search?: string; page?: number; limit?: number }) {
  return useQuery({
    queryKey: ['history', params],
    queryFn: () => historyApi.getAll(params).then((res) => res.data),
  })
}

export function useDeletePrediction() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (id: number) => historyApi.delete(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['history'] })
      toast.success('Prediction deleted')
    },
    onError: () => toast.error('Failed to delete'),
  })
}

export function useModelMetrics() {
  return useQuery({
    queryKey: ['metrics'],
    queryFn: () => import('../services/api').then((mod) => mod.modelApi.getMetrics().then((res) => res.data)),
    refetchOnWindowFocus: false,
  })
}

export function useHealth() {
  return useQuery({
    queryKey: ['health'],
    queryFn: () => import('../services/api').then((mod) => mod.modelApi.getHealth().then((res) => res.data)),
    refetchInterval: 30000,
  })
}

export function useRetrain() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: () => import('../services/api').then((mod) => mod.modelApi.retrain()),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['metrics'] })
      queryClient.invalidateQueries({ queryKey: ['health'] })
      toast.success('Model retrained successfully!')
    },
    onError: () => toast.error('Retraining failed'),
  })
}
