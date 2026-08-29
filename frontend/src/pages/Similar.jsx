import { ArrowLeft, Network } from 'lucide-react'
import { Link } from 'react-router-dom'
import Navbar from '../components/Navbar'

function Similar() { return <div className="app-shell form-shell"><Navbar /><main className="analysis-page container"><section className="analysis-card empty-analysis"><Network size={38} className="similar-icon" /><p className="eyebrow"><span />SIMILAR CHALLENGES</p><h2>Similarity Detection</h2><p>NeuroX will compare this challenge with existing societal problems.</p><div className="coming-soon">Coming in Step 6</div><Link className="button button-secondary" to="/analysis"><ArrowLeft size={16} />Back to Analysis</Link></section></main></div> }
export default Similar
