import { DailyTweetActivity } from "../entity/DailyTweetActivity"
import { Arg, Mutation, Query, Resolver } from "type-graphql"

@Resolver()
export class DailyTweetActivityResolver {
  @Mutation(() => DailyTweetActivity)
  async importDailyTweetActivity(@Arg("date") date: Date) {
    await DailyTweetActivity.create({ date })
    return true
  }

  @Mutation(() => Boolean)
  async deleteDailyTweetActivity(@Arg("date") date: Date) {
    await DailyTweetActivity.delete({ date })
    return true
  }

  @Query(() => [DailyTweetActivity])
  dailyTweetActivity() {
    return DailyTweetActivity.find()
  }
}
