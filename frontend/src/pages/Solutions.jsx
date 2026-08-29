import { ArrowLeft, ArrowRight, LoaderCircle, Lightbulb } from 'lucide-react'
import { useCallback, useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import Navbar from '../components/Navbar'
import { getSolutions } from '../services/api'

function Solutions() {
  const [challenge] = useState(() => JSON.parse(sessionStorage.getItem('neuroxChallenge') || 'null'))
  const [items, setItems] = useState([]); const [loading, setLoading] = useState(Boolean(challenge)); const [error, setError] = useState('')
  const load = useCallback(async () => { if (!challenge) return; setError(''); try { const data = await getSolutions(challenge); setItems(data.recommendations || []) } catch { setError('Solution recommendations are temporarily unavailable.') } finally { setLoading(false) } }, [challenge])
  useEffect(() => { const timer = window.setTimeout(load, 0); return () => window.clearTimeout(timer) }, [load])
  const retry = () => { setLoading(true); load() }
  return <div className="app-shell form-shell"><Navbar /><main className="analysis-page container"><Link className="back-link" to="/impact"><ArrowLeft size={16} />Back to Impact Analysis</Link><div className="analysis-heading"><p className="eyebrow"><span />SUGGESTED SOLUTION DIRECTIONS</p><h1>Practical paths to explore.</h1><p>Based on the submitted challenge, NeuroX identified several practical directions that could be explored.</p></div>{loading ? <section className="analysis-card loading-card"><LoaderCircle className="spinner" size={30} /><h2>NeuroX is identifying solution directions...</h2></section> : error ? <section className="analysis-card empty-analysis"><h2>{error}</h2><p>Please try again.</p><button className="button button-secondary" onClick={retry}>Retry</button></section> : !challenge ? <section className="analysis-card empty-analysis"><h2>No challenge found.</h2><Link className="button button-primary" to="/submit">Submit a Challenge</Link></section> : <><div className="solution-grid">{items.map((item) => <article className="analysis-card solution-card" key={item.id}><Lightbulb size={22} /><span className="analysis-domain">{item.type}</span><h2>{item.title}</h2><p>{item.description}</p><div className="solution-tags"><span>{item.estimated_complexity} Complexity</span><span>{item.potential_impact} Potential Impact</span></div></article>)}</div><section className="analysis-card why-card"><h2>Why these solutions?</h2><p>These recommendations are selected from the challenge’s domain and problem characteristics. They are prototype directions for further exploration, not final engineering designs.</p></section><div className="analysis-actions"><Link className="button button-secondary" to="/impact"><ArrowLeft size={16} />Back to Impact Analysis</Link><Link className="button button-primary" to="/universities">Continue to University Collaboration <ArrowRight size={16} /></Link></div></>}</main></div>
}
export default Solutions
