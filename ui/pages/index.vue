<template>
  <v-container fluid grid-list-xl>
    <NavbarSerpentin/>
    <v-layout justify-space-around>
      <v-flex v-for="sale in sales">
        <v-card color="gray" width="200px">
          <v-card-title>{{ sale.name }}</v-card-title>
          <v-card-text v-if="sale.target">{{ sale.target }}</v-card-text>
        </v-card>
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import NavbarSerpentin from '@/components/NavbarSerpentin'
export default {
  name: "index",
  components: {
    NavbarSerpentin
  },
  created() {
    this.fetchSales()
  },
  methods: {
    fetchSales() {
      this.$axios.get("api/sales").then((response) => {
          this.sales = response.data.sales;
        });
    },
  },
};
</script>
