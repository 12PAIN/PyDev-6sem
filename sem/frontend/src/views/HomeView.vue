<template>
  <section>
    <p>Добро пожаловать в определитель деталей лего!</p>

    <div v-if="isLoggedIn" id="logout">
      <p id="logout">Вы вошли в аккаунт!</p>
    </div>
    <p v-else>
      <span><a href="/register">Зарегистрироваться</a></span>
      <span> или </span>
      <span><a href="/login">Войти</a></span>
    </p>
  </section>
</template>
<script>

import { defineComponent } from 'vue';


export default defineComponent({
  name: 'HomeView',
  
  computed : {
    isLoggedIn: function() {
      return this.$store.getters.isAuthenticated;
    }
  },
});
</script>