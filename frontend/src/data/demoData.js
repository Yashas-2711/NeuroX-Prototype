import { Building2, BusFront, Droplets, GraduationCap, Handshake, HeartPulse, Lightbulb, Recycle, Sprout, Target } from 'lucide-react'

export const statistics = [
  { value: '125+', label: 'Challenges', icon: Target },
  { value: '42', label: 'Universities', icon: Building2 },
  { value: '28', label: 'Industry Partners', icon: Handshake },
  { value: '67', label: 'Solutions', icon: Lightbulb },
]

export const challenges = [
  { domain: 'Water & Sanitation', title: 'Public Water Tap Wastage', description: 'Public taps remain open after use, causing unnecessary water wastage in busy community areas.', location: 'Maharashtra', confidence: '91%', impact: 'High', similarCount: 3, icon: Droplets },
  { domain: 'Waste Management', title: 'Overflowing Community Waste Points', description: 'Collection schedules do not match local demand, leaving roadside waste points overflowing for days.', location: 'Pune, Maharashtra', confidence: '88%', impact: 'High', similarCount: 5, icon: Recycle },
  { domain: 'Healthcare', title: 'Rural Medicine Stock Visibility', description: 'Primary health centres lack a simple way to report and anticipate essential medicine shortages.', location: 'Nashik, Maharashtra', confidence: '94%', impact: 'High', similarCount: 4, icon: HeartPulse },
  { domain: 'Transportation', title: 'Unreliable Last-Mile Bus Updates', description: 'Commuters receive no timely information about bus delays on suburban and rural connecting routes.', location: 'Bengaluru, Karnataka', confidence: '86%', impact: 'Medium', similarCount: 6, icon: BusFront },
  { domain: 'Education', title: 'Career Guidance Gap for Government Schools', description: 'Students need accessible pathways to discover careers, scholarships, and local learning opportunities.', location: 'Jaipur, Rajasthan', confidence: '89%', impact: 'Medium', similarCount: 2, icon: GraduationCap },
  { domain: 'Agriculture', title: 'Smallholder Crop Advisory Access', description: 'Farmers need localized, easy-to-understand guidance for changing weather and crop disease risks.', location: 'Guntur, Andhra Pradesh', confidence: '92%', impact: 'High', similarCount: 7, icon: Sprout },
]

export const solutionFlow = [
  { title: 'Problem', icon: Target }, { title: 'AI Understanding', icon: Lightbulb }, { title: 'Similarity Detection', icon: Recycle }, { title: 'Smart Matching', icon: Handshake }, { title: 'Collaborative Solution', icon: Building2 },
]
