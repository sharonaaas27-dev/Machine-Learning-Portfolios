import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { ratingService } from '../services/ratings';

export const useUserRatings = () =>
  useQuery({
    queryKey: ['userRatings'],
    queryFn: () => ratingService.getUserRatings(),
  });

export const useRateMovie = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ movieId, rating }: { movieId: number; rating: number }) =>
      ratingService.rateMovie(movieId, rating),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['userRatings'] });
      queryClient.invalidateQueries({ queryKey: ['dashboard'] });
    },
  });
};

export const useDeleteRating = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (ratingId: number) => ratingService.deleteRating(ratingId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['userRatings'] });
      queryClient.invalidateQueries({ queryKey: ['dashboard'] });
    },
  });
};