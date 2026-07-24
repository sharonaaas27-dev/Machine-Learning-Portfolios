import { useDashboard } from '../hooks/useRecommendations';
import { useTopRated, useTrending } from '../hooks/useMovies';
import { useHybridRecommendations } from '../hooks/useRecommendations';
import MovieCard from '../components/MovieCard';
import RecommendationCarousel from '../components/RecommendationCarousel';
import LoadingSkeleton from '../components/LoadingSkeleton';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function Dashboard() {
  const { data: dashboard, isLoading: dashLoading } = useDashboard();
  const { data: topRated } = useTopRated(10);
  const { data: trending } = useTrending(10);
  const { data: hybridRecs, isLoading: recsLoading } = useHybridRecommendations();

  const chartData = {
    labels: dashboard?.top_genres?.map((g) => g.name) || [],
    datasets: [
      {
        label: 'Movies in Genre',
        data: dashboard?.top_genres?.map((g) => g.count) || [],
        backgroundColor: '#E50914',
        borderRadius: 4,
      },
    ],
  };

  return (
    <div className="pt-20 pb-10">
      <div className="max-w-7xl mx-auto px-4">
        <h1 className="text-3xl font-bold mb-8">Dashboard</h1>

        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-10">
          <StatCard title="Total Movies" value={dashboard?.total_movies ?? 0} icon="🎬" />
          <StatCard title="Total Ratings" value={dashboard?.total_ratings ?? 0} icon="⭐" />
          <StatCard title="Your Ratings" value={dashboard?.user_ratings_count ?? 0} icon="📊" />
          <StatCard title="Genres" value={dashboard?.top_genres?.length ?? 0} icon="🏷️" />
        </div>

        <div className="grid lg:grid-cols-3 gap-8 mb-10">
          <div className="lg:col-span-2 bg-netflix-light rounded-xl p-6">
            <h2 className="text-lg font-bold mb-4">Genre Distribution</h2>
            {dashLoading ? (
              <div className="h-64 skeleton" />
            ) : (
              <Bar
                data={chartData}
                options={{
                  responsive: true,
                  plugins: { legend: { display: false } },
                  scales: {
                    x: { ticks: { color: '#b3b3b3' }, grid: { color: '#333' } },
                    y: { ticks: { color: '#b3b3b3' }, grid: { color: '#333' } },
                  },
                }}
              />
            )}
          </div>

          <div className="bg-netflix-light rounded-xl p-6">
            <h2 className="text-lg font-bold mb-4">Recently Rated</h2>
            {dashboard?.recently_rated?.length ? (
              <div className="space-y-3">
                {dashboard.recently_rated.map((r: any) => (
                  <div key={r.movieId} className="flex items-center justify-between">
                    <div>
                      <p className="text-sm font-medium truncate max-w-[150px]">{r.title}</p>
                      <p className="text-xs text-netflix-muted">{r.genres?.split('|')[0]}</p>
                    </div>
                    <span className="text-yellow-400 text-sm">★ {r.rating}</span>
                  </div>
                ))}
              </div>
            ) : (
              <p className="text-netflix-muted text-sm">Rate some movies to see them here</p>
            )}
          </div>
        </div>

        <RecommendationCarousel
          title="🎯 Personalized For You"
          items={hybridRecs || []}
          loading={recsLoading}
        />

        <section className="mb-10">
          <h2 className="text-xl font-bold mb-4">⭐ Top Rated Movies</h2>
          {topRated ? (
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
              {topRated.map((m: any) => <MovieCard key={m.id} movie={m} />)}
            </div>
          ) : <LoadingSkeleton count={6} />}
        </section>

        <section>
          <h2 className="text-xl font-bold mb-4">🔥 Trending Movies</h2>
          {trending ? (
            <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 xl:grid-cols-6 gap-4">
              {trending.map((m: any) => <MovieCard key={m.id} movie={m} />)}
            </div>
          ) : <LoadingSkeleton count={6} />}
        </section>
      </div>
    </div>
  );
}

function StatCard({ title, value, icon }: { title: string; value: number; icon: string }) {
  return (
    <div className="bg-netflix-light rounded-xl p-5">
      <div className="text-2xl mb-2">{icon}</div>
      <p className="text-2xl font-bold">{value.toLocaleString()}</p>
      <p className="text-sm text-netflix-muted">{title}</p>
    </div>
  );
}