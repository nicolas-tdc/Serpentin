<template>
  <div>
    <h1 class="mb-10">Simple Compensations</h1>

    <v-data-table
      v-if="simple_compensations"
      :headers="headers"
      :items="simple_compensations"
      :items-per-page="5"
      class="elevation-1"
    ></v-data-table>
  </div>
</template>

<script>
export default {
  name: "simple_compensations",
  data() {
    return {
      headers: [
        {
          text: "Name",
          align: "start",
          value: "name",
        },
      ],
      simple_compensations: [],
    };
  },
  created() {
    this.fetchSimpleCompensations();
  },
  methods: {
    fetchSimpleCompensations() {
      this.$axios.get("api/simple-compensations").then((response) => {
        this.simple_compensations = response.data.simple-compensations;
      });
    },
  },
};
</script>
