const modal_messages = new Vue({
    el: "#modal-messages",
    data: {
        status: "close",
        main_message: "",
        sub_message: ""
    },
    methods: {
        modalClose: function(){
            this.status = "close"
        },
        modalOpen: function(status, message, sub_message){
            this.status = status;
            this.main_message = message;
            this.sub_message = sub_message;
        }
    }
})


const app = new Vue({
    el: "#app",
    data: {
        tasks: [
            {name: "Eat Lunch Today", time: "12:00", shift: "AM", description: "Eat your lunch and don't forget to turn off the TV."},
            {name: "Eat Lunch Today", time: "7:00", shift: "PM", description: "Eat your lunch and don't forget to turn on the TV."}
        ]
    },
    methods: {
        todaysDate: () => {
            const date = new Date();
            const month = date.toLocaleString('default', { month: 'long' });
            return `${month} ${date.getUTCDate()}, ${date.getUTCFullYear()}`
        }
    }
})
