import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from './pages/Home'
import SubmitChallenge from './pages/SubmitChallenge'
import Analysis from './pages/Analysis'
import Similar from './pages/Similar'
import './index.css'

function App() { return <BrowserRouter><Routes><Route path="/" element={<Home />} /><Route path="/submit" element={<SubmitChallenge />} /><Route path="/analysis" element={<Analysis />} /><Route path="/similar" element={<Similar />} /></Routes></BrowserRouter> }

export default App
