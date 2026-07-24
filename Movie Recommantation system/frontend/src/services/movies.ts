import api from './api';
import { Movie } from '../types';

export const movieService = {
  async getMovies(page = 1, pageSize = 20, genre?: string, year?: number) {
    const params: any = { page, page_size: pageSize };
    if (genre) params.genre = genre;
    if (year) params.year = year;
    const { data } = await api.get('/movies', { params });
    return data;
  },

  async getMovie(id: number) {
    const { data } = await api.get<Movie>(`/movies/${id}`);
    return data;
  },

  async searchMovies(query: string) {
    const { data } = await api.get<Movie[]>('/movies/search', { params: { q: query } });
    return data;
  },

  async getByGenre(genre: string, limit = 50) {
    const { data } = await api.get<Movie[]>(`/movies/genre/${genre}`, { params: { limit } });
    return data;
  },

  async getTopRated(limit = 10) {
    const { data } = await api.get<Movie[]>('/movies/top-rated', { params: { limit } });
    return data;
  },

  async getTrending(limit = 10) {
    const { data } = await api.get<Movie[]>('/movies/trending', { params: { limit } });
    return data;
  },
};