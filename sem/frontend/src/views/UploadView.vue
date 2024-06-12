<template>
    <section>
      
      <section>
      <h1>Загрузить новую фотографию</h1>
      <hr/><br/>

      <form @submit.prevent="submit">
        <div class="mb-3">
          <input type="file" accept=".jpg, .png, .jpeg" name="title" id="file" ref="file" class="form-control" v-on:change="handleFileUpload()" />
        </div>
        <button type="submit" class="btn btn-primary">Загрузить</button>
      </form>
    </section>
      
    </section>
  </template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters, mapActions } from 'vuex';
  
  export default defineComponent({
    name: 'UploadPage',
    data(){
      return {
        file: ''
      }
    },
    computed: {
      ...mapGetters({user: 'stateUser' }),
    },
    methods: {
      ...mapActions(['createTask']),
      handleFileUpload(){
        this.file = this.$refs.file.files[0];
      },

      async submit() {
        let formData = new FormData();
        formData.append('file', this.file);
        
        await this.createTask(formData);
        this.$router.push('/tasks')
      },
    },
  });
  </script>