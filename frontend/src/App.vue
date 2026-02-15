<script setup>
import { ref, onMounted, watch } from 'vue'
import axios from 'axios'

const name = ref('')
const feeling = ref('')
const affirmation = ref('')
const displayedAffirmation = ref('')
const error = ref('')
const loading = ref(false)
const isDark = ref(false)

// Use VITE_API_URL if set, otherwise default to localhost
const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api/affirmation'

onMounted(() => {
  // Check system preference or localStorage
  if (localStorage.theme === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    isDark.value = true
    document.documentElement.classList.add('dark')
  } else {
    isDark.value = false
    document.documentElement.classList.remove('dark')
  }
})

const toggleTheme = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    localStorage.theme = 'dark'
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.theme = 'light'
  }
}

const generateAffirmation = async () => {
  if (!name.value.trim() || !feeling.value.trim()) {
    error.value = "Please share both your name and how you're feeling."
    return
  }
  
  loading.value = true
  error.value = ''
  affirmation.value = ''
  displayedAffirmation.value = ''
  
  try {
    const response = await axios.post(API_URL, {
      name: name.value,
      feeling: feeling.value
    })
    
    // Start typewriter effect
    const text = response.data.affirmation
    affirmation.value = text
    typeWriter(text)
    
  } catch (err) {
    console.error(err)
    if (err.response && err.response.data && err.response.data.detail) {
        error.value = err.response.data.detail
    } else {
        error.value = "The spirits are quiet right now. Please try again in a moment."
    }
  } finally {
    loading.value = false
  }
}

const typeWriter = (text) => {
  let i = 0
  displayedAffirmation.value = ''
  const speed = 40 
  
  const type = () => {
    if (i < text.length) {
      displayedAffirmation.value += text.charAt(i)
      i++
      setTimeout(type, speed)
    }
  }
  type()
}
</script>

<template>
  <div class="min-h-screen w-full relative overflow-hidden bg-slate-50 dark:bg-slate-900 flex flex-col font-sans transition-colors duration-500">
    
    <!-- Top Bar -->
    <header class="w-full p-6 flex justify-end z-20 relative">
      <button 
        @click="toggleTheme" 
        class="p-2 rounded-full bg-white/50 dark:bg-slate-800/50 backdrop-blur-sm border border-slate-200 dark:border-slate-700 shadow-sm hover:scale-105 transition-transform duration-200 text-slate-800 dark:text-yellow-300"
        aria-label="Toggle Dark Mode"
      >
        <!-- Sun Icon -->
        <svg v-if="!isDark" xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
        </svg>
        <!-- Moon Icon -->
        <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
        </svg>
      </button>
    </header>

    <!-- Animated Decoration Blobs -->
    <div class="absolute top-[-10%] left-[-10%] w-96 h-96 bg-purple-400/60 dark:bg-purple-600/50 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl opacity-70 animate-blob"></div>
    <div class="absolute top-[-10%] right-[-10%] w-96 h-96 bg-yellow-400/60 dark:bg-yellow-600/50 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl opacity-70 animate-blob animation-delay-2000"></div>
    <div class="absolute -bottom-32 left-20 w-96 h-96 bg-pink-400/60 dark:bg-pink-600/50 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl opacity-70 animate-blob animation-delay-4000"></div>
    
    <!-- New Blobs -->
    <div class="absolute top-[40%] right-[30%] w-72 h-72 bg-blue-400/60 dark:bg-blue-600/50 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl opacity-70 animate-blob animation-delay-6000"></div>
    <div class="absolute bottom-10 right-10 w-80 h-80 bg-green-400/60 dark:bg-green-600/50 rounded-full mix-blend-multiply dark:mix-blend-screen filter blur-3xl opacity-70 animate-blob animation-delay-8000"></div>

    <main class="flex-grow flex items-center justify-center p-4 sm:p-6 lg:p-8 relative z-10">
      <div class="relative w-full max-w-lg">
        <!-- Main Card -->
        <div class="backdrop-blur-xl bg-white/70 dark:bg-slate-800/60 border border-white/50 dark:border-slate-700/50 shadow-2xl rounded-3xl overflow-hidden transition-all duration-300 hover:shadow-purple-500/10">
          
          <!-- Header Section -->
          <div class="bg-gradient-to-r from-violet-600 to-indigo-600 p-8 text-center relative overflow-hidden">
            <div class="absolute inset-0 bg-white/10 opacity-20"></div>
            <h1 class="relative text-4xl font-extrabold text-white tracking-tight mb-2 font-display drop-shadow-sm">
              Mood Architect
            </h1>
            <p class="relative text-indigo-100 text-sm font-medium opacity-90">
              Design your mindset, one thought at a time.
            </p>
          </div>

          <div class="p-8 space-y-8">
            
            <!-- Inputs Group -->
            <div class="space-y-6">
              <div class="group">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2 ml-1 transition-colors group-focus-within:text-violet-600 dark:group-focus-within:text-violet-400">
                  What should we call you?
                </label>
                <input 
                  v-model="name"
                  type="text" 
                  class="w-full px-5 py-3 bg-slate-50 dark:bg-slate-900/50 border-2 border-slate-100 dark:border-slate-700 rounded-xl text-slate-700 dark:text-slate-200 placeholder-slate-400 focus:bg-white dark:focus:bg-slate-900 focus:border-violet-500 dark:focus:border-violet-500 focus:ring-4 focus:ring-violet-500/10 outline-none transition-all duration-300 shadow-sm"
                  placeholder="Your name"
                  @keyup.enter="$refs.feelingInput.focus()"
                />
              </div>
              
              <div class="group">
                <label class="block text-sm font-semibold text-slate-700 dark:text-slate-300 mb-2 ml-1 transition-colors group-focus-within:text-violet-600 dark:group-focus-within:text-violet-400">
                  How are you feeling right now?
                </label>
                <textarea 
                  ref="feelingInput"
                  v-model="feeling"
                  rows="3"
                  class="w-full px-5 py-3 bg-slate-50 dark:bg-slate-900/50 border-2 border-slate-100 dark:border-slate-700 rounded-xl text-slate-700 dark:text-slate-200 placeholder-slate-400 focus:bg-white dark:focus:bg-slate-900 focus:border-violet-500 dark:focus:border-violet-500 focus:ring-4 focus:ring-violet-500/10 outline-none transition-all duration-300 shadow-sm resize-none"
                  placeholder="I'm feeling..."
                  @keyup.enter.ctrl="generateAffirmation"
                ></textarea>
              </div>
            </div>

            <!-- Action Button -->
            <button 
              @click="generateAffirmation" 
              :disabled="loading"
              class="w-full group relative overflow-hidden bg-violet-600 hover:bg-violet-700 text-white font-bold py-4 rounded-xl shadow-lg hover:shadow-violet-500/30 transition-all duration-300 transform hover:-translate-y-0.5 active:translate-y-0 disabled:opacity-70 disabled:cursor-not-allowed disabled:transform-none"
            >
              <div class="absolute inset-0 w-full h-full bg-gradient-to-r from-transparent via-white/20 to-transparent -translate-x-full group-hover:animate-shimmer" v-if="!loading"></div>
              <span class="relative flex items-center justify-center gap-2 text-lg">
                <span v-if="loading" class="animate-spin text-xl">✨</span>
                {{ loading ? 'Consulting the Universe...' : 'Generate Affirmation' }}
              </span>
            </button>

            <!-- Error Message -->
            <div v-if="error" class="animate-fade-in p-4 bg-red-50 dark:bg-red-900/20 text-red-600 dark:text-red-400 rounded-xl text-sm text-center border border-red-100 dark:border-red-900/30 flex items-center justify-center gap-2 shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 flex-shrink-0" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd" /></svg>
              {{ error }}
            </div>

            <!-- Result Card -->
            <div v-if="displayedAffirmation" class="animate-fade-in-up mt-8">
              <div class="relative bg-gradient-to-br from-indigo-50 to-purple-50 dark:from-indigo-900/30 dark:to-purple-900/30 rounded-2xl p-8 border border-indigo-100/50 dark:border-indigo-700/30 shadow-inner">
                <div class="absolute -top-3 -left-3 text-5xl text-indigo-200 dark:text-indigo-700 font-serif opacity-50">❝</div>
                <p class="text-slate-700 dark:text-slate-200 text-lg sm:text-xl leading-relaxed font-medium text-center font-serif italic relative z-10 drop-shadow-sm">
                  {{ displayedAffirmation }}
                </p>
                <div class="absolute -bottom-6 -right-3 text-5xl text-indigo-200 dark:text-indigo-700 font-serif rotate-180 opacity-50">❝</div>
              </div>
              <div class="text-center mt-6 animate-pulse">
                 <span class="text-xs text-slate-400 dark:text-slate-500 uppercase tracking-widest font-bold">For {{ name }}</span>
              </div>
            </div>

          </div>
        </div>
      </div>
    </main>
    
    <!-- Footer -->
    <footer class="w-full p-6 text-center z-20 relative">
      <p class="text-slate-400 dark:text-slate-500 text-xs opacity-70 hover:opacity-100 transition-opacity">
        Built by Akhil Pillay 2026, as a technical assessment for Marisa Peer
      </p>
    </footer>

  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

.font-sans {
  font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
}

.font-serif {
  font-family: 'Playfair Display', serif;
}

/* Animations */
@keyframes blob {
  0% { transform: translate(0px, 0px) scale(1); }
  33% { transform: translate(30px, -50px) scale(1.1); }
  66% { transform: translate(-20px, 20px) scale(0.9); }
  100% { transform: translate(0px, 0px) scale(1); }
}

.animate-blob {
  animation: blob 10s infinite;
}

.animation-delay-2000 {
  animation-delay: 2s;
}

.animation-delay-4000 {
  animation-delay: 4s;
}

.animation-delay-6000 {
  animation-delay: 6s;
}

.animation-delay-8000 {
  animation-delay: 8s;
}

@keyframes shimmer {
  100% { transform: translateX(100%); }
}

.animate-shimmer {
  animation: shimmer 2s infinite;
}

.animate-fade-in {
  animation: fadeIn 0.4s ease-out;
}

.animate-fade-in-up {
  animation: fadeInUp 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
