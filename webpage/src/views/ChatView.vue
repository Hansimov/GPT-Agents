<script>
import { register } from 'vue-advanced-chat'
register()

export default {
  // https://github.com/antoine92190/vue-advanced-chat#rooms-prop
  data() {
    return {
      currentUserId: '1234',
      rooms: [
        {
          roomId: '1',
          roomName: 'Room 1',
          avatar: 'public/favicon.ico',
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
      ],
      currentRoomId: 'room1',
      messages: [],
      roomActions: [
        { name: 'inviteUser', title: 'Invite User' },
        { name: 'removeUser', title: 'Remove User' },
        { name: 'deleteRoom', title: 'Delete Room' }
      ]
    }
  }
}
</script>

<template>
  <vue-advanced-chat
    class="chat-window"
    :current-user-id="currentUserId"
    :rooms="JSON.stringify(rooms)"
    :messages="JSON.stringify(messages)"
    :room-actions="JSON.stringify(roomActions)"
  />
</template>

<style>
.chat-window {
  height: 100vh;
}
</style>
