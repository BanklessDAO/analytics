import { Language } from "../../entity/examples/Language"
import { Arg, Mutation, Query, Resolver } from "type-graphql"

@Resolver()
export class LanguageResolver {
  @Mutation(() => Language)
  async createLanguage(@Arg("id") id: string, @Arg("name") name: string) {
    const lang = await Language.create({ id, name }).save()
    return lang
  }

  @Mutation(() => Boolean)
  async deleteLanguage(@Arg("id") id: string) {
    await Language.delete({ id })
    return true
  }

  @Query(() => [Language])
  languages() {
    return Language.find()
  }
}
