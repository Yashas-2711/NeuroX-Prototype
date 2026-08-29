import { ArrowRight, MapPin, Sparkles } from 'lucide-react'

function ChallengeCard({ challenge }) {
  const Icon = challenge.icon
  return <article className="challenge-card"><div className="card-topline"><span className="domain-badge">{challenge.domain}</span><span className="domain-icon"><Icon size={20} /></span></div><h3>{challenge.title}</h3><p className="card-description">{challenge.description}</p><div className="location"><MapPin size={15} />{challenge.location}</div><div className="metrics"><div><span>AI Confidence</span><strong className="confidence"><Sparkles size={13} />{challenge.confidence}</strong></div><div><span>Impact</span><strong className={`impact impact-${challenge.impact.toLowerCase()}`}>{challenge.impact}</strong></div></div><p className="similar-count"><span>{challenge.similarCount}</span> Similar Problems</p><button className="analyze-button" type="button">Analyze Challenge <ArrowRight size={16} /></button></article>
}
export default ChallengeCard
