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
import { mapMutations, mapActions } from 'vuex'
export default {

  computed: {
    search: {
      get() {
        return ''
      },
      set(value) {
        this.$emit('input', { q: value })
      }
    }
  },

  methods: {
    ...mapActions('documents', ['getDocumentList']),
    ...mapMutations('documents', ['setCurrent', 'updateSearchOptions']),
    update() {
      this.updateSearchOptions({
        q: this.search
      })
      this.getDocumentList({
        projectId: this.$route.params.id
      })
      this.setCurrent(0)
      const checkpoint = {}
      checkpoint[this.$route.params.id] = this.page
      localStorage.setItem('checkpoint', JSON.stringify(checkpoint))
    }
  }
}
</script>

<style scoped>

</style>
