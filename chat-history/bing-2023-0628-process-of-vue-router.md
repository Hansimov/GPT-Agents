## Explain the process of router of vue3 which served by Vite.

Vue 3 is a JavaScript framework for building user interfaces, and Vite is a frontend tooling that provides faster and leaner development for modern web projects. Vue Router is the official router for Vue.js, which allows you to map components to different routes and navigate between them.
To use Vue Router with a Vue 3 project served by Vite, you need to follow these steps:
 - Install Vue Router by running `npm install vue-router@next` or `yarn add vue-router@next`.
 - Create a `router` directory inside the src directory of your project, and create an index.js file inside the `router` directory.
 - In the `index.js` file, import Vue Router, define your routes, and create a new Vue Router instance.
 - In your `main.js` file, import the Vue Router instance and pass it to your Vue app using the `app.use()` method.
 - Add a `<router-view>` component to your app where you want to display the routed components.

Here is an example that shows how to set up Vue Router with a Vue 3 project served by Vite:

```js
// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/about',
    component: () => import('../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

// src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

createApp(App).use(router).mount('#app')
```

This sets up Vue Router with two routes, `/` and `/about`, which are mapped to the `Home.vue` and `About.vue` components respectively. When you navigate between these routes, the `<router-view>` component will update to display the corresponding component.

## 1st, what is the relationships of the .ts file and .vue file in Vue3 project?
**2nd, how to communicate through these two file types?**

In a Vue 3 project, `.ts` files are TypeScript files, while `.vue` files are Single File Components (SFCs). TypeScript is a typed superset of JavaScript that compiles to plain JavaScript, and it can be used to write Vue components and other parts of a Vue application. SFCs are a special file format for Vue components that allows you to define the template, script, and styles for a component in a single file.

To communicate between .ts and .vue files in a Vue 3 project, you can use the standard module import/export syntax. For example, you can define a component in a .vue file and then import it into a .ts file to use it in your application.

Here is an example that shows how to define a component in a .vue file and then import it into a .ts file:

```vue
// MyComponent.vue
<template>
  <div>{{ message }}</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'MyComponent',
  data() {
    return {
      message: 'Hello from MyComponent!'
    }
  }
})
</script>
```

```ts
// main.ts
import { createApp } from 'vue'
import App from './App.vue'
import MyComponent from './MyComponent.vue'

const app = createApp(App)
app.component('my-component', MyComponent)
app.mount('#app')
```

In this example, we define a `MyComponent` component in the` MyComponent.vue` file, and then import it into the `main.ts` file. We register the `MyComponent` component with the Vue app using the `app.component()` method, which allows us to use the `<my-component>` custom element in our templates.


## Then when to use .ts, when to use .vue?

In a Vue 3 project, you would typically use `.vue` files to define your Vue components using the Single File Component (SFC) format. This allows you to define the template, script, and styles for a component in a single, easy-to-read file. You can also use TypeScript in your `.vue` files by adding the `lang="ts"` attribute to the `<script>` tag.

On the other hand, you would use `.ts` files to write TypeScript code that is not specific to a single Vue component. For example, you might use `.ts` files to define utility functions, store modules, or other parts of your application that are not tied to a specific component.

In general, you would use `.vue` files to define your Vue components and `.ts` files to write other TypeScript code in your Vue 3 project. However, this is not a strict rule and you can organize your code in whatever way makes the most sense for your project.