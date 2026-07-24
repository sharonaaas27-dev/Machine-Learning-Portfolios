import { useCollaborativeRecommendations, useHybridRecommendations } from '../hooks/useRecommendations';
import RecommendationCarousel from '../components/RecommendationCarousel';

export default function Recommendations() {
  const { data: collabRecs, isLoading: collabLoading } = useCollaborativeRecommendations();
  const { data: hybridRecs, isLoading: hybridLoading } = useHybridRecommendations();

  return (
    <div className="pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-4">
        <h1 className="text-3xl font-bold mb-8">Recommendations</h1>

        <RecommendationCarousel
          title="🤝 Collaborative Filtering"
          items={collabRecs || []}
          loading={collabLoading}
        />

        <RecommendationCarousel
          title="⚡ Hybrid Recommendations"
          items={hybridRecs || []}
          loading={hybridLoading}
        />

        {!collabLoading && !hybridLoading && !collabRecs?.length && !hybridRecs?.length && (
          <div className="text-center py-20">
            <p className="text-xl text-netflix-muted mb-4">
              Rate some movies first to get personalized recommendations!
            </p>
            <a href="/movies" className="btn-primary">Browse Movies</a>
          </div>
        )}
      </div>
    </div>
  );
}