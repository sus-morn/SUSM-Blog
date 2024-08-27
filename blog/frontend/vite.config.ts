import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
  ],
  server: {
    proxy: {
      // 将 /api 代理到 FastAPI 后端
      '/api': {
        target: 'http://localhost:8000', // FastAPI 后端地址
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, '') // 可选：如果需要的话，重写请求路径
      }
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
