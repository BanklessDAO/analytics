import { GraphQLClient } from "graphql-request"
import getPort, { makeRange } from "get-port"
import { ApolloServer, ServerInfo } from "apollo-server"
import { getServer } from "../src/server"

type TestContext = {
  client: GraphQLClient
}

export function createTestContext(): TestContext {
  let ctx = {} as TestContext
  const graphqlCtx = graphqlTestContext()
  let server: ApolloServer | null = null

  beforeEach(async () => {
    if (server === null) {
      server = await getServer()
    }
    const client = await graphqlCtx.before(server)
    Object.assign(ctx, { client })
  })

  afterEach(async () => {
    await graphqlCtx.after()
  })

  return ctx
}

function graphqlTestContext() {
  let serverInstace: ServerInfo | null = null

  return {
    async before(server: ApolloServer) {
      const port = await getPort({ port: makeRange(4000, 6000) })
      serverInstace = await server.listen({ port })
      return new GraphQLClient(`http://localhost:${port}`)
    },
    async after() {
      serverInstace?.server.close()
    },
  }
}
