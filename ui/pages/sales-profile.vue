<template>
  <v-container fluid grid-list-xl>
    <NavbarSerpentin/>
    <div class="chart" justify-space-around>
      <v-card-title class="justify-center">
        <h1 class="justify-center">{{ sales.name }}</h1>
      </v-card-title>
      <v-card-title class="justify-center">
        <h2 class="justify-center">Statistics</h2>
      </v-card-title>
      <LineChart :data="chartData" :options="chartOptions"/>
    </div>
    <div class="chart" justify-space-around>
      <v-card-title class="justify-center">
        <h2 class="justify-center">Deals</h2>
      </v-card-title>
      <v-data-table
        v-if="deals"
        :headers="headers"
        :items="deals"
        :items-per-page="5"
        class="elevation-1"
      ></v-data-table>
    </div>
  </v-container>
</template>

<script>
import NavbarSerpentin from '@/components/NavbarSerpentin'
import LineChart from '@/components/LineChart'
import axios from 'axios';

export default {
  name: "index",
  components: {
    NavbarSerpentin,
    LineChart,
  },
  data() {
    return {
      chartData: null,
      chartOptions: null,
      headers: [
        {
          text: "Client name",
          align: "start",
          value: "name",
        },
        { text: "Modified", value: "modified" },
        { text: "Amount", value: "amount" },
        { text: "Closed", value: "closed" },
        { text: "Close date", value: "close_date" },
      ],
      deals: undefined,
      sales: '',
    }
  },
  created() {
    const userId = this.$route.query.salesId
    const salesStatements = this.$axios.get("api/sales/" + userId + "/statements")
    const salesDeals = this.$axios.get("api/sales/" + userId + "/deals")
    axios.all([salesStatements, salesDeals]).then(axios.spread((...responses) => {
      this.sales = responses[0].data.sales
      this.deals = responses[1].data.sales.deals
      const statements = Array.prototype.reverse.call(this.sales.last_statements)
      this.chartData = {
        labels: statements.map(item => item.month.toString() + '-' + item.year.toString()),
        datasets: [
          {
            label: 'Total deals amount',
            borderColor: '#26c786',
            fill: false,
            yAxesGroup: 'A',
            data: statements.map(item => item.deals_amount)
          },
          {
            label: 'Simple compensation',
            borderColor: '#7eadf7',
            fill: false,
            yAxesGroup: 'A',
            data: statements.map(item => item.compensations.simple.amount)
          },
          {
            label: 'Complex compensation',
            borderColor: '#7532fa',
            fill: false,
            yAxesGroup: 'A',
            data: statements.map(item => item.compensations.complex.amount)
          },
          {
            label: 'Number of deals',
            borderColor: '#aba81a',
            fill: false,
            yAxisID: 'B',
            data: statements.map(item => item.compensations.complex.deals_count)
          },
          {
            label: 'Number of closed deals',
            borderColor: '#ab6c1a',
            fill: false,
            yAxisID: 'B',
            data: statements.map(item => item.compensations.complex.closed_deals_count)
          },
        ]
      }
    }))
    this.chartOptions = {
    maintainAspectRatio: false,
      scales: {
        yAxes: [{
          id: 'A',
          type: 'linear',
          position: 'left',
          ticks: {
              callback: function(value, index, values) {
                  return value + '€';
              }
          }
        }, {
          id: 'B',
          type: 'linear',
          position: 'right',
          ticks: {
            max: 20,
            min: 0
          },
          scaleLabel: {
            display: true,
            labelString: 'Deals count'
          }
        }]
      }
    }
  },
};
</script>