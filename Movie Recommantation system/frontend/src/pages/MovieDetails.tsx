import { useParams } from 'react-router-dom';
import { useMovie } from '../hooks/useMovies';
import { useContentRecommendations, useCollaborativeRecommendations } from '../hooks/useRecommendations';
import { useRateMovie, useUserRatings, useDeleteRating } from '../hooks/useRatings';
import StarRating from '../components/StarRating';
import RecommendationCarousel from '../components/RecommendationCarousel';
import LoadingSkeleton from '../components/LoadingSkeleton';
import { useState } from 'react';

export default function MovieDetails() {
  const { id } = useParams();
  const movieId = parseInt(id || '0');
  const { data: movie, isLoading } = useMovie(movieId);
  const { data: contentRecs, isLoading: contentLoading } = useContentRecommendations(movie?.movieId);
  const { data: userRatings } = useUserRatings();
  const rateMutation = useRateMovie();
  const deleteMutation = useDeleteRating();

  const userRating = userRatings?.find((r: any) => r.movie_id === movie?.movieId);
  const [rating, setRating] = useState(userRating?.rating || 0);

  const handleRate = async (value: number) => {
    setRating(value);
    try {
      await rateMutation.mutateAsync({ movieId: movie!.movieId, rating: value });
    } catch {
      // ignore
    }
  };

  const handleDeleteRating = async () => {
    if (!userRating) return;
    try {
      await deleteMutation.mutateAsync(userRating.id);
      setRating(0);
    } catch {
      // ignore
    }
  };

  if (isLoading) return <div className="pt-20"><LoadingSkeleton count={1} /></div>;
  if (!movie) return <div className="pt-20 text-center text-xl">Movie not found</div>;

  const genres = movie.genres.split('|').filter(Boolean);

  return (
    <div className="pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-4">
        <div className="bg-netflix-light rounded-xl overflow-hidden mb-10">
          <div className="md:flex">
            <div className="md:w-80 h-96 bg-netflix-darker flex items-center justify-center">
              {movie.poster_path ? (
                <img src={movie.poster_path} alt={movie.title} className="w-full h-full object-cover" />
              ) : (
                <div className="text-6xl">🎬</div>
              )}
            </div>
            <div className="p-8 flex-1">
              <h1 className="text-3xl font-bold mb-2">{movie.title}</h1>
              <div className="flex flex-wrap gap-2 mb-4">
                {genres.map((g) => (
                  <span key={g} className="px-3 py-1 bg-netflix-darker rounded-full text-sm text-netflix-muted">
                    {g}
                  </span>
                ))}
              </div>

              <div className="flex items-center gap-6 mb-4">
                <div className="flex items-center gap-2">
                  <span className="text-yellow-400 text-2xl">★</span>
                  <span className="text-2xl font-bold">{movie.average_rating?.toFixed(1) || 'N/A'}</span>
                  <span className="text-netflix-muted">({movie.rating_count} ratings)</span>
                </div>
              </div>

              {movie.overview && <p className="text-netflix-muted mb-6">{movie.overview}</p>}

              {movie.release_date && (
                <p className="text-sm text-netflix-muted mb-4">Released: {movie.release_date}</p>
              )}

              <div className="border-t border-gray-700 pt-6">
                <p className="text-sm font-medium mb-2">Your Rating</p>
                <div className="flex items-center gap-4">
                  <StarRating rating={rating || userRating?.rating || 0} onChange={handleRate} size="lg" />
                  {userRating && (
                    <button onClick={handleDeleteRating} className="text-sm text-netflix-muted hover:text-netflix-red">
                      Remove
                    </button>
                  )}
                </div>
                {rateMutation.isPending && <p className="text-xs text-netflix-muted mt-1">Saving...</p>}
              </div>
            </div>
          </div>
        </div>

        <RecommendationCarousel
          title="🔍 Similar Movies (Content-Based)"
          items={contentRecs || []}
          loading={contentLoading}
        />
      </div>
    </div>
  );
}