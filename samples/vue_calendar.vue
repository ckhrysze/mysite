<template>
  <div id="app">
    <table>
      <tr v-for="week in weeks">
        <td v-for="day in week.days">
          <div v-show="day.display" class="day">
            <div class="day-header">
              {{day.display}}
            </div>
            <div class="day-events">
              &nbsp;
            </div>
          </div>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'app',
  data () {
    return {
      weeks: []
    }
  },
  created: function() {
    let day_generator = moment().startOf('month').subtract(2, 'month')
    let month = day_generator.month()

    let week = {days: []}
    let padding_counter = 0
    while (padding_counter < day_generator.day()) {
      week.days.push({display: ''})
      padding_counter += 1
    }
    while (day_generator.month() == month) {
      week.days.push({display: day_generator.format('ddd DD')})
      day_generator.add(1, 'day')
      if (day_generator.day() == 0) {
        this.weeks.push(week)
        week = {days: []}
      }
    }
    if (week.days.length > 0) {
      this.weeks.push(week)
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;

  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}

table {
  width: 100%;
  height: 100%;
}

tr, td {
  padding: 0;
  margin: 0;
}

td {
  vertical-align: top;
  height: 150px;
}

.day {
  border: 1px solid #cccccc;
  width: 100%;
  height: 100%;
}

.day-header {
  background-color: #cccccc;
  text-align: right;
}

</style>
