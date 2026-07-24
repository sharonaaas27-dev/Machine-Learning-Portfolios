import api from './api';
import { Recommendation, DashboardData } from '../types';

export const recommendationService = {
  async getContentBased(movieId: number, topN = 10) {
    const { data } = await api.get<Recommendation[]>(`/recommend/content/${movieId}`, {
      params: { top_n: topN },
    });
    return data;
  },

  async getCollaborative(topN = 10) {
    const { data } = await api.get<Recommendation[]>('/recommend/collaborative', {
      params: { top_n: topN },
    });
    return data;
  },

  async getHybrid(topN = 10) {
    const { data } = await api.get<Recommendation[]>('/recommend/hybrid', {
      params: { top_n: topN },
    });
    return data;
  },

  async getDashboard() {
    const { data } = await api.get<DashboardData>('/recommend/dashboard');
    return data;
  },
};