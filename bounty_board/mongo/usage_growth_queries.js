// Total and Unique Bounty Creators by Week
// BanklessDAO Jan 1 - Jan 31, 2022
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { createdAt: { $gte: "2022-01-01" } },
        { createdAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$createdAt" } },
      num_creators: { $sum: 1 },
      unique_creators: { $addToSet: "$createdBy.discordHandle" },
    },
  },
]);

// Total and Unique Bounty Claimers by Week
// BanklessDAO Jan 1 - Jan 31, 2022
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { claimedAt: { $gte: "2022-01-01" } },
        { claimedAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      claimedAt: { $toDate: "$claimedAt" },
      "claimedBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$claimedAt" } },
      num_claimers: { $sum: 1 },
      unique_claimers: { $addToSet: "$claimedBy.discordHandle" },
    },
  },
]);

// Total and Unique Bounty Submitters by Week
// BanklessDAO Jan 1 - Jan 31, 2022
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { submittedAt: { $gte: "2022-01-01" } },
        { submittedAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      submittedAt: { $toDate: "$submittedAt" },
      "submittedBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$submittedAt" } },
      num_submitters: { $sum: 1 },
      unique_submitters: { $addToSet: "$submittedBy.discordHandle" },
    },
  },
]);

// Total and Unique Bounty Reviewers by Week
// BanklessDAO Jan 1 - Jan 31, 2022
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { reviewedAt: { $gte: "2022-01-01" } },
        { reviewedAt: { $lt: "2022-02-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      reviewedAt: { $toDate: "$reviewedAt" },
      "reviewedBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$reviewedAt" } },
      num_reviewers: { $sum: 1 },
      unique_reviewer: { $addToSet: "$reviewedBy.discordHandle" },
    },
  },
]);

// UNIQUE CREATORS - last 30 days (checked) FINAL
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _createdAt: "$createdAt",
      "createdBy.discordHandle": 1,
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      createdAt: { $toDate: "$_createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  {
    $match: {
      createdAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$createdAt" } },
      num_creators: { $sum: 1 },
      unique_creators: { $addToSet: "$createdBy.discordHandle" },
    },
  },
]);

// UNIQUE CLAIMERS - last 30 days (checked) FINAL
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _claimedAt: "$claimedAt",
      "claimedBy.discordHandle": 1,
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      claimedAt: { $toDate: "$_claimedAt" },
      "claimedBy.discordHandle": 1,
    },
  },
  {
    $match: {
      claimedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$claimedAt" } },
      num_claimers: { $sum: 1 },
      unique_claimers: { $addToSet: "$claimedBy.discordHandle" },
    },
  },
]);

// UNIQUE SUBMITTERS - last 30 days (checked) FINAL
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _submittedAt: "$submittedAt",
      "submittedBy.discordHandle": 1,
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      submittedAt: { $toDate: "$_submittedAt" },
      "submittedBy.discordHandle": 1,
    },
  },
  {
    $match: {
      submittedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$submittedAt" } },
      num_submitters: { $sum: 1 },
      unique_submitters: { $addToSet: "$submittedBy.discordHandle" },
    },
  },
]);

// UNIQUE REVIEWERS - last 30 days (checked) FINAL
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $project: {
      _id: 1,
      _customer_id: "$customer_id",
      _title: "$title",
      _status: "$status",
      _reviewedAt: "$reviewedAt",
      "reviewedBy.discordHandle": 1,
    },
  },
  {
    $project: {
      _id: 1,
      customer_id: "$_customer_id",
      title: "$_title",
      status: "$_status",
      reviewedAt: { $toDate: "$_reviewedAt" },
      "reviewedBy.discordHandle": 1,
    },
  },
  {
    $match: {
      reviewedAt: { $gt: new Date(new Date() - 30 * 60 * 60 * 24 * 1000) },
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$reviewedAt" } },
      num_reviewers: { $sum: 1 },
      unique_reviewers: { $addToSet: "$reviewedBy.discordHandle" },
    },
  },
]);

// Number of (Unique) Bounty CREATORS per week since start of year (FINAL)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { createdAt: { $gte: "2022-01-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      createdAt: { $toDate: "$createdAt" },
      "createdBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$createdAt" } },
      unique_creators: { $addToSet: "$createdBy.discordHandle" },
    },
  },
]);

// Number of (Unique) Bounty CLAIMERS per week since start of year (FINAL)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { claimedAt: { $gte: "2022-01-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      claimedAt: { $toDate: "$claimedAt" },
      "claimedBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$claimedAt" } },
      unique_claimers: { $addToSet: "$claimedBy.discordHandle" },
    },
  },
]);

// Number of (Unique) Bounty SUBMITTERS per week since start of year (FINAL)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { submittedAt: { $gte: "2022-01-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      submittedAt: { $toDate: "$submittedAt" },
      "submittedBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$submittedAt" } },
      unique_submitters: { $addToSet: "$submittedBy.discordHandle" },
    },
  },
]);

// Number of (Unique) Bounty REVIEWERS per week since start of year (FINAL)
db.bounties.aggregate([
  {
    $match: {
      $and: [
        { customer_id: "834499078434979890" },
        { reviewedAt: { $gte: "2022-01-01" } },
      ],
    },
  },
  {
    $project: {
      _id: 1,
      reviewedAt: { $toDate: "$reviewedAt" },
      "reviewedBy.discordHandle": 1,
    },
  },
  {
    $group: {
      _id: { week: { $isoWeek: "$reviewedAt" } },
      unique_reviewers: { $addToSet: "$reviewedBy.discordHandle" },
    },
  },
]);

// Find Query
// Count TOTAL Bankless bounties
db.bounties.find({ customer_id: "834499078434979890" }).count();

// bounties before jan 2022: 98
db.bounties
  .find({
    $and: [
      { customer_id: "834499078434979890" },
      { createdAt: { $lt: "2022-01-01" } },
    ],
  })
  .count();

// bounties after jan 2022: tbd
db.bounties
  .find({
    $and: [
      { customer_id: "834499078434979890" },
      { createdAt: { $gte: "2022-01-01" } },
    ],
  })
  .count();

// bounties in jan 2022: 24
db.bounties
  .find({
    $and: [
      { customer_id: "834499078434979890" },
      { createdAt: { $gte: "2022-01-01", $lt: "2022-02-01" } },
    ],
  })
  .count();

// Aggregation Framework
// Percentage of New Bounties created After Jan 1st 2022
// before and after New Years
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $group: {
      _id: 1,
      count_new: {
        $sum: { $cond: [{ $gte: ["$createdAt", "2022-01-01"] }, 1, 0] },
      },
      count_repeat: {
        $sum: { $cond: [{ $lt: ["$createdAt", "2022-01-01"] }, 1, 0] },
      },
    },
  },
  {
    $project: {
      _id: 1,
      new_creator_percentage: { $divide: ["$count_new", "$count_repeat"] },
    },
  },
]);

// Percentage of New Bounties created After Feb 1st 2022
// before and after Feb 1st 2022
db.bounties.aggregate([
  { $match: { customer_id: "834499078434979890" } },
  {
    $group: {
      _id: 1,
      count_new: {
        $sum: { $cond: [{ $gte: ["$createdAt", "2022-02-01"] }, 1, 0] },
      },
      count_repeat: {
        $sum: { $cond: [{ $lt: ["$createdAt", "2022-02-01"] }, 1, 0] },
      },
    },
  },
  {
    $project: {
      _id: 1,
      new_creator_percentage: { $divide: ["$count_new", "$count_repeat"] },
    },
  },
]);
