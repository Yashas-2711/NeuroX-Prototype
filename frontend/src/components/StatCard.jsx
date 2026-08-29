function StatCard({ stat }) {
  const Icon = stat.icon
  return <article className="stat-card"><span className="stat-icon"><Icon size={21} /></span><div><strong>{stat.value}</strong><span>{stat.label}</span></div></article>
}
export default StatCard
