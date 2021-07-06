import { createReadStream } from 'fs'
import { GraphQLClient } from 'graphql-request'
import parse from 'csv-parse'

const processFile = async () => {
  const records = new Array<any>()

  const parser = createReadStream(
    `${__dirname}/../../marketing/twitter/raw/daily_tweet_activity_metrics_banklessDAO_20210508_20210608_en.csv`
  ).pipe(parse({ delimiter: ',' }))

  for await (const record of parser) {
    records.push(record)
  }

  return records
}

;(async () => {
  const records = await processFile()
  const gqlClient = new GraphQLClient('http://localhost:4000')

  for (let i = 1; i < records.length; i++) {
    const dta = records[i]

    let request = `
mutation {
  importDailyTweetActivity(date: "${dta[0]}", input: {`
    for (let j = 1; j < records[0].length; j++) {
      const header = (records[0][j] as string).toLowerCase().replace(/ /g, '_')
      request += `
    ${header}: ${dta[j] != '-' ? dta[j] : null}`
    }
    request += `
  })
}
`
    await gqlClient.request(request)
  }
})()
