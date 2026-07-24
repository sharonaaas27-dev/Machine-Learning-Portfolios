export default function ConfidenceMeter({ confidence, prediction }: { confidence: number; prediction: string }) {
  const isSpam = prediction === 'spam'
  const color = isSpam ? 'from-red-500 to-red-600' : 'from-green-500 to-green-600'
  const bgColor = isSpam ? 'bg-red-500/20' : 'bg-green-500/20'
  const textColor = isSpam ? 'text-red-400' : 'text-green-400'

  return (
    <div className="space-y-2">
      <div className="flex justify-between items-center">
        <span className={`text-sm font-medium ${textColor}`}>
          {isSpam ? 'Spam Risk' : 'Safe'}
        </span>
        <span className={`text-sm font-bold ${textColor}`}>
          {(confidence * 100).toFixed(1)}%
        </span>
      </div>
      <div className={`h-3 rounded-full ${bgColor} overflow-hidden`}>
        <div
          className={`h-full rounded-full bg-gradient-to-r ${color} confidence-bar`}
          style={{ width: `${confidence * 100}%` }}
        />
      </div>
    </div>
  )
}
