# Deployment Guide

This guide covers how to set up **Live Mood Architect** locally for development and how to deploy it to the cloud for production.

---

## 💻 Local Development Setup

Follow these steps to run the application on your local machine.

### Prerequisites
- **Git**
- **Python 3.9+**
- **Node.js 16+** & **npm**
- A **Google Gemini API Key** (Get one from [Google AI Studio](https://aistudio.google.com/))

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/mood-architect.git
cd mood-architect
```

### 2. Backend Setup (FastAPI)
Open a terminal and navigate to the backend folder:
```bash
cd backend
```

Create a virtual environment:
```bash
# macOS/Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Configure Environment Variables:
1. Create a file named `.env` in the `backend/` directory.
2. Add your API key:
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

Start the Server:
```bash
uvicorn main:app --reload
```
*The backend will start at `http://localhost:8000`.*

### 3. Frontend Setup (Vue 3 + Vite)
Open a **new** terminal window (keep the backend running) and navigate to the frontend folder:
```bash
cd frontend
```

Install dependencies:
```bash
npm install
```

Start the Development Server:
```bash
npm run dev
```
*The frontend will start at `http://localhost:5173`.*

Visit `http://localhost:5173` in your browser to use the app.

---

## ☁️ Cloud Deployment

We will deploy the backend to **Render** and the frontend to **Vercel**.

### Part 1: Deploy Backend to Render

1. Push your code to a GitHub repository.
2. Sign up/Log in to [Render](https://render.com/).
3. Click **New +** -> **Web Service**.
4. Connect your GitHub repository.
5. **Configure the Service:**
   - **Root Directory:** `backend`
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
6. **Environment Variables:**
   - Scroll down to "Environment Variables".
   - Key: `GEMINI_API_KEY`
   - Value: `your_gemini_api_key`
7. Click **Create Web Service**.
8. Once deployed, copy your backend URL (e.g., `https://mood-architect.onrender.com`).

### Part 2: Deploy Frontend to Vercel

1. Sign up/Log in to [Vercel](https://vercel.com/).
2. Click **Add New...** -> **Project**.
3. Import your GitHub repository.
4. **Configure Project:**
   - **Framework Preset:** Vite (should be auto-detected).
   - **Root Directory:** Click "Edit" and select `frontend`.
5. **Environment Variables:**
   - Expand "Environment Variables".
   - Key: `VITE_API_URL`
   - Value: `https://your-render-url.onrender.com/api/affirmation`
   *(Replace with your actual Render URL from Part 1, and ensure you keep /api/affirmation path if your frontend code expects it, OR just the base URL if your code appends the path)*
   *Note: In our code, `App.vue` uses `import.meta.env.VITE_API_URL`.*
6. Click **Deploy**.

### Verification
Once both are deployed, open your Vercel URL.
- Enter a name and feeling.
- Click "Generate Affirmation".
- If it works, your full-stack app is live!

---

### Troubleshooting

- **CORS Errors:** If the frontend cannot talk to the backend, check `main.py`. The `allow_origins=["*"]` setting currently allows all domains. For better security in production, replace `"*"` with your specific Vercel domain.
- **502 Bad Gateway:** This often means the backend crashed or the API key is missing. Check Render logs.
