# The 90-Minute "Live Mood Architect" Build Guide (Gemini Edition)

This guide is optimized for speed using AI coding assistants while strictly adhering to the technical challenge requirements.

## Target Architecture

- **Frontend:** Vue 3 + Vite
- **Backend:** FastAPI (Python)
- **AI:** Google Gemini API (Free Tier)
- **Deployment:** Render (Backend) + Vercel (Frontend)

## Phase 1: Project Setup & Git (5 Minutes)

### 1. Create a Folder
```bash
mkdir mood-architect
cd mood-architect
git init
```

### 2. Create Subdirectories
```bash
mkdir backend frontend
```

### 3. Create a `.gitignore` in the root
```plaintext
node_modules/
venv/
__pycache__/
.env
.DS_Store
dist/
```

## Phase 2: The Backend (FastAPI + Gemini) (25 Minutes)

### 1. Setup Environment
```bash
cd backend
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install fastapi uvicorn google-generativeai python-dotenv pydantic
pip freeze > requirements.txt
```

### 2. AI Prompt for Backend Code
Copy/Paste this prompt into your AI tool:

> "Write a Python FastAPI backend (main.py) for a therapeutic affirmation app.
> Requirements:
> 1. Use pydantic for input validation: name and feeling must be non-empty strings.
> 2. Endpoint: POST /api/affirmation.
> 3. Use google-generativeai (Gemini) to generate responses.
> 4. Safety & Prompting: System instructions must ensure: no medical/legal advice, no diagnosis, and no self-harm guidance. If self-harm is mentioned, provide a safe, supportive message and encourage professional help.
> 5. Output: Short (2-4 sentences), warm affirmations specific to the user.
> 6. Error Handling: Return HTTP 400 for validation errors and 502 for Gemini API failures with friendly messages.
> 7. Security: Load GEMINI_API_KEY from os.environ.
> 8. CORS: Configure CORS for the frontend domain."

## Phase 3: Immediate Backend Deployment (15 Minutes)
Deploy now so Render can build while you work on the frontend.

1. **Get Gemini Key:** Get a free API key from Google AI Studio.
2. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Backend with Gemini"
   git push origin main
   ```
3. **Deploy to Render:**
   - **New Web Service** -> Connect Repo.
   - **Root Directory:** `backend`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Env Vars:** Add `GEMINI_API_KEY`. Take your screenshot now (blur the value) for the submission.

## Phase 4: The Frontend (Vue + Vite) (25 Minutes)

### 1. Setup
```bash
cd ../frontend
npm create vite@latest . -- --template vue
npm install axios tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

### 2. AI Prompt for Frontend Code
Copy/Paste this prompt into your AI tool:

> "Create a Vue 3 component using Tailwind CSS.
>
> UI Requirements: Clean, responsive interface with a loading state.
> 1. Inputs: Name and Feeling.
> 2. Button: 'Generate Affirmation'.
> 3. Display: Show the generated affirmation or a friendly error message if the API fails.
> Logic:
> Use axios to POST to YOUR_RENDER_BACKEND_URL/api/affirmation.
>
> Bonus: Implement a typewriter effect so the affirmation text streams in visually."

## Phase 5: Frontend Deployment & Final Checks (20 Minutes)

1. **Deploy to Vercel:**
   - Connect GitHub.
   - Set **Root Directory** to `frontend`.
   - Deploy.

2. **README:** Create a `README.md` including local setup instructions, env var names, and your live URLs.

3. **Final Test:** Open your Vercel URL and generate an affirmation to ensure the "Full-stack wiring" is 100% functional.

## Submission Checklist

- [ ] Public GitHub Repo link.
- [ ] Live Frontend URL (Vercel).
- [ ] Live Backend URL (Render).
- [ ] Screenshot of Render Env Vars (Blurred).
- [ ] README with setup and improvement notes.
