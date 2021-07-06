import { Field, InputType, Int, ObjectType } from "type-graphql"
import { Entity, PrimaryGeneratedColumn, Column, BaseEntity, JoinColumn, ManyToOne } from "typeorm"
import { Language } from "./Language"

@ObjectType()
@Entity()
export class Greeting extends BaseEntity {
  @Field(() => Int)
  @PrimaryGeneratedColumn()
  id: number

  @Field()
  @Column()
  msg: string

  @Field()
  @Column()
  langId: string

  @Field()
  @ManyToOne(() => Language)
  @JoinColumn({ name: "langId" })
  lang: Language

  @Field()
  @Column({ type: "datetime" })
  createdAt: Date
}

@InputType()
export class GreetingInput {
  @Field(() => String, { nullable: true })
  msg?: string

  @Field(() => String, { nullable: true })
  langId?: string
}
