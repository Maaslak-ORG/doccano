<template>
  <v-data-table
    :items="items"
    :headers="headers"
    hide-default-footer
    hide-default-header
    class="elevation-1"
    caption="Labels cheat sheet"
  >
    <template v-slot:items="props">
      <tr>
        <td
          v-for="key in Object.keys(props.items).filter((key) => (Object.keys(props.headers).includes(key)))"
          :key="key"
          :style="{
            'color': props.item['background_color'].concat(' !important')
          }"
        >
          {{ props.item[key] }}
        </td>
      </tr>
    </template>
  </v-data-table>
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
      headers: [{ text: 'label', value: 'text' }, { text: 'shortcut', value: 'suffix_key' }, { text: 'background_color', value: 'background_color' }]
    }
  }
}
</script>
