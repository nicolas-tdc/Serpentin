<template>
    <nav class="navbar">
      <v-layout justify-space-around>
        <v-card-title class="justify-center">
          <NuxtLink to="/" class="justify-center">Sales</NuxtLink>
        </v-card-title>
        <v-card-title class="justify-center">
          <NuxtLink to="/deals" class="justify-center">Deals</NuxtLink>
        </v-card-title>
        <v-card-title class="justify-center">
          <NuxtLink to="/statements">Statements</NuxtLink>
        </v-card-title>
        <v-card-title class="justify-center">
          <NuxtLink to="/compensations" class="justify-center">Compensations</NuxtLink>
        </v-card-title>
      </v-layout>
    </nav>
</template>

<script>
export default {}
</script>

<style>
  a {
    background-color: #EEEEEE;
    padding: 8px 20px;
    text-decoration:none;
    font-weight:bold;
    border-radius:5px;
    cursor:pointer;
  }

  .active {
      background-color: #ccccff;

  }

  .navbar {
    margin: 30px;
  }
</style>