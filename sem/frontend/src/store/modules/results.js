import axios from 'axios';

const state = {
    result: null
};
  
const getters = {
    stateResult: state => state.result,
};

const actions = {
    async getResult({commit}, task_id) {
        let {data} = await axios.get(`results/${task_id}`);
        commit('setResult', data);
    },
};

const mutations = {

    setResult(state, result){
        state.result = result;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};