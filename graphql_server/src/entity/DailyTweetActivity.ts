import { Field, Float, InputType, Int, ObjectType } from 'type-graphql'
import { Entity, Column, BaseEntity, PrimaryColumn } from 'typeorm'

@ObjectType()
@Entity()
export class DailyTweetActivity extends BaseEntity {
  @Field()
  @PrimaryColumn({ type: 'date' })
  date: string

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  tweets_published?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  impressions?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  engagements?: number

  @Field(() => Float, { nullable: true })
  @Column({ nullable: true })
  engagement_rate?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  retweets?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  replies?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  likes?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  user_profile_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  url_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  hashtag_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  detail_expands?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  permalink_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  app_opens?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  app_installs?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  follows?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  email_tweet?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  dial_phone?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  media_views?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  media_engagements?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_impressions?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_engagements?: number

  @Field(() => Float, { nullable: true })
  @Column({ nullable: true })
  promoted_engagement_rate?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_retweets?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_replies?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_likes?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_user_profile_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_url_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_hashtag_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_detail_expands?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_permalink_clicks?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_app_opens?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_app_installs?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_follows?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_email_tweet?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_dial_phone?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_media_views?: number

  @Field(() => Int, { nullable: true })
  @Column({ nullable: true })
  promoted_media_engagements?: number
}

@InputType()
export class DailyTweetActivityInput {
  @Field(() => Int, { nullable: true })
  tweets_published?: number

  @Field(() => Int, { nullable: true })
  impressions?: number

  @Field(() => Int, { nullable: true })
  engagements?: number

  @Field(() => Float, { nullable: true })
  engagement_rate?: number

  @Field(() => Int, { nullable: true })
  retweets?: number

  @Field(() => Int, { nullable: true })
  replies?: number

  @Field(() => Int, { nullable: true })
  likes?: number

  @Field(() => Int, { nullable: true })
  user_profile_clicks?: number

  @Field(() => Int, { nullable: true })
  url_clicks?: number

  @Field(() => Int, { nullable: true })
  hashtag_clicks?: number

  @Field(() => Int, { nullable: true })
  detail_expands?: number

  @Field(() => Int, { nullable: true })
  permalink_clicks?: number

  @Field(() => Int, { nullable: true })
  app_opens?: number

  @Field(() => Int, { nullable: true })
  app_installs?: number

  @Field(() => Int, { nullable: true })
  follows?: number

  @Field(() => Int, { nullable: true })
  email_tweet?: number

  @Field(() => Int, { nullable: true })
  dial_phone?: number

  @Field(() => Int, { nullable: true })
  media_views?: number

  @Field(() => Int, { nullable: true })
  media_engagements?: number

  @Field(() => Int, { nullable: true })
  promoted_impressions?: number

  @Field(() => Int, { nullable: true })
  promoted_engagements?: number

  @Field(() => Float, { nullable: true })
  promoted_engagement_rate?: number

  @Field(() => Int, { nullable: true })
  promoted_retweets?: number

  @Field(() => Int, { nullable: true })
  promoted_replies?: number

  @Field(() => Int, { nullable: true })
  promoted_likes?: number

  @Field(() => Int, { nullable: true })
  promoted_user_profile_clicks?: number

  @Field(() => Int, { nullable: true })
  promoted_url_clicks?: number

  @Field(() => Int, { nullable: true })
  promoted_hashtag_clicks?: number

  @Field(() => Int, { nullable: true })
  promoted_detail_expands?: number

  @Field(() => Int, { nullable: true })
  promoted_permalink_clicks?: number

  @Field(() => Int, { nullable: true })
  promoted_app_opens?: number

  @Field(() => Int, { nullable: true })
  promoted_app_installs?: number

  @Field(() => Int, { nullable: true })
  promoted_follows?: number

  @Field(() => Int, { nullable: true })
  promoted_email_tweet?: number

  @Field(() => Int, { nullable: true })
  promoted_dial_phone?: number

  @Field(() => Int, { nullable: true })
  promoted_media_views?: number

  @Field(() => Int, { nullable: true })
  promoted_media_engagements?: number
}
