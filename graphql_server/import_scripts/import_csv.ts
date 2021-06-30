import { createReadStream } from "fs"
import parse from "csv-parse"

const processFile = async () => {
  const records = new Array<any>()

  console.log(process.argv)

  const parser = createReadStream(
    `${__dirname}/../../marketing/twitter/raw/daily_tweet_activity_metrics_banklessDAO_20210508_20210608_en.csv`
  ).pipe(parse({ delimiter: "," }))

  for await (const record of parser) {
    records.push(record)
  }

  return records
}

;(async () => {
  const records = await processFile()
  console.info(records)
})()
