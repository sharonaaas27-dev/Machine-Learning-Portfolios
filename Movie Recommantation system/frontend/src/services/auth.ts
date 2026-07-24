import api from './api';
import { AuthResponse } from '../types';

export const authService = {
  async register(username: string, email: string, password: string) {
    const { data } = await api.post<AuthResponse>('/register', { username, email, password });
    return data;
  },

  async login(username: string, password: string) {
    const { data } = await api.post<AuthResponse>('/login', { username, password });
    return data;
  },

  async getProfile() {
    const { data } = await api.get('/profile');
    return data;
  },
};