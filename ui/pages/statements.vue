<template>
  <div>
    <h1 class="mb-10">Statements</h1>

    <v-data-table
      v-if="statements"
      :headers="headers"
      :items="statements"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
export default {
  name: "statements",
  data() {
    return {
      headers: [
        {
          text: "Name",
          align: "start",
          value: "sales",
        },
        { text: "Month", value: "month" },
        { text: "Year", value: "year" },
        { text: "Deals Amount", value: "deals_amount" },
        { text: "Compensation Type", value: "compensation.type"},
        { text: "Compensation", value: "compensation.amount" },
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
