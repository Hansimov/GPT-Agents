import { defineStore } from 'pinia';

export const useChatStore = defineStore({
    id: 'chat',
    state: () => ({
        rooms: [],
        roomId: "1" as string,
        messages: [],
        chat_data_json_path: 'src/data/vue_chats.json',
    }),
    actions: {
        async fetchJsonData(json_path: string) {
            const response = await fetch(json_path);
            return await response.json();
        },
        async updateChatData(roomId: string = "x") {
            const chat_data = await this.fetchJsonData(this.chat_data_json_path);
            this.rooms = chat_data.rooms;
            this.messages = chat_data.roomMessages[this.roomId];
            if (roomId != "x") {
                this.roomId = roomId
            }
            console.log(`roomId: ${this.roomId}`)
            return this.messages
        },
        updateNestedDict(target: any, source: any) {
            for (const key of Object.keys(source)) {
                if (typeof source[key] === 'object' && source[key].constructor === Object && key in target) {
                    target[key] = this.updateNestedDict(target[key], source[key]);
                } else {
                    target[key] = source[key];
                }
            }
            return target;
        },
        startPolling() {
            let preChatData: any;

            function isValueChanged(newValue: any) {
                let preValue: any;
                preValue = preChatData;
                if (preValue && (JSON.stringify(newValue) === JSON.stringify(preValue))) {
                    return false;
                } else {
                    preChatData = newValue;
                    return true;
                }
            }

            const poll = async () => {
                const new_chat_data = await this.fetchJsonData(this.chat_data_json_path);

                if (isValueChanged(new_chat_data)) {
                    this.updateChatData();
                }
            }

            setInterval(poll, 500);
        }
    }
});
