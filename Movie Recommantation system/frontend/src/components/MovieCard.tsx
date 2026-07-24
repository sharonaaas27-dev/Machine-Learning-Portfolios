import { Link } from 'react-router-dom';
import { Movie } from '../types';

interface Props {
  movie: Movie;
}

export default function MovieCard({ movie }: Props) {
  const genres = movie.genres.split('|').filter(Boolean);

  return (
    <Link to={`/movies/${movie.id}`} className="card group">
      <div className="aspect-[2/3] bg-netflix-darker flex items-center justify-center overflow-hidden">
        {movie.poster_path ? (
          <img
            src={movie.poster_path}
            alt={movie.title}
            className="w-full h-full object-cover"
            loading="lazy"
          />
        ) : (
          <div className="text-center p-4">
            <div className="text-4xl mb-2">🎬</div>
            <p className="text-xs text-netflix-muted truncate">{movie.title}</p>
          </div>
        )}
      </div>
      <div className="p-3">
        <h3 className="font-semibold text-sm truncate group-hover:text-netflix-red transition">
          {movie.title}
        </h3>
        <div className="flex items-center gap-2 mt-1">
          <span className="text-yellow-400 text-xs">★</span>
          <span className="text-xs text-netflix-muted">
            {movie.average_rating?.toFixed(1) || 'N/A'}
          </span>
          <span className="text-xs text-netflix-muted">({movie.rating_count})</span>
        </div>
        <div className="flex flex-wrap gap-1 mt-2">
          {genres.slice(0, 3).map((g) => (
            <span key={g} className="text-[10px] px-1.5 py-0.5 bg-netflix-darker rounded text-netflix-muted">
              {g}
            </span>
          ))}
        </div>
      </div>
    </Link>
  );
}