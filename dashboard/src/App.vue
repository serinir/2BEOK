<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <div class="d-flex align-center">
        <v-img
          alt="Univ Logo"
          class="shrink mr-2"
          contain
          :src="require('./assets/logo.png')"
          transition="scale-transition"
          width="70"
        />
      </div>

      <v-spacer></v-spacer>

    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'App',
  components: {
  },
  data: () => ({
    //
  }),
  methods: {
  },
  computed: {
    show_logout: function() {
      console.log(this.$is_logged);
      return this.$is_logged;
    }
  }
};
</script>