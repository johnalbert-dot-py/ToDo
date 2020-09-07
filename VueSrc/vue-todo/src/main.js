import Vue from 'vue'
import App from './App.vue'
import ModalMessages from './ModalMessages.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


let app = new Vue({
  render: h => h(App),
})

let modal_messages = new Vue({
  render: h => h(ModalMessages),
})

app.$mount('#app')
modal_messages.$mount('#modal-messages')


