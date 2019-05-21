import Vue from 'vue';
import Router from 'vue-router';
import Ping from '@/components/Ping';
import Tasks from '@/components/Tasks';
import Home from '@/components/Home';
import NotFound from '@/components/error-pages/NotFound';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
    {
      path: '/tasks',
      name: 'Tasks',
      component: Tasks,
    },
    {
      path: '*',
      name: 'NotFound',
      component: NotFound,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
  mode: 'history',
});
