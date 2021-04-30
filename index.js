
const labels = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
];

// const labels = getLables()

const data = {
  labels: labels,
  datasets: [{
    label: 'Số lần xuất hiện',
    backgroundColor: '#037bfc',
    borderColor: 'rgb(255, 99, 132)',
    data: [0, 10, 5, 2, 20, 30, 45],
  }]
};
// </block:setup>

// <block:config:0>
const config = {
  type: 'bar',
  data,
  options: {}
};
// </block:config>

module.exports = {
  actions: [],
  config: config,
};