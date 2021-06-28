<template>
  <div class="v-data-footer">
    <v-edit-dialog
      large
      persistent
      @save="changePage"
    >
      <span>{{ page }} of {{ total }}</span>
      <template v-slot:input>
        <div class="mt-4 title">
          Move Page
        </div>
      </template>
      <template v-slot:input>
        <v-text-field
          v-model="newPage"
          :rules="rules"
          label="Edit"
          single-line
          counter
          autofocus
        />
      </template>
    </v-edit-dialog>
    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn
          v-shortkey.once="['arrowleft']"
          :disabled="page===1"
          text
          fab
          small
          v-on="on"
          @shortkey="prevPage"
          @click="prevPage"
        >
          <v-icon>mdi-chevron-left</v-icon>
        </v-btn>
      </template>
      <span>←</span>
    </v-tooltip>
    <v-tooltip bottom>
      <template v-slot:activator="{ on }">
        <v-btn
          v-shortkey.once="['arrowright']"
          :disabled="page===total"
          text
          fab
          small
          v-on="on"
          @shortkey="nextPage(total)"
          @click="nextPage(total)"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </template>
      <span>→</span>
    </v-tooltip>
  </div>
</template>

<script>
import { mapState, mapActions, mapMutations, mapGetters } from 'vuex'

export default {
  data() {
    return {
      editedPage: null,
      rules: [
        value => (value && parseInt(value, 10) > 0 && parseInt(value, 10) <= this.total) || 'Invalid page number!'
      ]
    }
  },

  computed: {
    ...mapState('documents', ['items', 'total']),
    ...mapGetters('pagination', ['current', 'limit', 'offset', 'page']),
    newPage: {
      get() {
        return this.page
      },
      set(newValue) {
        const value = parseInt(newValue, 10)
        this.editedPage = value
      }
    }
  },

  watch: {
    offset() {
      this.updateSearchOptions({
        limit: this.limit,
        offset: this.offset
      })
      this.getDocumentList({
        projectId: this.$route.params.id
      })
    },
    current() {
      this.setCurrent(this.current)
    }
  },

  created() {
    this.initPage({
      projectId: this.$route.params.id
    })
    this.getDocumentList({
      projectId: this.$route.params.id
    })
  },

  methods: {
    ...mapActions('documents', ['getDocumentList']),
    ...mapActions('pagination', ['prevPage', 'nextPage', 'initPage', 'movePage']),
    ...mapMutations('documents', ['setCurrent', 'updateSearchOptions']),
    changePage() {
      if (!this.editedPage || this.editedPage < 0 || this.editedPage > this.total) {
        return
      }
      this.movePage(this.editedPage)
    }
  }
}
</script>
