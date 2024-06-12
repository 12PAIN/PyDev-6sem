<template>
  <section v-if="!!result">
      
    <section>
        <h1>Результат к задаче {{this.$route.params.id}}</h1>
        <hr/><br/>
        <div v-if="result.input_img_code">
            <img  style="max-height: 1000px;" v-bind:src="result.input_img_code">
            <hr/><br/>
        </div>

        <div v-if="result.output_img_code">
            <img  style="max-height: 1000px;" v-bind:src="result.output_img_code">
            <hr/><br/>
        </div>
        
        <div v-for="part in result.parts" :key="part.name">
            <p>Артикул: {{ part.name }}, количество {{ part.pcs }}</p>
        </div>
          
    </section>
      
  </section>
</template>
  
  <script>
  import { defineComponent } from 'vue';
  import { mapGetters } from 'vuex';
  
  export default defineComponent({
    name: 'ResultPage',
    beforeCreate: function() {
      return this.$store.dispatch('getResult', this.$route.params.id);
    },

    computed: {
        ...mapGetters({result: 'stateResult' }),
    }
  });
  </script>