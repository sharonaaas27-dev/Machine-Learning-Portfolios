import api from './api';
import { Rating } from '../types';

export const ratingService = {
  async rateMovie(movieId: number, rating: number) {
    const { data } = await api.post<Rating>('/ratings', { movie_id: movieId, rating });
    return data;
  },

  async updateRating(ratingId: number, rating: number) {
    const { data } = await api.put<Rating>(`/ratings/${ratingId}`, { rating });
    return data;
  },

  async deleteRating(ratingId: number) {
    await api.delete(`/ratings/${ratingId}`);
  },

  async getUserRatings() {
    const { data } = await api.get<Rating[]>('/ratings/user');
    return data;
  },
};