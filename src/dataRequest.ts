import R6StatsAPI from '@r6stats/node'

// create an instance of the API client
const api = new R6StatsAPI({ apiKey: 'xxx' })


// valid platform options: pc, xbox, ps4

// get general stats (kills, deaths, etc.)
const player = await api.playerStats({ username: 'xxx', platform: 'pc' })
console.log(player.username, player.stats.general.kills)

// get operator stats
const player = await api.operatorStats({ username: 'xxx', platform: 'pc' })
console.log(player.username, player.operators[0].name, player.operators[0].kills)

// get weapon stats
const player = await api.weaponStats({ username: 'xxx', platform: 'pc' })
console.log(player.username, player.weapons[0].name, player.weapons[0].kills)

// get weapon category stats
const player = await api.weaponCategoryStats({ username: 'xxx', platform: 'pc' })
console.log(player.username, player.categories[0].category, player.categories[0].kills)