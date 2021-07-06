import { getServer } from "./server"

async function start() {
  const server = await getServer()
  server.listen().then(({ url }) => {
    console.log(`Server running at ${url}`)
  })
}

start()
