<template>
  <base-card
    :disabled="!valid"
    title="Sign up"
    agree-text="Sign up"
    @agree="trySignUp"
  >
    <template #content>
      <v-form
        ref="form"
        v-model="valid"
      >
        <v-alert
          v-show="errorMessage"
          v-model="errorMessage"
          type="error"
          dismissible
        >
          {{ errorMessage }}
        </v-alert>
        <v-text-field
          v-model="username"
          :rules="userNameRules"
          label="Username"
          name="username"
          prepend-icon="person"
          type="text"
          autofocus-l
          @keyup.enter="trySignUp"
        />
        <v-text-field
          id="password"
          v-model="password"
          :rules="passwordRules"
          label="Password"
          name="password"
          prepend-icon="lock"
          type="password"
          @keyup.enter="trySignUp"
        />
        <v-text-field
          id="confirmPassword"
          v-model="confirmPassword"
          :rules="passwordRules.concat([checkSamePassword])"
          label="Confirm password"
          name="confirmPassword"
          prepend-icon="lock"
          type="password"
          @keyup.enter="trySignUp"
        />
      </v-form>
    </template>
  </base-card>
</template>

<script>
import { userNameRules, passwordRules } from '../../../rules'
import BaseCard from '../../molecules/BaseCard'

export default {
  components: { BaseCard },

  props: {
    signUp: {
      type: Function,
      default: () => {}
    }
  },

  data() {
    return {
      valid: false,
      username: '',
      password: '',
      confirmPassword: '',
      userNameRules,
      passwordRules,
      errorMessage: ''
    }
  },
  methods: {
    validate() {
      return this.$refs.form.validate()
    },
    trySignUp() {
      console.log(this.$notify)

      if (this.validate()) {
        this.signUp({
          username: this.username,
          password: this.password,
          password_confirm: this.confirmPassword
        })
          .then((result) => {
            this.$notify({
              group: 'top',
              type: 'success',
              title: 'Success',
              text: 'Account succesfully created'
            })
            this.$router.push('/auth')
          })
          .catch((err) => {
            this.errorMessage = Object.values(err.response.data).map((arr) => {
              return arr.join(' ')
            }).join(' ')
          })
      }
    },
    checkSamePassword(val) {
      return val === this.password || 'Password match is required'
    }
  }
}
</script>
