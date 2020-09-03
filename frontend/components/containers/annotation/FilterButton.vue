<template>
  <v-menu>
    <template v-slot:activator="{ on: menu }">
      <v-tooltip bottom>
        <template v-slot:activator="{ on: tooltip }">
          <v-btn
            class="text-capitalize ps-1 pe-1"
            min-width="36"
            outlined
            v-on="{ ...tooltip, ...menu }"
          >
            <v-icon>
              mdi-filter
            </v-icon>
          </v-btn>
        </template>
        <span>Select a filter</span>
      </v-tooltip>
    </template>
    <v-list>
      <v-list-item-group v-model="selected" mandatory>
        <v-list-item
          v-for="(item, i) in itemsAll"
          :key="i"
          :style="item.background_color ? {
            'color': item.background_color.concat(' !important')
          } : {}"
        >
          <v-list-item-icon>
            <v-icon v-if="selected === i">
              mdi-check
            </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>
              {{ item.text }}
            </v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
  </v-menu>
</template>

<script>
export default {
  props: {
    value: {
      type: String,
      default: '{}',
      required: true
    },
    items: {
      type: Array,
      default: () => ([]),
      required: true
    }
  },

  computed: {
    itemsAll() {
      const CONST_ITEMS = [
        { text: 'All', isChecked: '', id: '' },
        { text: 'Done', isChecked: 'false', id: '' },
        { text: 'Undone', isChecked: 'true', id: '' }
      ]
      this.items.forEach((item) => {
        item.isChecked = 'false'
      })
      return CONST_ITEMS.concat(this.items)
    },
    selected: {
      get() {
        const ParsedValue = JSON.parse(this.value)
        const index = this.itemsAll.findIndex(item => (item.isChecked === ParsedValue.isChecked && item.id === ParsedValue.selectedLabelId))
        return index === -1 ? 0 : index
      },
      set(value) {
        this.$emit('input', JSON.stringify({ isChecked: this.itemsAll[value].isChecked, selectedLabelId: this.itemsAll[value].id }))
      }
    }
  }
}
</script>
