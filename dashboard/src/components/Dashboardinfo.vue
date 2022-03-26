<template>
  <div class="tab-content">
    <table class="min-w-full overflow-scroll">
        <thead>
            <tr>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-left leading-4 text-gray-500 tracking-wider">ID</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">Select</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">Station name</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">Status</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">Begin</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">End</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">Extract</th>
                <th class="px-6 py-3 border-b-2 border-gray-300  text-sm leading-4 text-gray-500 tracking-wider">Extract All</th>
                <th class="px-6 py-3 border-b-2 border-gray-300"></th>
            </tr>
        </thead>
        <tbody class="bg-white">
                <tr v-for="station in stations" :key="station.name_station" >
                    <td class="px-6 whitespace-no-wrap border-b border-gray-500">
                        <div class="flex items-center">
                            <div>
                                <div class="text-sm leading-5 text-gray-800">#{{station.sid}}</div>
                            </div>
                        </div>
                    </td>
                    <td class="px-6 whitespace-no-wrap border-b border-gray-500">
                        <input class="text-sm leading-5 text-gray-900" 
                            type="checkbox" 
                            v-model="comparable" 
                            :value="station.name_station" 
                            />
                    </td>
                    <td class="px-6 whitespace-no-wrap border-b border-gray-500">
                        <div class="text-sm leading-5 text-gray-900">{{station.name_station}}</div>
                    </td>
                    <td class="px-6  whitespace-no-wrap border-b text-gray-900 border-gray-500 text-sm leading-5">
                        <span class="relative inline-block px-3 py-1 font-semibold text-green-900 leading-tight">
                        <span aria-hidden class="absolute inset-0 bg-green-200 opacity-50 rounded-full"></span>
                        <span class="relative text-xs">active</span>
                    </span>
                    </td>
                    <td class="px-6  whitespace-no-wrap border-b text-gray-900 border-gray-500 text-sm leading-5"> 
                        <input 
                            type="date" 
                            name="" 
                            v-model="station.start" 
                            id=""
                            />
                    </td>
                    <td class="px-6  whitespace-no-wrap border-b text-gray-900 border-gray-500 text-sm leading-5">
                            <input 
                                type="date" 
                                v-model="station.end" 
                                name="" 
                                id=""
                                />
                    </td>
                    <td class="px-6 py-1 whitespace-no-wrap border-b border-gray-500 text-red-900 text-sm leading-5">                                       
                            <a :href="API_URL+station.name_station+'/sensors?start='+station.start+' 06:00:00&end='+station.end+' 06:00:00'">
                                <button class="px-5 py-1 border-red-500 border text-red-500 rounded transition 
                                    duration-300 hover:bg-red-700  hover:text-white focus:outline-none">
                                    Extract
                                </button>
                            </a>
                    </td>
                    <td class="px-6 py-1 whitespace-no-wrap border-b border-gray-500 text-sm leading-5">
                        <a :href=" API_URL + station.name_station + '/sensors/'">
                            <button class="px-5 py-1 border-red-500 border text-red-500 rounded transition 
                                duration-300 hover:bg-red-700 hover:text-white focus:outline-none">
                                Extract All
                            </button>
                        </a>
                    </td>
                    <td class="px-6 py-1 whitespace-no-wrap text-right border-b border-gray-500 text-sm leading-5">
                        <router-link :to="'/station/' + station.name_station"> 
                            <button class="px-5 py-1 border-red-500 border text-red-500 rounded transition 
                                duration-300 hover:bg-red-700  hover:text-white focus:outline-none">
                                Show Plot
                            </button>
                        </router-link>
                    </td>
            </tr>
        </tbody>
    </table>
    </div>
</template>
<script>
export default {
    name:'Dashboardinfo',
    setup() {
        const stations = [{
            name_station:"hello",
            start:"hello",
            sid:"12",
            start:"hello",
            end:"hallo"

        }]
        return {
            stations
        }
    },
}
</script>