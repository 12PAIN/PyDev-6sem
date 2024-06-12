<template>
  <div id="app">
    <NavBar />
    <div class="main container">
      <router-view/>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import NavBar from '@/components/NavBar.vue'
import { mapActions } from 'vuex';

export default {
  components: {
    NavBar
  },
  methods: {
    ...mapActions(['checkToken']),
  },
  created: async function(){
    await this.checkToken();

    if (this.$store.getters.isAuthenticated == false) this.$router.push("/login");
    
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}
.main {
  padding-top: 5em;
}
</style>