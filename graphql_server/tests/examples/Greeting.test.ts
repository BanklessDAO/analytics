import { createTestContext } from "../__helpers"

const ctx = createTestContext()

test("test greeting api", async () => {
  await ctx.client.request(`
    mutation {
      createLanguage(id: "en", name: "english") {
        id
        name
      }
    }
  `)

  await ctx.client.request(`
    mutation {
      createLanguage(id: "de", name: "german") {
        id
        name
      }
    }
  `)

  let result = await ctx.client.request(`
    mutation {
      createGreeting(msg: "hello", langId: "en") {
        id
        msg
        lang {
          name
        }
      }
    }
  `)

  expect(result).toMatchInlineSnapshot(`
Object {
  "createGreeting": Object {
    "id": 1,
    "lang": Object {
      "name": "english",
    },
    "msg": "hello",
  },
}
`)

  await ctx.client.request(`
    mutation {
      updateGreeting(id: 1, input: {
        langId: "en",
        msg: "moin"
      })
    }
  `)

  result = await ctx.client.request(`
    {
      allGreetings {
        id
        msg
        lang {
          name
        }
      }
    }
  `)

  expect(result).toMatchInlineSnapshot(`
Object {
  "allGreetings": Array [
    Object {
      "id": 1,
      "lang": Object {
        "name": "english",
      },
      "msg": "moin",
    },
  ],
}
`)
})
