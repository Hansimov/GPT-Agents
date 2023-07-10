import { createRouter, createWebHistory } from 'vue-router'
import AgentsView from '@/views/AgentsView.vue'
import ChatView from '@/views/ChatView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/agents',
      name: 'agents',
      component: AgentsView
    },
    {
      path: '/chat',
      name: 'chat',
      component: ChatView
    }
  ]
})

export default router
