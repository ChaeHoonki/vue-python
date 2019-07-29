<template>
  <div>
    <p>{{ msg }}</p>
    <v-btn @click= "test()" >login</v-btn>
    <v-card>123 {{loginRes}}</v-card>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data () {
    return {
      msg: '',
      loginRes: ''
    }
  },
  methods: {
    test () {
      const path = 'http://localhost:5000/login'
      axios.get(path)
        .then((res) => {
          this.loginRes = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    getMessage () {
      const path = 'http://localhost:5000/ping'
      axios.get(path)
        .then((res) => {
          this.msg = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    }
  },
  created () {
    this.getMessage()
  }
}
</script>
