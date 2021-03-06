import {
  DailyTweetActivity,
  DailyTweetActivityInput,
} from '../entity/DailyTweetActivity'
import { Arg, Mutation, Query, Resolver } from 'type-graphql'

@Resolver()
export class DailyTweetActivityResolver {
  @Mutation(() => Boolean)
  async importDailyTweetActivity(
    @Arg('date') date: string,
    @Arg('input', () => DailyTweetActivityInput) input: DailyTweetActivityInput
  ) {
    await DailyTweetActivity.create({ date, ...input }).save()
    return true
  }

  @Mutation(() => Boolean)
  async deleteDailyTweetActivity(@Arg('date') date: string) {
    await DailyTweetActivity.delete({ date })
    return true
  }

  @Query(() => [DailyTweetActivity])
  allDailyTweetActivity() {
    return DailyTweetActivity.find()
  }
}
