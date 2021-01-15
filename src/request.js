const axios = require('axios')
const API_KEY = ''

const getGenericStats = async ({ username, platform }) => {
  const { data } = await axios.get(`https://api2.r6stats.com/public-api/stats/${username}/${platform}/weapons`, {
    headers: {
      Authorization: `Bearer ${API_KEY}`,
    },
  })

  console.log({ data })
}

getGenericStats({
  username: 'Kuri_NEON',
  platform: 'pc',
})