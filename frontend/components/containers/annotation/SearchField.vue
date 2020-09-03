<template>
  <v-text-field
    v-model="search"
    prepend-inner-icon="search"
    label="Search"
    single-line
    hide-details
    class="pa-0 pl-2"
  />
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: '',
      required: true
    }
  },

  computed: {
    search: {
      get() {
        return ''
      },
      set(value) {
        this.$emit('input', JSON.stringify({ q: value }))
      }
    }
  }
}
</script>

<style scoped>

</style>
