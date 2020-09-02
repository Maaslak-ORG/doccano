<template>
  <v-data-table
    :items="items"
    :headers="headers"
    hide-default-footer
    hide-default-header
    class="elevation-1"
    caption="Labels cheat sheet"
  />
</template>

<script>
export default {
  name: 'LabelBox',

  props: {
    items: {
      type: Array,
      default: () => [],
      required: true
    }
  },

  data() {
    return {
      headers: [{ text: 'label', value: 'text' }, { text: 'shortcut', value: 'suffix_key' }]
    }
  }
}
</script>
