import { useState } from 'react';
import { useMovies } from '../hooks/useMovies';
import MovieCard from '../components/MovieCard';
import GenreChip from '../components/GenreChip';
import LoadingSkeleton from '../components/LoadingSkeleton';

const GENRES = [
  'Action', 'Adventure', 'Comedy', 'Drama', 'Horror', 'Romance',
  'Sci-Fi', 'Thriller', 'Fantasy', 'Mystery', 'Animation', 'Documentary',
];

export default function BrowseMovies() {
  const [page, setPage] = useState(1);
  const [selectedGenre, setSelectedGenre] = useState<string | undefined>();
  const { data, isLoading } = useMovies(page, selectedGenre);

  return (
    <div className="pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-4">
        <h1 className="text-3xl font-bold mb-6">Browse Movies</h1>

        <div className="flex flex-wrap gap-2 mb-8">
          <GenreChip
            genre="All"
            active={!selectedGenre}
            onClick={() => { setSelectedGenre(undefined); setPage(1); }}
          />
          {GENRES.map((g) => (
            <GenreChip
              key={g}
              genre={g}
              active={selectedGenre === g}
              onClick={() => { setSelectedGenre(g); setPage(1); }}
            />
          ))}
        </div>

        {isLoading ? (
          <LoadingSkeleton count={12} />
        ) : (
          <>
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
              {data?.movies?.map((m: any) => <MovieCard key={m.id} movie={m} />)}
            </div>

            {data && (
              <div className="flex items-center justify-between mt-8">
                <p className="text-netflix-muted text-sm">
                  Showing {data.movies.length} of {data.total} movies
                </p>
                <div className="flex gap-3">
                  <button
                    onClick={() => setPage((p) => Math.max(1, p - 1))}
                    disabled={page === 1}
                    className="btn-secondary text-sm"
                  >
                    Previous
                  </button>
                  <button
                    onClick={() => setPage((p) => p + 1)}
                    disabled={page * 20 >= data.total}
                    className="btn-primary text-sm"
                  >
                    Next
                  </button>
                </div>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}