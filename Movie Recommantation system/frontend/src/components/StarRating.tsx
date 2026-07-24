interface Props {
  rating: number;
  onChange?: (rating: number) => void;
  readonly?: boolean;
  size?: 'sm' | 'md' | 'lg';
}

export default function StarRating({ rating, onChange, readonly = false, size = 'md' }: Props) {
  const sizes = { sm: 'text-lg', md: 'text-2xl', lg: 'text-3xl' };

  return (
    <div className="flex gap-1">
      {[1, 2, 3, 4, 5].map((star) => (
        <button
          key={star}
          type="button"
          disabled={readonly}
          onClick={() => onChange?.(star)}
          className={`${sizes[size]} transition-colors ${
            star <= rating ? 'text-yellow-400' : 'text-gray-600'
          } ${readonly ? 'cursor-default' : 'hover:text-yellow-300 cursor-pointer'}`}
        >
          ★
        </button>
      ))}
    </div>
  );
}