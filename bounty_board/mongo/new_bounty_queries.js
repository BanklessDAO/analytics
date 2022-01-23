//name of people who created bounties in past 30-days
db.bounties.aggregate([
  { $match: { $and: [{ season: 2 }, { customer_id: "834499078434979890" }] } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _name: "$createdBy.discordHandle",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      name: "$_name",
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

//name of people who claimed bounties in past 30-days
db.bounties.aggregate([
  { $match: { $and: [{ season: 2 }, { customer_id: "834499078434979890" }] } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _claimedAt: "$claimedAt",
      _name: "$claimedBy.discordHandle",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      claimedAt: { $toDate: "$_claimedAt" },
      name: "$_name",
    },
  },
  {
    $match: {
      claimedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

//name of people who submitted bounties in past 30-days
db.bounties.aggregate([
  { $match: { $and: [{ season: 2 }, { customer_id: "834499078434979890" }] } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _submittedAt: "$submittedAt",
      _name: "$submittedBy.discordHandle",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      submittedAt: { $toDate: "$_submittedAt" },
      name: "$_name",
    },
  },
  {
    $match: {
      submittedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

//name of people who reviewed bounties in past 30-days
db.bounties.aggregate([
  { $match: { $and: [{ season: 2 }, { customer_id: "834499078434979890" }] } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _reviewedAt: "$reviewedAt",
      _name: "$reviewedBy.discordHandle",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      reviewedAt: { $toDate: "$_reviewedAt" },
      name: "$_name",
    },
  },
  {
    $match: {
      reviewedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);
