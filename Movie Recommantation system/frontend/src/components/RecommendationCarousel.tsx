import { Link } from 'react-router-dom';
import { Recommendation } from '../types';

interface Props {
  title: string;
  items: Recommendation[];
  loading?: boolean;
}

export default function RecommendationCarousel({ title, items, loading }: Props) {
  if (loading) {
    return (
      <section className="mb-8">
        <h2 className="text-xl font-bold mb-4">{title}</h2>
        <div className="flex gap-4 overflow-x-auto pb-4">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="min-w-[160px]">
              <div className="aspect-[2/3] skeleton rounded" />
              <div className="h-4 skeleton mt-2 w-3/4" />
            </div>
          ))}
        </div>
      </section>
    );
  }

  if (!items?.length) return null;

  return (
    <section className="mb-8">
      <h2 className="text-xl font-bold mb-4">{title}</h2>
      <div className="flex gap-4 overflow-x-auto pb-4 scrollbar-thin">
        {items.map((item) => (
          <Link
            key={item.movieId}
            to={`/movies/${item.movieId}`}
            className="min-w-[160px] max-w-[160px] flex-shrink-0 group"
          >
            <div className="aspect-[2/3] bg-netflix-darker rounded overflow-hidden">
              {item.poster_path ? (
                <img src={item.poster_path} alt={item.title} className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300" />
              ) : (
                <div className="w-full h-full flex items-center justify-center text-3xl">🎬</div>
              )}
            </div>
            <p className="text-sm mt-1 truncate group-hover:text-netflix-red transition">{item.title}</p>
            {item.predicted_rating && (
              <p className="text-xs text-yellow-400">★ {item.predicted_rating.toFixed(1)}</p>
            )}
            {item.explanation && (
              <p className="text-[10px] text-netflix-muted mt-1 line-clamp-2">{item.explanation}</p>
            )}
          </Link>
        ))}
      </div>
    </section>
  );
}