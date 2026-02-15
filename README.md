# Live Mood Architect

**A modern, therapeutic affirmation generator built with Vue 3, FastAPI, and Google Gemini AI.**

Live Mood Architect is a full-stack application designed to provide personalized, warm, and supportive affirmations based on a user's name and current emotional state. The interface features a stunning glassmorphism design with fluid animations and a fully functional dark mode.

## � Live Application

- **Frontend URL:** [https://mood-architect-v1.vercel.app/](https://mood-architect-v1.vercel.app/)
- **Backend API:** [https://mood-architect-ru6c.onrender.com](https://mood-architect-ru6c.onrender.com)
- **GitHub Repository:** [https://github.com/Mr-Akhil12/Mood-Architect](https://github.com/Mr-Akhil12/Mood-Architect)

## �🏗 Architecture

The application follows a decoupled client-server architecture:

- **Frontend (Client):** 
  - **Framework:** Vue 3 (Composition API) built with Vite for lightning-fast performance.
  - **Styling:** Tailwind CSS with custom glassmorphism effects and complex animations (`animate-blob`, `animate-shimmer`).
  - **State Management:** Native Vue 3 Reactivity (`ref`, `computed`).
  - **Networking:** Axios for asynchronous API communication.

- **Backend (Server):**
  - **Framework:** FastAPI (Python) for high-performance, asynchronous request handling.
  - **AI Engine:** Google Gemini Pro (`gemini-2.5-flash-lite-preview-09-2025`) via the `google-generativeai` library.
  - **Validation:** Pydantic models ensure strict type checking and input sanitization.
  - **Security:** Environment variable management using `python-dotenv`.

## 📂 Codebase Structure

```bash
root/
├── backend/                  # Python FastAPI Server
│   ├── main.py              # Application entry point, API routes, and Gemini integration
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # (Gitignored) Environment secrets
│
├── frontend/                 # Vue 3 Client Application
│   ├── src/
│   │   ├── App.vue          # Main application component (UI & Logic)
│   │   ├── style.css        # Tailwind directives and custom CSS
│   │   └── main.js          # Vue app initialization
│   ├── tailwind.config.js   # Tailwind configuration (Dark mode, themes)
│   ├── vite.config.js       # Vite build configuration
│   └── package.json         # Node dependencies
│
└── deployment.md             # Comprehensive deployment guide
```

## 🚀 How It Works

1. **User Input:** The user enters their name and current feeling into the glassmorphism interface.
2. **Request Dispatch:** The frontend validates the input and sends a secure POST request to the `/api/affirmation` endpoint via Axios.
3. **API Processing:**
   - FastAPI receives the request and validates it against the `AffirmationRequest` Pydantic model.
   - The server constructs a safe prompt with strict system instructions to prevent harmful output.
4. **AI Generation:** The `gemini-2.5-flash-lite-preview-09-2025` model generates a personalized, empathetic response.
5. **Response Rendering:** The frontend receives the text and displays it with a smooth typewriter animation effect.

## ✨ Key Features

- **Dynamic Theme Switching:** Seamless dark/light mode toggle with persistent local storage preference.
- **Responsive Glassmorphism:** A modern, translucent UI design that adapts to all screen sizes.
- **Fluid Animations:** Background ambient orbs and interactive UI elements enhance the user experience.
- **Robust Error Handling:** graceful degradation with user-friendly error messages if the AI service is unavailable.
- **Safety First:** Strict AI safety settings to prevent the generation of harmful or inappropriate content.

## 🛠 Deployment & Setup

For detailed instructions on how to run this project locally or deploy it to the cloud (Render/Vercel), please refer to [deployment.md](./deployment.md).

## 📋 Submission Checklist

- ✅ **Public GitHub Repository:** [https://github.com/Mr-Akhil12/Mood-Architect](https://github.com/Mr-Akhil12/Mood-Architect)
- ✅ **Live Application URL:** [https://mood-architect-v1.vercel.app/](https://mood-architect-v1.vercel.app/)
- ✅ **Backend API URL:** [https://mood-architect-ru6c.onrender.com](https://mood-architect-ru6c.onrender.com)
- ✅ **Environment Configuration Screenshot:** Render dashboard showing `GEMINI_API_KEY` (value blurred)
- ✅ **Future Improvements:**
  - **Rate Limiting:** Implement user-based rate limiting to prevent API abuse and manage Gemini quota more effectively.
  - **Affirmation History:** Add authentication and a database (PostgreSQL) to save user affirmations and track emotional trends over time.
  - **Advanced Animations:** Implement more sophisticated GSAP-based animations for page transitions and text reveals.
  - **Multi-language Support:** Use i18n to provide affirmations in multiple languages for broader accessibility.
  - **Testing Suite:** Add comprehensive unit tests (Pytest for backend, Vitest for frontend) and E2E tests (Playwright).

---
*Built by Akhil Pillay, 2026*
