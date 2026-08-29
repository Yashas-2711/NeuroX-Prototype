# NeuroX Prototype

NeuroX is a local, AI-assisted societal challenge collaboration platform prototype built for an inter-college hackathon demonstration.

It helps move a community problem from submission to a practical, collaborative solution:

```text
Challenge
  → BERT-tiny classification
  → MiniLM similarity detection
  → Impact assessment
  → Solution directions
  → University matching
  → Industry matching
  → Solution Workspace
  → MongoDB persistence
```

## What the prototype demonstrates

- Challenge Hub and guided challenge submission
- Local BERT-tiny problem classification
- Local `sentence-transformers/all-MiniLM-L6-v2` semantic similarity
- Transparent deterministic impact scoring
- Curated domain-based solution recommendations
- Fictional demo university and industry matching
- Persistent challenge and solution records in MongoDB Atlas
- SIH Presentation Mode at `/demo`
- Solution Workspace at `/workspace`

AI processing remains local to the backend. The demo university and industry organizations are fictional demonstration data and do not represent confirmed partnerships.

## Repository structure

```text
NeuroX-Prototype/
├── backend/       FastAPI API, local models, matching services, MongoDB access
├── frontend/      React/Vite web application
├── .gitignore
└── README.md
```

## Requirements

- Python 3.12+ (the included virtual environment may use a compatible Python version)
- Node.js 18+
- MongoDB Atlas account and database user for persistence

## Backend setup

```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill in your own MongoDB Atlas values locally:

```text
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster-url>/
MONGODB_DATABASE=neurox_prototype
MONGODB_DNS_SERVER=your_dns_server_here
```

Never commit `.env`. The backend uses two MongoDB collections: `challenges` and `solutions`.

Start the API:

```powershell
cd backend
.\venv\Scripts\Activate.ps1
python -m uvicorn main:app --reload
```

API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

## Frontend setup

```powershell
cd frontend
npm install
npm run dev
```

Open the Vite URL, normally [http://localhost:5173](http://localhost:5173).

The frontend defaults to `http://127.0.0.1:8000` for the backend. To override it, create `frontend/.env` locally:

```text
VITE_API_BASE_URL=http://127.0.0.1:8000
```

## Demo journey

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

The sample journey uses **Public Water Tap Wastage**. Temporary navigation state is held in `sessionStorage`; saved challenges and solution concepts are persisted through FastAPI and MongoDB Atlas.

## API overview

| Endpoint | Purpose |
| --- | --- |
| `GET /api/health` | API and database health |
| `POST /api/challenges/analyze` | BERT-tiny classification |
| `POST /api/challenges/similar` | MiniLM similarity results |
| `POST /api/challenges/impact` | Deterministic impact assessment |
| `POST /api/challenges/solutions` | Curated solution directions |
| `POST /api/challenges/universities` | Demo university matching |
| `POST /api/challenges/industries` | Demo industry matching |
| `POST /api/challenges` | Persist a challenge |
| `GET /api/challenges/{id}` | Retrieve a persisted challenge |
| `POST /api/solutions` | Persist a solution concept |
| `GET /api/solutions/{id}` | Retrieve a persisted solution |

## Validation

Run frontend checks from `frontend/`:

```powershell
npm run build
npm run lint
```

## Prototype disclaimer

Impact scores are transparent prototype guidance, not scientifically validated predictions. Solution directions are starting points, not final engineering designs. University and industry records are fictional demo data. No authentication, payment, production deployment, or real external collaboration integration is included.
