import { ArrowLeft, ArrowRight, LoaderCircle, Network } from 'lucide-react'
import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import Navbar from '../components/Navbar'
import { findSimilarChallenges } from '../services/api'

function Similar() {
  const [challenge] = useState(() => JSON.parse(sessionStorage.getItem('neuroxChallenge') || 'null'))
  const [results, setResults] = useState([])
  const [loading, setLoading] = useState(Boolean(challenge))
  const [error, setError] = useState('')
  const loadResults = useCallback(async () => {
    if (!challenge) return
    setError('')
    try { const data = await findSimilarChallenges(challenge); setResults(data.results || []) }
    catch { setError('Similarity analysis is temporarily unavailable.') }
    finally { setLoading(false) }
  }, [challenge])
  useEffect(() => { const timer = window.setTimeout(loadResults, 0); return () => window.clearTimeout(timer) }, [loadResults])
  const retry = () => { setLoading(true); loadResults() }
  return <div className="app-shell form-shell"><Navbar /><main className="analysis-page container"><Link className="back-link" to="/analysis"><ArrowLeft size={16} />Back to Analysis</Link><div className="analysis-heading"><p className="eyebrow"><span />SIMILAR CHALLENGES</p><h1>Existing Problems, Shared Solutions.</h1><p>NeuroX compares this challenge with the current demo network to surface related opportunities.</p></div>{loading ? <section className="analysis-card loading-card"><LoaderCircle className="spinner" size={30} /><h2>NeuroX is checking existing challenges...</h2></section> : error ? <section className="analysis-card empty-analysis"><h2>{error}</h2><p>Please try again.</p><button className="button button-secondary" type="button" onClick={retry}>Try Again</button></section> : !challenge ? <section className="analysis-card empty-analysis"><Network size={38} className="similar-icon" /><h2>No challenge found.</h2><Link className="button button-primary" to="/submit">Submit a Challenge</Link></section> : <><div className="similar-results-heading"><h2>SIMILAR CHALLENGES FOUND</h2><span>{results.length} results from the demo dataset</span></div>{results.length ? <div className="similar-grid">{results.map((item) => <article className="analysis-card similar-result" key={item.id}><span className="analysis-domain">{item.classification}</span><h2>{item.title}</h2><p>{item.description}</p><div className="similar-meta"><span>{item.location}</span><span>{item.domain}</span><strong>{(item.similarity * 100).toFixed(2)}% Similarity</strong></div><small className="similar-classification">{item.classification}</small></article>)}</div> : <section className="analysis-card empty-analysis"><h2>No closely related challenge was found in the current demo dataset.</h2></section>}<div className="analysis-actions"><Link className="button button-secondary" to="/analysis"><ArrowLeft size={16} />Back to Analysis</Link><Link className="button button-primary" to="/impact">Continue to Impact Analysis <ArrowRight size={16} /></Link></div></>}</main></div>
}
export default Similar
