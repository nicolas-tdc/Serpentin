<template>
  <v-container fluid grid-list-xl>
    <NavbarSerpentin/>
    <v-data-table
      v-if="statements"
      :headers="headers"
      :items="statements"
      :items-per-page="5"
      class="elevation-1"
    >
      <template #item.date="{ item }">{{ item.month }}-{{ item.year }}</template>
    </v-data-table>
  </v-container>
</template>

<script>
import NavbarSerpentin from '@/components/NavbarSerpentin'
export default {
  name: "statements",
  components: {
    NavbarSerpentin
  },
  data() {
    return {
      items: [
        { month: "month", year: "year" },
      ],
      headers: [
        {
          text: "Name",
          align: "start",
          value: "sales",
        },
        { text: "Date", value: "date" },
        { text: "Deals Amount", value: "deals_amount" },
        { text: "Deals", value: "compensations.simple.deals-count"},
        { text: "Closed Deals", value: "compensations.simple.closed-deals-count" },
        { text: "Simple Amount", value: "compensations.simple.amount"},
        { text: "Complex Amount", value: "compensations.complex.amount"},
      ],
      statements: [],
    };
  },
  created() {
    this.fetchStatements();
  },
  methods: {
    fetchStatements() {
      this.$axios.get("api/statements").then((response) => {
        this.statements = response.data.statements;
      });
    },
  },
};
</script>
