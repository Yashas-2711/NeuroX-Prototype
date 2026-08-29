import { Menu, Plus, X } from 'lucide-react'
import { useState } from 'react'
import { Link } from 'react-router-dom'

const navItems = ['Challenge Hub', 'How It Works', 'About']

function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)
  return <header className="navbar"><div className="nav-content container"><Link className="brand" to="/" aria-label="NeuroX home"><span>NEURO<span className="brand-accent">X</span></span><small>AI-Powered Societal Problem Solving</small></Link><nav className="desktop-nav" aria-label="Primary navigation">{navItems.map((item) => <Link key={item} to={item === 'Challenge Hub' ? '/#challenges' : '/#how-it-works'}>{item}</Link>)}</nav><Link className="button button-primary nav-action" to="/submit"><Plus size={17} />Submit Challenge</Link><button className="menu-button" type="button" aria-label="Toggle navigation menu" aria-expanded={isMenuOpen} onClick={() => setIsMenuOpen(!isMenuOpen)}>{isMenuOpen ? <X size={22} /> : <Menu size={22} />}</button></div>{isMenuOpen && <nav className="mobile-nav container" aria-label="Mobile navigation">{navItems.map((item) => <Link key={item} to={item === 'Challenge Hub' ? '/#challenges' : '/#how-it-works'} onClick={() => setIsMenuOpen(false)}>{item}</Link>)}<Link className="button button-primary" to="/submit" onClick={() => setIsMenuOpen(false)}><Plus size={17} />Submit Challenge</Link></nav>}</header>
}

export default Navbar
