import axios from 'axios';

const state = {
    tasks: null,
    task: null
};
  

const getters = {
    stateTasks: state => state.tasks,
    stateTask: state => state.task,
};


const actions = {
    async createTask({dispatch}, task) {


        await axios.post('tasks', task,
        {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        });

        await dispatch('getTasks');
    },
    async getTasks({commit}) {
        let {data} = await axios.get('tasks');
        commit('setTasks', data);
    },
    async viewTask({commit}, id) {
        let {data} = await axios.get(`task/${id}`);
        commit('setTask', data);
    },
};

const mutations = {
    setTasks(state, tasks){
        state.tasks = tasks;
    },
    setTask(state, task){
        state.task = task;
    },
};

export default {
    state,
    getters,
    actions,
    mutations
};