import { createTestContext } from "../__helpers"

const ctx = createTestContext()

test("test language api", async () => {
  let result = await ctx.client.request(`
    mutation {
      createLanguage(id: "en", name: "english") {
        id
        name
      }
    }
  `)

  expect(result).toMatchInlineSnapshot(`
Object {
  "createLanguage": Object {
    "id": "en",
    "name": "english",
  },
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

  result = await ctx.client.request(`
    query {
      languages {
        id
        name
      }
    }
  `)

  expect(result).toMatchInlineSnapshot(`
Object {
  "languages": Array [
    Object {
      "id": "en",
      "name": "english",
    },
    Object {
      "id": "de",
      "name": "german",
    },
  ],
}
`)

  await ctx.client.request(`
    mutation {
      deleteLanguage(id: "de")
    }
  `)

  result = await ctx.client.request(`
    query {
      languages {
        id
        name
      }
    }
  `)

  expect(result).toMatchInlineSnapshot(`
Object {
  "languages": Array [
    Object {
      "id": "en",
      "name": "english",
    },
  ],
}
`)
})
