const axios = require('axios')
const API_KEY = '89236ab4-678f-4320-965a-efed356a900a'

const getGenericStats = async ({ username, platform }) => {
  const { data } = await axios.get(`https://api2.r6stats.com/public-api/stats/${username}/${platform}/operators`, {
    headers: {
      Authorization: `Bearer ${API_KEY}`,
    },
  })

//   console.log({ data })
 // console.log(JSON.stringify(data, null, 2))
  var fs = require('fs');
  fs.writeFile ("ops_del.json", JSON.stringify(data), function(err) {
    if (err) throw err;
    console.log('complete');
    }
);
}

const getSeasonalStats = async ({ username, platform }) => {
  const { data } = await axios.get(`https://api2.r6stats.com/public-api/stats/${username}/${platform}/seasonal`, {
    headers: {
      Authorization: `Bearer ${API_KEY}`,
    },
  })

  console.log({ data })
  console.log(JSON.stringify(data), null, 2)
  var file = require('fs');
  file.writeFile ("seasonal_del.json", JSON.stringify(data), function(err) {
    if (err) throw err;
    console.log('complete');
    }
);
}

getGenericStats({
  username: 'delluxe_pkg',
  platform: 'pc',
})

getSeasonalStats({
  username: 'delluxe_pkg',
  platform: 'pc',
})