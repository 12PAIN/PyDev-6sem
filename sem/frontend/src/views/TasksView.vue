<template>
    <section>
      <h1>Ваши загрузки</h1>
      <hr/><br/>
      <div v-for="task in tasks" :key="task.id">
        <p>№ {{ task.id }} Статус: {{ getStatusTitle(task.status) }}  <a style=":hover {outline: thin red solid}" v-on:click="this.$router.push('/results/' + task.id)">Посмотреть результат</a></p>
      </div>
    </section>
</template>
  
<script>
  import { defineComponent } from 'vue';
  import { mapGetters } from 'vuex';
  
  export default defineComponent({
    name: 'TasksPage',
    created: function() {
      return this.$store.dispatch('getTasks');
    },
    computed: {
      ...mapGetters({tasks: 'stateTasks' }),
    },
    methods: {
        getStatusTitle: function(status){
            
            if(status == "FINISHED") return "Завершена" 
            if(status == "WAITING") return "Ожидание"
            if(status == "AT_WORK") return "Обрабатывается"
        }     
    },
  });
</script>