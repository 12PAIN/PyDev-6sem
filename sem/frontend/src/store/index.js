import { createStore } from "vuex";

import tasks from './modules/tasks';
import users from './modules/users';
import results from './modules/results';

export default createStore({
  modules: {
    users,
    tasks,
    results,
  }
});