<script setup lang="ts">
import { register } from 'vue-advanced-chat'
register()

const currentUserId = '1234'
const rooms = [
  {
    roomId: '1',
    roomName: 'Room X',
    avatar: '/favicon.ico',
    unreadCount: 4,
    index: 3,
    lastMessage: {
      _id: 'xyz',
      content: 'Last message received',
      senderId: '1234',
      username: 'John Doe',
      timestamp: '10:20',
      saved: true,
      distributed: false,
      seen: false,
      new: true
    },
    users: [
      {
        _id: '1234',
        username: 'John Doe',
        avatar: 'assets/imgs/doe.png',
        status: {
          state: 'online',
          lastChanged: 'today, 14:30'
        }
      },
      {
        _id: '4321',
        username: 'John Snow',
        avatar: 'assets/imgs/snow.png',
        status: {
          state: 'offline',
          lastChanged: '14 July, 20:00'
        }
      }
    ],
    typingUsers: [4321]
  }
]

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
    :rooms="JSON.stringify(rooms)"
    :messages="JSON.stringify(messages)"
    :room-actions="JSON.stringify(roomActions)"
    height="100vh"
  />
</template>

<style scope>
.chat-window {
  margin: 0;
}
</style>
