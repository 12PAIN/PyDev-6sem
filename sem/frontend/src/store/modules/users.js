import axios from 'axios';


const state = {
  user: null,
};

const getters = {
  isAuthenticated: state => !!state.user,
  stateUser: state => state.user,
};

const actions = {
  async register({dispatch}, form) {
    await axios.post('signup', form);

    let UserForm = new FormData();

    UserForm.append('username', form.email);
    UserForm.append('password', form.password);

    await dispatch('logIn', UserForm);
  },

  async logIn({dispatch}, user) {
    user.append('grant_type', "password");
    await axios.post('login', user).then(function (response) {
      window.localStorage.setItem("ACCESS_TOKEN", response.data.access_token)
    });
    
    await dispatch('viewMe');
  },

  async viewMe({commit}) {

    let {data} = await axios.get(`users/me`, {
      withCredentials: true,
      credentials: 'include'
    });

    window.localStorage.setItem("USER_DATA", data)
    await commit('setUser', data);
  },

  async logOut({commit}) {
    let user = null;
    commit('logout', user);

  },

  async checkToken({commit}) {

    let user_Data = window.localStorage.getItem("USER_DATA")
    let token = window.localStorage.getItem("ACCESS_TOKEN") 
    if (user_Data != undefined && token != undefined && user_Data != null && token != null ){


      let responseData = null

      await axios.get(`users/me`, {
        withCredentials: true,
        credentials: 'include'
      }).then( response => {
        if (response.status == 200 && response.data != null && response.data != undefined) responseData = response.data
      }).catch(function () {});
      
      if (responseData != null) {
        commit('setUser', responseData);
      }
      else {
        commit('logout', null);
      }
    }else{
      commit('logout', null);
    }
  },

};

const mutations = {
  setUser(state, user) {
    window.localStorage.setItem("ACCESS_TOKEN", user)
    state.user = user;
  },
  logout(state, user){
    window.localStorage.removeItem("USER_DATA")
    window.localStorage.removeItem("ACCESS_TOKEN")
    state.user = user;
  },
};

export default {
  state,
  getters,
  actions,
  mutations
};