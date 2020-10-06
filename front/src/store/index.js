import Vue from 'vue'
import Vuex from 'vuex'

const TOKEN_KEY = 'user-token'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: localStorage.getItem(TOKEN_KEY) || null,
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
    }
  },
  actions: {
    updateToken({ commit }, val){
        commit('UPDATE_TOKEN', val) ;
    }
  },
  modules: {
  }
})
