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
