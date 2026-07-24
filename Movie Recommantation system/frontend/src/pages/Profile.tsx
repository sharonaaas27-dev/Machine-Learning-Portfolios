import { useAuth } from '../hooks/useAuth';
import { useUserRatings, useDeleteRating } from '../hooks/useRatings';
import StarRating from '../components/StarRating';
import { Link } from 'react-router-dom';

export default function Profile() {
  const { user, logout } = useAuth();
  const { data: ratings, isLoading } = useUserRatings();
  const deleteMutation = useDeleteRating();

  if (!user) return null;

  return (
    <div className="pt-20 pb-10">
      <div className="max-w-4xl mx-auto px-4">
        <div className="bg-netflix-light rounded-xl p-8 mb-8">
          <h1 className="text-3xl font-bold mb-6">Profile</h1>
          <div className="grid md:grid-cols-2 gap-4">
            <div>
              <p className="text-sm text-netflix-muted">Username</p>
              <p className="text-lg font-medium">{user.username}</p>
            </div>
            <div>
              <p className="text-sm text-netflix-muted">Email</p>
              <p className="text-lg font-medium">{user.email}</p>
            </div>
            <div>
              <p className="text-sm text-netflix-muted">Member Since</p>
              <p className="text-lg font-medium">
                {new Date(user.created_at).toLocaleDateString()}
              </p>
            </div>
          </div>
        </div>

        <div className="bg-netflix-light rounded-xl p-8">
          <h2 className="text-xl font-bold mb-4">Your Ratings ({ratings?.length || 0})</h2>
          {isLoading ? (
            <div className="space-y-3">
              {[1, 2, 3].map((i) => <div key={i} className="h-16 skeleton" />)}
            </div>
          ) : ratings?.length ? (
            <div className="space-y-3">
              {ratings.map((r: any) => (
                <div key={r.id} className="flex items-center justify-between p-3 bg-netflix-darker rounded-lg">
                  <div>
                    <Link to={`/movies/${r.movie_id}`} className="font-medium hover:text-netflix-red">
                      {r.movie_title || `Movie #${r.movie_id}`}
                    </Link>
                    {r.movie_genres && (
                      <p className="text-xs text-netflix-muted">{r.movie_genres.split('|')[0]}</p>
                    )}
                  </div>
                  <div className="flex items-center gap-3">
                    <StarRating rating={r.rating} readonly size="sm" />
                    <button
                      onClick={() => deleteMutation.mutate(r.id)}
                      className="text-xs text-netflix-muted hover:text-netflix-red"
                    >
                      Delete
                    </button>
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <p className="text-netflix-muted">
              You haven't rated any movies yet.{' '}
              <Link to="/movies" className="text-netflix-red hover:underline">Browse movies</Link>
            </p>
          )}
        </div>
      </div>
    </div>
  );
}