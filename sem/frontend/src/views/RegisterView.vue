<template>
  <section>
    <form @submit.prevent="submit">
      <div class="mb-3">
        <label for="email" class="form-label">Эл. Почта:</label>
        <input type="text" name="email" v-model="user.email" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="full_name" class="form-label">Ф.И.О:</label>
        <input type="text" name="full_name" v-model="user.full_name" class="form-control" />
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Пароль:</label>
        <input type="password" name="password" v-model="user.password" class="form-control" />
      </div>
      <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
    </form>
  </section>
</template>

<script>
import { defineComponent } from 'vue';
import { mapActions } from 'vuex';

export default defineComponent({
  name: 'RegisterPage',
  data() {
    return {
      user: {
        email: '',
        full_name: '',
        password: '',
      },
    };
  },
  methods: {
    ...mapActions(['register']),
    async submit() {
      try {
        await this.register(this.user);
        this.$router.push('/');
      } catch (error) {
        throw 'Account already exists. Please try again.';
      }
    },
  },
});
</script>