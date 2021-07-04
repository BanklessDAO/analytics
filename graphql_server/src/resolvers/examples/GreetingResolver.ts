import { Greeting, GreetingInput } from "../../entity/examples/Greeting"
import { Arg, Mutation, Query, Resolver } from "type-graphql"

@Resolver(() => Greeting)
export class GreetingResolver {
  @Mutation(() => Greeting)
  async createGreeting(@Arg("msg") msg: string, @Arg("langId") langId: string) {
    const greeting = await Greeting.create({ msg, langId, createdAt: new Date() }).save()
    return await Greeting.findOne(greeting.id, { relations: ["lang"] })
  }

  @Mutation(() => Boolean)
  async updateGreeting(@Arg("id") id: number, @Arg("input", () => GreetingInput) input: GreetingInput) {
    await Greeting.update({ id }, input)
    return true
  }

  @Mutation(() => Boolean)
  async deleteGreeting(@Arg("id") id: number) {
    await Greeting.delete({ id })
    return true
  }

  @Query(() => Greeting)
  findGreeting(@Arg("id") id: number) {
    return Greeting.findOne(id, { relations: ["lang"] })
  }

  @Query(() => [Greeting])
  async allGreetings() {
    const greetings = await Greeting.find({ relations: ["lang"] })
    return greetings
  }
}
