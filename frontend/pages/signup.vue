<template>
  <v-app id="inspire">
    <v-content>
      <v-container class="fill-height" fluid>
        <v-row align="center" justify="center">
          <v-col cols="12" sm="8" md="4">
            <sign-up-form :sign-up="signUp" />
          </v-col>
        </v-row>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import { mapActions } from 'vuex'
import SignUpForm from '../components/organisms/auth/SignUpForm'

export default {
  components: {
    SignUpForm
  },

  methods: {
    ...mapActions('auth', ['signUp'])
  }
}
</script>
