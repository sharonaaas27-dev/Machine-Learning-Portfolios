interface Props {
  genre: string;
  active?: boolean;
  onClick?: () => void;
}

const genreColors: Record<string, string> = {
  Action: 'bg-red-900/50 text-red-300 border-red-700',
  Adventure: 'bg-orange-900/50 text-orange-300 border-orange-700',
  Comedy: 'bg-yellow-900/50 text-yellow-300 border-yellow-700',
  Drama: 'bg-blue-900/50 text-blue-300 border-blue-700',
  Horror: 'bg-purple-900/50 text-purple-300 border-purple-700',
  Romance: 'bg-pink-900/50 text-pink-300 border-pink-700',
  'Sci-Fi': 'bg-cyan-900/50 text-cyan-300 border-cyan-700',
  Thriller: 'bg-indigo-900/50 text-indigo-300 border-indigo-700',
  Fantasy: 'bg-emerald-900/50 text-emerald-300 border-emerald-700',
  Mystery: 'bg-violet-900/50 text-violet-300 border-violet-700',
};

export default function GenreChip({ genre, active, onClick }: Props) {
  const colors = genreColors[genre] || 'bg-gray-800 text-gray-300 border-gray-600';

  return (
    <button
      onClick={onClick}
      className={`px-3 py-1 rounded-full text-xs font-medium border transition-all ${
        colors
      } ${
        active ? 'ring-2 ring-white/30 scale-105' : 'opacity-70 hover:opacity-100'
      }`}
    >
      {genre}
    </button>
  );
}