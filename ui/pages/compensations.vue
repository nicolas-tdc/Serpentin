<template>
  <v-container fluid grid-list-xl>
    <NavbarSerpentin/>
    <v-data-table
      v-if="compensations"
      :headers="headers"
      :items="compensations"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </v-container>
</template>

<script>
import NavbarSerpentin from '@/components/NavbarSerpentin'
export default {
  name: "compensations",
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
        { text: "Type", value: "type" },
        { text: "Amount", value: "amount" },
        { text: "Deals count", value: "deals_count" },
        { text: "Closed deals count", value: "closed_deals_count" },
        { text: "Draft", value: "draft" },
      ],
      compensations: [],
    };
  },
  created() {
    this.fetchCompensations();
  },
  methods: {
    fetchCompensations() {
      this.$axios.get("api/compensations").then((response) => {
        this.compensations = response.data.compensations;
      });
    },
  },
};
</script>
