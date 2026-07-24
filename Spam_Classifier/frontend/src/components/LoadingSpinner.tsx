export default function LoadingSpinner({ size = 'md', text = '' }: { size?: 'sm' | 'md' | 'lg'; text?: string }) {
  const sizeClasses = { sm: 'w-6 h-6', md: 'w-10 h-10', lg: 'w-16 h-16' }

  return (
    <div className="flex flex-col items-center justify-center space-y-3">
      <div className={`${sizeClasses[size]} loader`} />
      {text && <p className="text-gray-400 text-sm">{text}</p>}
    </div>
  )
}
