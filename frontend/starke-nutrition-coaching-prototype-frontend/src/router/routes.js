const routes = [
  {
    path: '/coach',
    component: () => import('layouts/coach-view-layout.vue'),
    children: [
      { path: '', component: () => import('pages/CoachView.vue') }  // You should use '' for the root path
    ]
  },
  {
    path: '/trainee',
    component: () => import('layouts/trainee-view-layout.vue'),
    children: [
      { path: '', component: () => import('pages/TraineeView.vue') }
    ]
  },
  {
    path: '/:catchAll(.*)*',  // This is the catch-all route for any unmatched URLs
    component: () => import('pages/ErrorNotFound.vue')
  }
]

export default routes
