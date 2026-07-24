export interface User {
  id: number;
  username: string;
  email: string;
  created_at: string;
}

export interface Movie {
  id: number;
  movieId: number;
  title: string;
  genres: string;
  poster_path: string;
  overview: string;
  release_date: string;
  average_rating: number;
  rating_count: number;
}

export interface Rating {
  id: number;
  user_id: number;
  movie_id: number;
  rating: number;
  timestamp: string;
  movie_title?: string;
  movie_genres?: string;
  movie_poster?: string;
}

export interface Recommendation {
  movieId: number;
  title: string;
  genres: string;
  poster_path: string;
  overview: string;
  average_rating: number;
  similarity_score?: number;
  predicted_rating?: number;
  hybrid_score?: number;
  content_score?: number;
  collaborative_score?: number;
  explanation?: string;
}

export interface DashboardData {
  total_movies: number;
  total_ratings: number;
  user_ratings_count: number;
  top_genres: { name: string; count: number }[];
  recently_rated: {
    movieId: number;
    title: string;
    genres: string;
    rating: number;
  }[];
}

export interface AuthResponse {
  access_token: string;
  token_type: string;
  user: User;
}