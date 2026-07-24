import { Link } from 'react-router-dom';
import { useAuth } from '../hooks/useAuth';

export default function Landing() {
  const { user } = useAuth();

  return (
    <div className="min-h-screen">
      <div className="relative h-[80vh] bg-gradient-to-b from-netflix-darker via-netflix-dark to-netflix-dark">
        <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_top,rgba(229,9,20,0.15)_0%,transparent_70%)]" />
        <div className="relative z-10 max-w-7xl mx-auto px-4 h-full flex flex-col justify-center items-center text-center">
          <h1 className="text-5xl md:text-7xl font-bold mb-6">
            Discover Your Next
            <span className="text-netflix-red"> Favorite Movie</span>
          </h1>
          <p className="text-xl md:text-2xl text-netflix-muted max-w-2xl mb-10">
            Personalized movie recommendations powered by AI. Rate movies, explore genres,
            and get suggestions tailored just for you.
          </p>
          {user ? (
            <Link to="/dashboard" className="btn-primary text-lg px-10 py-4">
              Go to Dashboard
            </Link>
          ) : (
            <div className="flex gap-4">
              <Link to="/register" className="btn-primary text-lg px-10 py-4">
                Get Started
              </Link>
              <Link to="/login" className="btn-secondary text-lg px-10 py-4">
                Sign In
              </Link>
            </div>
          )}
        </div>
      </div>

      <div className="max-w-7xl mx-auto px-4 py-20">
        <div className="grid md:grid-cols-3 gap-8">
          <div className="text-center p-8 bg-netflix-light rounded-xl">
            <div className="text-4xl mb-4">🎯</div>
            <h3 className="text-xl font-bold mb-3">Content-Based Filtering</h3>
            <p className="text-netflix-muted">
              Find movies similar to ones you love using genre analysis and TF-IDF similarity.
            </p>
          </div>
          <div className="text-center p-8 bg-netflix-light rounded-xl">
            <div className="text-4xl mb-4">🤝</div>
            <h3 className="text-xl font-bold mb-3">Collaborative Filtering</h3>
            <p className="text-netflix-muted">
              Get recommendations based on what users with similar tastes enjoyed.
            </p>
          </div>
          <div className="text-center p-8 bg-netflix-light rounded-xl">
            <div className="text-4xl mb-4">⚡</div>
            <h3 className="text-xl font-bold mb-3">Hybrid Engine</h3>
            <p className="text-netflix-muted">
              Combined content and collaborative scores for the most accurate recommendations.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}