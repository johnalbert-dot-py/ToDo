<template>
    <div id="modal-messages">
        <template v-if="status != 'close'">
            <modal-message-component :modal_message="message" :modal_sub_message="sub_message" :close_func="modalClose"></modal-message-component>
        </template>
    </div>
</template>

<script>
import ModalMessageComponent from './components/ModalMessages.vue'

export default {
  name: 'ModalMessages',
  components: {
    ModalMessageComponent
  },
  data() {
      return {
        status: "close",
        message: "",
        sub_message: ""
      }
  },
  methods: {
      modalClose(){
          this.status = "close"
      },
      modalOpen(message, sub_message, status){
          this.message = message;
          this.sub_message = sub_message;
          this.status = status;
      }
  }
}
</script>
