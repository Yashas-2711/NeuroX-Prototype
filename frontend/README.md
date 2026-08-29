# NeuroX Frontend

NeuroX is an AI-powered societal challenge collaboration platform prototype for hackathon demonstrations. This React/Vite frontend guides a challenge through local AI analysis, similarity detection, impact assessment, solution recommendations, and university/industry collaboration matching.

## Features

- Challenge Hub and guided submission flow
- BERT-tiny classification results from the FastAPI backend
- MiniLM semantic similarity results
- Transparent prototype impact scoring
- Curated solution directions
- Demo university and industry matching
- MongoDB-backed challenge and solution persistence
- SIH Presentation Mode at `/demo`
- Solution Workspace at `/workspace`

All AI inference runs locally through the backend. University and industry organizations are fictional demo data and do not represent confirmed partnerships.

## Requirements

- Node.js 18+
- A running NeuroX backend at `http://127.0.0.1:8000`

The backend setup, Python environment, local model checkpoint, and MongoDB Atlas configuration are documented in [`../backend`](../backend).

## Run locally

```powershell
npm install
npm run dev
```

Open the Vite URL shown in the terminal, normally `http://localhost:5173`.

To use another backend URL, create a local `.env` file (do not commit it):

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Demo flow

```text
/submit
  → /analysis
  → /similar
  → /impact
  → /solutions
  → /universities
  → /industry
  → /workspace
  → /demo
```

The current challenge is held in `sessionStorage` for navigation while saved challenges and solution concepts are persisted by the FastAPI/MongoDB backend.

## Scripts

```powershell
npm run dev       # Start the development server
npm run build     # Create a production build
npm run lint      # Run Oxlint
npm run preview   # Preview the production build
```

## Project structure

```text
src/
├── components/   Shared navigation and UI components
├── pages/        Challenge, analysis, collaboration, workspace, and demo pages
└── services/     FastAPI client functions
```

## Prototype disclaimer

Impact scores and solution directions are transparent prototype guidance, not scientifically validated predictions or final engineering designs. Demo universities and industries are fictional demonstration data.
