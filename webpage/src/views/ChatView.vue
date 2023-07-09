<script lang="ts">
import { register } from 'vue-advanced-chat'
register()

export default {
  data() {
    return {
      currentUserId: 'Asimov',
      loadFirstRoom: true,
      rooms: [
        // {
        //   _id: 'room1',
        //   name: 'Room 1',
        //   participants: ['user1', 'user2']
        // },
        // {
        //   _id: 'room2',
        //   name: 'Room 2',
        //   participants: ['user1', 'user3']
        // }
      ],
      currentRoomId: 'room1',
      messages: [
        // {
        //   _id: 'message1',
        //   content: 'Hello!',
        //   senderId: 'user1',
        //   roomId: 'room1'
        // }
        // {
        //   _id: 'message2',
        //   content: 'Hi!',
        //   senderId: 'user2',
        //   roomId: 'room1'
        // }
      ],
      participants: [
        // {
        //   _id: 'user1',
        //   username: 'User 1'
        // },
        // {
        //   _id: 'user2',
        //   username: 'User 2'
        // },
        // {
        //   _id: 'user3',
        //   username: 'User 3'
        // }
      ],
      roomActions: [
        { name: 'inviteUser', title: 'Invite User' },
        { name: 'removeUser', title: 'Remove User' },
        { name: 'deleteRoom', title: 'Delete Room' }
      ],
      menuActions: [
        {
          name: 'inviteUser',
          title: 'Invite User'
        },
        {
          name: 'removeUser',
          title: 'Remove User'
        },
        {
          name: 'deleteRoom',
          title: 'Delete Room'
        }
      ],
      messageActions: [
        {
          name: 'replyMessage',
          title: 'Reply'
        },
        {
          name: 'editMessage',
          title: 'Edit Message',
          onlyMe: true
        },
        {
          name: 'deleteMessage',
          title: 'Delete Message',
          onlyMe: true
        },
        {
          name: 'selectMessages',
          title: 'Select'
        }
      ]
    }
  }
}
</script>

<template>
  <vue-advanced-chat
    :rooms="JSON.stringify(rooms)"
    :current-room-id="currentRoomId"
    :messages="JSON.stringify(messages)"
    :participants="participants"
    :room-actions="JSON.stringify(roomActions)"
  />
</template>
