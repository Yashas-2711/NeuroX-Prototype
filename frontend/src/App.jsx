import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import SubmitChallenge from './pages/SubmitChallenge'
import Analysis from './pages/Analysis'
import Similar from './pages/Similar'
import Impact from './pages/Impact'
import Solutions from './pages/Solutions'
import Universities from './pages/Universities'
import Industry from './pages/Industry'
import './index.css'

function App() { return <BrowserRouter><Routes><Route path="/" element={<Home />} /><Route path="/submit" element={<SubmitChallenge />} /><Route path="/analysis" element={<Analysis />} /><Route path="/similar" element={<Similar />} /><Route path="/impact" element={<Impact />} /><Route path="/solutions" element={<Solutions />} /><Route path="/universities" element={<Universities />} /><Route path="/industry" element={<Industry />} /></Routes></BrowserRouter> }

export default App
