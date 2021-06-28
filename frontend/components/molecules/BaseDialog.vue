<template>
  <v-dialog
    :value="dialog"
    :width="width"
    :scrollable="scrollable"
  >
    <slot />
  </v-dialog>
</template>

<script>
export default {
  props: {
    dialog: {
      type: Boolean,
      default: false,
      required: true
    },
    width: {
      type: String,
      default: '800'
    },
    scrollable: {
      type: Boolean,
      default: false
    }
  }
}
</script>
