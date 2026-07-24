import { Link } from 'react-router-dom';

export default function NotFound() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-6xl font-bold text-netflix-red mb-4">404</h1>
      <p className="text-xl text-netflix-muted mb-8">Page not found</p>
      <Link to="/" className="btn-primary">Go Home</Link>
    </div>
  );
}