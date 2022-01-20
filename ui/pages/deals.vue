<template>
  <v-container fluid grid-list-xl>
    <NavbarSerpentin/>
    <v-data-table
      v-if="deals"
      :headers="headers"
      :items="deals"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </v-container>
</template>

<script>
import NavbarSerpentin from '@/components/NavbarSerpentin'
export default {
  name: "deals",
  components: {
    NavbarSerpentin
  },
  data() {
    return {
      headers: [
        {
          text: "Name",
          align: "start",
          value: "name",
        },
        { text: "Modified", value: "modified" },
        { text: "Amount", value: "amount" },
        { text: "Closed", value: "closed" },
        { text: "Close date", value: "close_date" },
        { text: "Owner", value: "owner" },
      ],
      deals: undefined,
    };
  },
  created() {
    this.fetchDeals();
  },
  methods: {
    fetchDeals() {
      this.$axios.get("api/deals").then((response) => {
        this.deals = response.data.deals;
      });
    },
  },
};
</script>
