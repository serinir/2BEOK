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
                            <v-dialog
                            v-model="dialog"
                            scrollable
                            max-width="1000px"
                            >
                                <template v-slot:activator="{ on, attrs }">
                                    <v-list-item
                                    :key="item._id"
                                    v-bind="attrs"
                                    v-on="on"
                                    >
                                        <v-list-item-icon>
                                            {{item.prediction}}
                                        </v-list-item-icon>
                                        <v-list-item-content>
                                            <v-list-item-title>{{ item.patient.mail }}</v-list-item-title>
                                            <v-list-item-subtitle v-text="item.date"></v-list-item-subtitle>
                                        </v-list-item-content>

                                        <v-list-item-action>
                                            <v-dialog
                                            v-model="dialog1"
                                            persistent
                                            max-width="600px"
                                            >
                                            <template v-slot:activator="{ on, attrs }">
                                                <v-btn
                                                color="primary"
                                                dark
                                                v-bind="attrs"
                                                v-on="on"
                                                >
                                                Add Session Summary
                                                </v-btn>
                                            </template>
                                            <v-card>
                                                <v-card-title>
                                                <span class="text-h5">Session Summary</span>
                                                </v-card-title>
                                                <v-card-text>
                                                <v-container>
                                                    <v-text-field
                                                        label="Write what you think is most noticeable for this session"
                                                        required
                                                        v-model="note"
                                                    ></v-text-field>
                                                </v-container>
                                                </v-card-text>
                                                <v-card-actions>
                                                    <v-spacer></v-spacer>
                                                    <v-btn
                                                        color="blue darken-1"
                                                        text
                                                        @click="dialog1 = false"
                                                    >
                                                        Close
                                                    </v-btn>
                                                    <v-btn
                                                        color="blue darken-1"
                                                        text
                                                        @click="sendSummary(item._id)"
                                                    >
                                                        Save
                                                    </v-btn>
                                                </v-card-actions>
                                            </v-card>
                                            </v-dialog>
                                        </v-list-item-action>
                                    </v-list-item>
                                </template>
                                <v-card>
                                    <v-card-title>{{ item.patient.mail }}</v-card-title>
                                    <v-card-subtitle>{{ item.date }}</v-card-subtitle>
                                    <v-divider class="mx-4"></v-divider>
                                    <v-card-text>
                                        <v-list-item
                                        three-line
                                        v-for="summary in item.history"
                                        :key="summary"
                                        >
                                        <v-list-item-content>
                                            <v-list-item-title>{{summary.doctor}}</v-list-item-title>
                                            <v-list-item-subtitle>{{summary.date}}</v-list-item-subtitle>
                                            <v-list-item-subtitle>{{summary.note}}</v-list-item-subtitle>
                                        </v-list-item-content>
                                        </v-list-item>
                                    </v-card-text>
                                </v-card>
                            </v-dialog>
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
            dialog1: false,
            dialog: false,
            doctor_id: "623ed0c8270103f97a1ebed5",
            selectedItem: 0,
            items: [
                { text: 'Patients', icon: 'mdi-format-list-bulleted' },
                { text: 'Dropout Warnings', icon: 'mdi-account-alert' },
                { text: 'Logout', icon: 'mdi-logout'}
            ],
            note: ""
        }),
        methods: {
            getTickets: function() {
                this.$http.get(`${this.$api}/doctor`, {params: {"_id": this.doctor_id}})
                .then(response => {
                    this.tickets = response.body;
                    this.is_doctor = true;
                }, response => {
                    // this.is_doctor = false;
                    // this.$router.push('login');
                    console.log(response);
                });
            },
            sendSummary: function(ticket_id) {
                this.$http.post(`${this.$api}/tickets`, {
                    _id: ticket_id,
                    summary: {
                        doctor_id: this.doctor_id,
                        note: this.note
                    }
                })
                .then(() => {
                    this.dialog1 = false;
                    this.getTickets();
                });
            },
            getPrediction: function() {
                this.$http.post(`${this.$api}/diagnose`)
                .then((response) => {
                    return response.prediction;
                })
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