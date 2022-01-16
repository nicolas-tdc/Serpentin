<template>
  <div>
    <h1 class="mb-10">Compensations</h1>

    <v-data-table
      v-if="compensations"
      :headers="headers"
      :items="compensations"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
export default {
  name: "compensations",
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
        { text: "Deals count", value: "deals-count" },
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
