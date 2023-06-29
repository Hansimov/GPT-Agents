import { defineConfigs } from 'v-network-graph';

const configs = {
    node: {
        normal: {
            type: 'circle',
            radius: 25,
            color: '#99ccff'
        },
        hover: {
            color: '#88bbff'
        },
        label: {
            visible: true,
            fontSize: 12
        },
        selectable: true
    },
    edge: {
        gap: 12,
        normal: {
            color: '#6699cc'
        }
    },
    path: {
        visible: true,
        normal: {
            width: 12,
            dasharray: '40 16',
            animate: true,
            animationSpeed: 100
        }
    }
}

const graphConfigs = defineConfigs(configs);
export default {
    graphConfigs
}