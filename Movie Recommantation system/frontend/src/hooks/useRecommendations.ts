import { useQuery } from '@tanstack/react-query';
import { recommendationService } from '../services/recommendations';

export const useDashboard = () =>
  useQuery({
    queryKey: ['dashboard'],
    queryFn: () => recommendationService.getDashboard(),
  });

export const useContentRecommendations = (movieId: number) =>
  useQuery({
    queryKey: ['contentRecs', movieId],
    queryFn: () => recommendationService.getContentBased(movieId),
    enabled: !!movieId,
  });

export const useCollaborativeRecommendations = () =>
  useQuery({
    queryKey: ['collabRecs'],
    queryFn: () => recommendationService.getCollaborative(),
  });

export const useHybridRecommendations = () =>
  useQuery({
    queryKey: ['hybridRecs'],
    queryFn: () => recommendationService.getHybrid(),
  });