<script setup lang="ts">
import { register } from 'vue-advanced-chat'
import { onMounted } from 'vue'
import { useChatStore } from '@/stores/chatStore'

register()

const chatStore = useChatStore()
onMounted(() => {
  chatStore.startPolling()
})

const currentUserId = '0'
const roomId = '1'
const roomActions = [
  { name: 'inviteUser', title: 'Invite User' },
  { name: 'removeUser', title: 'Remove User' },
  { name: 'deleteRoom', title: 'Delete Room' }
]

function sendMessage(event) {
  console.log('sendMessage:', event.detail)
  const detail = event.detail[0]
  const content = detail.content
  const files = detail.files
  const roomId = detail.roomId
  const replyMessage = detail.replyMessage
  console.log(`You: ${content}`)
}
function fetchMessage(event) {
  console.log('fetchMessage:', event)
}

function sendMessageReaction(event) {
  console.log('sendMessageReaction:', event.detail)
  const detail = event.detail[0]
  const roomId = detail.roomId
  const reaction = detail.reaction.unicode
  const messageId = detail.messageId
  console.log(`You add ${reaction} to message ${messageId}`)
}
</script>

<!--
  Use cases of events api:
  https://github.com/antoine92190/vue-advanced-chat/blob/master/demo/src/ChatContainer.vue#L32-L65
-->
<template>
  <vue-advanced-chat
    class="chat-window"
    :room-id="roomId"
    :current-user-id="currentUserId"
    :rooms="JSON.stringify(chatStore.$state.rooms)"
    :messages="JSON.stringify(chatStore.$state.messages)"
    :room-actions="JSON.stringify(roomActions)"
    rooms-loaded="true"
    messages-loaded="true"
    height="99vh"
    single-room="false"
    @send-message="sendMessage($event)"
    @send-message-reaction="sendMessageReaction($event)"
  />
</template>

<style scope>
.chat-window {
  /* margin:0  2rem; */
  /* padding: 0 1rem; */
}
</style>
