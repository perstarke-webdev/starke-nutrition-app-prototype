
const routes = [
  {
    path: '/coach',
    component: () => import('layouts/CoachViewLayout.vue'),
    children: [
      { path: '', component: () => import('pages/CoachView.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
