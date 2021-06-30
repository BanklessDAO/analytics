import { Field, Float, Int, ObjectType } from "type-graphql"
import { Entity, Column, BaseEntity, PrimaryColumn } from "typeorm"

@ObjectType()
@Entity()
export class DailyTweetActivity extends BaseEntity {
  @Field()
  @PrimaryColumn({ type: "date" })
  date: Date

  @Field(() => Int)
  @Column()
  tweets_published: number

  @Field(() => Int)
  @Column()
  impressions: number

  @Field(() => Int)
  @Column()
  engagements: number

  @Field(() => Float)
  @Column()
  engagement_rate: number

  @Field(() => Int)
  @Column()
  retweets: number

  @Field(() => Int)
  @Column()
  replies: number

  @Field(() => Int)
  @Column()
  likes: number

  @Field(() => Int)
  @Column()
  user_profile_clicks: number

  @Field(() => Int)
  @Column()
  url_clicks: number

  @Field(() => Int)
  @Column()
  hashtag_clicks: number

  @Field(() => Int)
  @Column()
  detail_expands: number

  @Field(() => Int)
  @Column()
  permalink_clicks: number

  @Field(() => Int)
  @Column()
  app_opens: number

  @Field(() => Int)
  @Column()
  app_installs: number

  @Field(() => Int)
  @Column()
  follows: number

  @Field(() => Int)
  @Column()
  email_tweet: number

  @Field(() => Int)
  @Column()
  dial_phone: number

  @Field(() => Int)
  @Column()
  media_views: number

  @Field(() => Int)
  @Column()
  media_engagements: number

  @Field(() => Int)
  @Column()
  promoted_impressions: number

  @Field(() => Int)
  @Column()
  promoted_engagements: number

  @Field(() => Float)
  @Column()
  promoted_engagement_rate: number

  @Field(() => Int)
  @Column()
  promoted_retweets: number

  @Field(() => Int)
  @Column()
  promoted_replies: number

  @Field(() => Int)
  @Column()
  promoted_likes: number

  @Field(() => Int)
  @Column()
  promoted_user_profile_clicks: number

  @Field(() => Int)
  @Column()
  promoted_url_clicks: number

  @Field(() => Int)
  @Column()
  promoted_hashtag_clicks: number

  @Field(() => Int)
  @Column()
  promoted_detail_expands: number

  @Field(() => Int)
  @Column()
  promoted_permalink_clicks: number

  @Field(() => Int)
  @Column()
  promoted_app_opens: number

  @Field(() => Int)
  @Column()
  promoted_app_installs: number

  @Field(() => Int)
  @Column()
  promoted_follows: number

  @Field(() => Int)
  @Column()
  promoted_email_tweet: number

  @Field(() => Int)
  @Column()
  promoted_dial_phone: number

  @Field(() => Int)
  @Column()
  promoted_media_views: number

  @Field(() => Int)
  @Column()
  promoted_media_engagements: number
}
