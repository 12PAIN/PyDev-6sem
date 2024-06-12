<template>
    <section>
      <h1>Ваш профиль</h1>
      <hr/><br/>
      <div>
        <p><strong>Ф.И.О:</strong> <span>{{ user.full_name }}</span></p>
        <p><strong>Эл. Почта:</strong> <span>{{ user.email }}</span></p>
      </div>
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters } from 'vuex';
  
  export default defineComponent({
    name: 'ProfilePage',
    created: function() {
      return this.$store.dispatch('viewMe');
    },
    computed: {
      ...mapGetters({user: 'stateUser' }),
    },
    methods: {      
    },
  });
  </script>