import { Field, ObjectType } from "type-graphql"
import { Entity, Column, BaseEntity, PrimaryColumn } from "typeorm"

@ObjectType()
@Entity()
export class Language extends BaseEntity {
  @Field()
  @PrimaryColumn()
  id: string

  @Field()
  @Column()
  name: string
}
