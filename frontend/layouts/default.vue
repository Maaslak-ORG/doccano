<template>
  <v-app>
    <the-header />
    <nuxt />
    <the-footer />
    <notifications group="top" position="top center" />
    <notifications group="default" position="right bottom" />
  </v-app>
</template>

<script>
import TheFooter from '@/components/organisms/layout/TheFooter'
import TheHeader from '@/components/organisms/layout/TheHeader'

export default {
  middleware: ['check-auth'],
  components: {
    TheFooter,
    TheHeader
  }
}
</script>
