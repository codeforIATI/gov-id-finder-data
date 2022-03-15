# Government Organisation ID Finder

Search government entity names (e.g. Ministries) to find their respective organisation identifiers (and vice versa), using data published in government budgets.

This repository contains the data; the front end can be found in the following repository:
https://github.com/codeforIATI/gov-id-finder

## What’s this for?

For traceability [[1]](#footnote-1), it’s crucial to know that ‘organisation one’ is the same as ‘organizzazione uno’. IATI solves this problem with [organisation identifiers](http://iatistandard.org/202/organisation-identifiers/) – standard, canonical references for organisations.

However, there’s no single database for these references (there’s just a [list of lists](http://org-id.guide)), so:

 * It’s difficult for IATI publishers to know the correct reference to use when entering IATI data. For instance:

    > how should I refer to my implementing partner in activity x?

 * It’s difficult to do a reverse lookup i.e. get from an organisation identifier to an organisation name. For instance, [the example provided here](https://discuss.codeforiati.org/t/data-use-observation-a-reference-for-an-organisation-alone-is-not-enough/1091) is:

    > which organisation does `NL-KVK-41198677` refer to?

## Why take this approach?

This works as described by [on IATI Connect](https://iaticonnect.org/group/7/discussion/new-methodology-identifying-government-entities). This approach means that:

 1. It’s relatively simple to understand
 2. It’s easy to automate
 3. It focuses on codes used by governments in their own budgets, or Charts of Accounts

----

<a name="footnote-1">[1]</a>: Perhaps ‘traceability’ is a bit grandiose here. There’s lots of useful stuff we can do if we know lots of disparate data all refers to the same organisation. For instance, we could list all the activities that a given (non-publishing) organisation is implementing.
