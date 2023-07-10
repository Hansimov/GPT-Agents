<script setup lang="ts">
import { register } from 'vue-advanced-chat'
import { onMounted } from 'vue'
import { useChatStore } from '@/stores/chatStore'

register()

const chatStore = useChatStore()
onMounted(() => {
  chatStore.startPolling()
})

const currentUserId = '1234'
const currentRoomId = 'room1'
const messages = []
const roomActions = [
  { name: 'inviteUser', title: 'Invite User' },
  { name: 'removeUser', title: 'Remove User' },
  { name: 'deleteRoom', title: 'Delete Room' }
]
</script>

<template>
  <vue-advanced-chat
    class="chat-window"
    :current-user-id="currentUserId"
    :rooms="JSON.stringify(chatStore.$state.rooms)"
    :messages="JSON.stringify(messages)"
    :room-actions="JSON.stringify(roomActions)"
    height="99vh"
  />
</template>

<style scope>
.chat-window {
  /* margin:0  2rem; */
  /* padding: 0 1rem; */
}
</style>
