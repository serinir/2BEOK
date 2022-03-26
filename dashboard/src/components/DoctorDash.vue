<template>
    <v-container class="d-flex flex-row align-start" v-if="is_doctor">
            <v-card
            class="pa-1"
            max-width="20%"
            tile
            >
                <v-list shaped>
                    <v-list-item-group
                        v-model="selectedItem"
                        color="primary"
                    >
                        <v-list-item
                        v-for="(item, i) in items"
                        :key="i"
                        @click="updateData(i)"
                        >
                        <v-list-item-icon>
                            <v-icon v-text="item.icon"></v-icon>
                        </v-list-item-icon>
                        <v-list-item-content>
                            <v-list-item-title v-text="item.text"></v-list-item-title>
                        </v-list-item-content>
                        </v-list-item>
                    </v-list-item-group>
                </v-list>
            </v-card>

            <v-card
            class="flex-grow-1 mx-4 pa-4"
            v-show="updateTab == 0"
            >
                <v-card-title class="justify-center">Patients</v-card-title>

                <v-divider></v-divider>

                <v-list
                class="pa-0"
                two-line
                >
                    <v-virtual-scroll
                    :items="tickets"
                    :item-height="50"
                    height="400"
                    >
                        <template
                        v-slot:default="{ item }"
                        >
                            <v-list-item
                            :key="item.patient"
                            >
                                <v-list-item-action>
                                    <v-btn
                                    icon
                                    >
                                        <v-icon color="grey lighten-1">mdi-minus</v-icon>
                                    </v-btn>
                                </v-list-item-action>
                            </v-list-item>
                        </template>
                    </v-virtual-scroll>
                </v-list>
            </v-card>

    </v-container>
</template>

<script>
    export default {
        name: 'DoctorDash',
        data: () => ({
            is_doctor: true,
            tickets: [],
            selectedItem: 0,
            items: [
                { text: 'Patients', icon: 'mdi-format-list-bulleted' },
                { text: 'Dropout Warnings', icon: 'mdi-account-warning' },
                { text: 'Logout', icon: 'mdi-logout'}
            ]
        }),
        methods: {
            getTickets: function() {
                this.$http.get(`${this.$api}/doctor`, {"_id": "623ed0c8270103f97a1ebed5"})
                .then(response => {
                    this.tickets = response.body;
                    this.is_doctor = true;
                }, response => {
                    // this.is_doctor = false;
                    // this.$router.push('login');
                    console.log(response);
                });
            },
            updateData: function(i) {
                this.selectedItem = i;
                if (i == 2) {
                    this.$cookies.remove('Authorization');
                    this.$router.push('/login');
                }
            }
        },
        computed: {
            updateTab: function() {
                return this.selectedItem;
            }
        },
        created() {
            this.getTickets();
        }
    }
</script>