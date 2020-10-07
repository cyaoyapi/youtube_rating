import Vue from 'vue'
import Vuex from 'vuex'

const TOKEN_KEY = 'user-token'
const USERNAME = 'username'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem(TOKEN_KEY) || null,
    username: localStorage.getItem(USERNAME) || null,
  },
  getters: {
    axiosConfig: state => {
      return {
        headers: {
          'Authorization': 'Token ' + state.token 
      }
    }
  }
  },
  mutations: {
    UPDATE_TOKEN(state, val){
      state.token = val ;
    },
    SET_USERNAME(state, val){
      state.username = val ;
    }
  },
  actions: {
    updateToken({ commit }, val){
        commit('UPDATE_TOKEN', val) ;
    },
    setUsername({ commit }, val){
      commit('SET_USERNAME', val) ;
  }
  },
  modules: {
  }
})
