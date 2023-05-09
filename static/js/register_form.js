export default {
    computed: {
      state() {
        return this.name.length >= 8
      },
      invalidFeedback() {
        if (this.name.length > 0) {
          return 'Enter at least 8 characters.'
        }
      }
    },
    data() {
      return {
        name: ''
      }
    }
  }