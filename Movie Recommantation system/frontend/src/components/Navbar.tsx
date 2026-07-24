import { Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';
import { useState } from 'react';
import { movieService } from '../services/movies';
import { Movie } from '../types';

export default function Navbar() {
  const { user, logout } = useAuth();
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<Movie[]>([]);
  const [showResults, setShowResults] = useState(false);

  const handleSearch = async (val: string) => {
    setQuery(val);
    if (val.length > 1) {
      const movies = await movieService.searchMovies(val);
      setResults(movies.slice(0, 5));
      setShowResults(true);
    } else {
      setResults([]);
      setShowResults(false);
    }
  };

  return (
    <nav className="bg-netflix-darker border-b border-gray-800 fixed top-0 w-full z-50">
      <div className="max-w-7xl mx-auto px-4 h-16 flex items-center justify-between">
        <div className="flex items-center gap-8">
          <Link to="/" className="text-netflix-red text-2xl font-bold tracking-wide">
            MovieRec
          </Link>
          {user && (
            <div className="hidden md:flex gap-6 text-sm">
              <Link to="/dashboard" className="hover:text-white transition">Dashboard</Link>
              <Link to="/movies" className="hover:text-white transition">Browse</Link>
              <Link to="/recommendations" className="hover:text-white transition">Recommendations</Link>
            </div>
          )}
        </div>

        <div className="flex items-center gap-4">
          {user && (
            <div className="relative">
              <input
                type="text"
                placeholder="Search movies..."
                value={query}
                onChange={(e) => handleSearch(e.target.value)}
                onBlur={() => setTimeout(() => setShowResults(false), 200)}
                className="input-field w-48 md:w-64 text-sm"
              />
              {showResults && results.length > 0 && (
                <div className="absolute top-full mt-1 w-full bg-netflix-light border border-gray-700 rounded shadow-xl">
                  {results.map((m) => (
                    <Link
                      key={m.id}
                      to={`/movies/${m.id}`}
                      className="block px-3 py-2 text-sm hover:bg-netflix-darker truncate"
                      onClick={() => { setShowResults(false); setQuery(''); }}
                    >
                      {m.title}
                    </Link>
                  ))}
                </div>
              )}
            </div>
          )}

          {user ? (
            <div className="flex items-center gap-3">
              <Link to="/profile" className="text-sm text-netflix-muted hover:text-white">
                {user.username}
              </Link>
              <button onClick={logout} className="btn-primary text-sm py-1.5 px-4">
                Logout
              </button>
            </div>
          ) : (
            <div className="flex gap-3">
              <Link to="/login" className="btn-secondary text-sm py-1.5 px-4">Login</Link>
              <Link to="/register" className="btn-primary text-sm py-1.5 px-4">Register</Link>
            </div>
          )}
        </div>
      </div>
    </nav>
  );
}