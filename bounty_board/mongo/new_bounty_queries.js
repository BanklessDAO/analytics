// Weekly Active Users (past 7-days)

// Number of Bounties created in past 7-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 7 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Number of Bounties Claimed in past 7-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      claimedAt: { $gt: new Date(new Date() - 7 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Number of Bounties Submitted in past 7-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      submittedAt: { $gt: new Date(new Date() - 7 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Number of Bounties Reviewed in past 7-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      reviewedAt: { $gt: new Date(new Date() - 7 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Monthly Active Users (past 30-days)

//Number of Bounties created in past 30-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Number of Bounties claimed in past 30-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      claimedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Number of Bounties Submitted in past 30-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      submittedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// Number of Bounties Reviewed in past 30-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      _claimedAt: "$claimedAt",
      _submittedAt: "$submittedAt",
      _reviewedAt: "$reviewedAt",
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      claimedAt: { $toDate: "$_claimedAt" },
      submittedAt: { $toDate: "$_submittedAt" },
      reviewedAt: { $toDate: "$_reviewedAt" },
    },
  },
  {
    $match: {
      reviewedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
]);

// POWER USERS: Number of People who created, claimed, submitted, reviewed bounties in past 30-days

//People who Created bounties in past 30-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
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

//People who Claimed bounties in past 30-days
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
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
  { $match: { customer_id: "834499078434979890" } },
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
  { $match: { customer_id: "834499078434979890" } },
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
