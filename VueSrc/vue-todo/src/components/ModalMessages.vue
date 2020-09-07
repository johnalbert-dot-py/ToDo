<template>
  <div class="overlay">
      <div class="card card-messages">
          <div class="card-messages-header text-center">
              <span class="status-success">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
                      <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-1.25
                      17.292l-4.5-4.364 1.857-1.858 2.643 2.506 5.643-5.784 1.857 1.857-7.5 7.643z"/>
                  </svg>
              </span>
              <a href="#" v-on:click="closeModal()" class="close">&times;</a>

              <!-- <span class="status-error">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                      <path d="M12 0c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm4.151
                      17.943l-4.143-4.102-4.117 4.159-1.833-1.833 4.104-4.157-4.162-4.119 1.833-1.833 4.155 4.102
                      4.106-4.16 1.849 1.849-4.1 4.141 4.157 4.104-1.849 1.849z"/></svg>
              </span> -->
          </div>
          <div class="card-messages-body">
              <h3 class='card-title text-center'>
                  {{ modal_message }}
              </h3>

              <p class="message-description text-center">
                  {{ modal_sub_message }}
              </p>
          </div>
      </div>
  </div>
</template>

<script>
export default {
  name: 'ModalMessageComponent',
  props: {
    modal_message: String,
    modal_sub_message: String,
    close_func: Function,
  },
  methods: {
    closeModal(){
      this.close_func()
    }
  }
}
</script>