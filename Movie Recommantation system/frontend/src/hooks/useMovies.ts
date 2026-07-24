import { useQuery } from '@tanstack/react-query';
import { movieService } from '../services/movies';

export const useMovies = (page = 1, genre?: string, year?: number) =>
  useQuery({
    queryKey: ['movies', page, genre, year],
    queryFn: () => movieService.getMovies(page, 20, genre, year),
  });

export const useMovie = (id: number) =>
  useQuery({
    queryKey: ['movie', id],
    queryFn: () => movieService.getMovie(id),
    enabled: !!id,
  });

export const useMovieSearch = (query: string) =>
  useQuery({
    queryKey: ['movieSearch', query],
    queryFn: () => movieService.searchMovies(query),
    enabled: query.length > 0,
  });

export const useTopRated = (limit = 10) =>
  useQuery({
    queryKey: ['topRated', limit],
    queryFn: () => movieService.getTopRated(limit),
  });

export const useTrending = (limit = 10) =>
  useQuery({
    queryKey: ['trending', limit],
    queryFn: () => movieService.getTrending(limit),
  });