import "reflect-metadata"
import { ApolloServer } from "apollo-server"
import { buildSchema } from "type-graphql"
import { createConnection, getConnectionOptions } from "typeorm"
import { GreetingResolver } from "./resolvers/examples/GreetingResolver"
import { LanguageResolver } from "./resolvers/examples/LanguageResolver"
import { DailyTweetActivityResolver } from "./resolvers/DailyTweetActivityResolver"

export async function getServer() {
  const options = await getConnectionOptions(process.env.NODE_ENV || "development")
  await createConnection({ ...options, name: "default" })

  const server = new ApolloServer({
    schema: await buildSchema({
      resolvers: [GreetingResolver, LanguageResolver, DailyTweetActivityResolver],
      validate: true,
    }),
  })
  return server
}
