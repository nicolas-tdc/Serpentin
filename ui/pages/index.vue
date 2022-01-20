<template>
  <v-container fluid grid-list-xl>
    <NavbarSerpentin/>
    <div class="chart" justify-space-around>
      <v-card-title class="justify-center">
        <h2 class="justify-center">Monthly Statistics</h2>
      </v-card-title>
      <BarChart :data="chartData" :options="chartOptions"/>
    </div>
    <div class="sales-profiles" justify-space-around>
      <v-card-title class="justify-center">
        <h2 class="justify-center profiles-title">Sales Profiles</h2>
      </v-card-title>
      <v-layout class="justify-center">
        <v-flex v-for="sale in sales" :key="sale.id">
          <h3>
            <router-link :to="{ path: 'sales-profile', query: { salesId: sale.id }}">
              {{ sale.name }}
            </router-link>
          </h3>
        </v-flex>
      </v-layout>
    </div>
  </v-container>
</template>

<script>
import NavbarSerpentin from '@/components/NavbarSerpentin'
import BarChart from '@/components/BarChart'

export default {
  name: "index",
  components: {
    NavbarSerpentin,
    BarChart,
  },
  data() {
    return {
      chartData: null,
      chartOptions: null,
    }
  },
  created() {
    this.$axios.get("api/sales").then((response) => {
      this.sales = response.data.sales
      this.chartData = {
        labels: this.sales.map(item => item.name),
        datasets: [
          {
            label: 'Target',
            backgroundColor: '#b5715c',
            data: this.sales.map(item => item.target)
          },
          {
            label: 'Total Deals Amount',
            backgroundColor: '#7532fa',
            data: this.sales.map(item => item.current_month_statement.deals_amount)
          },
          {
            label: 'Simple compensation',
            backgroundColor: '#26c786',
            data: this.sales.map(item => item.current_month_statement.compensations.simple.amount)
          },
          {
            label: 'Complex compensation',
            backgroundColor: '#5cb573',
            data: this.sales.map(item => item.current_month_statement.compensations.complex.amount)
          },
        ]
      }
    })
    this.chartOptions = {
    maintainAspectRatio: false,
    barValueSpacing: 20,
      scales: {
        yAxes: [{
          ticks: {
            min: 0,
            callback: function(value, index, values) {
                return value + '€';
            }
          }
        }]
      }
    }
  },
};
</script>

<style>
  .chart {
    height: 520px;
  }
  .sales-profiles {
    margin-bottom: 50px;
  }
  .profiles-title {
    margin-bottom: 20px;
  }
</style>
