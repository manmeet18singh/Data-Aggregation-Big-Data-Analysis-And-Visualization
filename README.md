# Word Clouds

## Data Aggregation: Big Data Analysis and Visualization

**Overview:**
> Data aggregation from more than one source using the APIs exposed by data sources Applying classical big data analytic method of MapReduce to the unstructured data collected Store the data collected on WORM infrastructure Hadoop Building a visualization data product.

**Project Description:**
> An important and critical phase of the data-science process is data collection. Social network applications such as Twitter and Facebook collect enormous amount of data contributed by their numerous and prolific user. For other businesses such as Amazon and NYTimes data is a significant and valuable byproduct of their main business. Sometimes the data that needs to be collected is not in a specific format but is available as a web page content. In this case, typically a web crawler is used to crawl the web (pages) and scrape the data from these web pages and extract the information needed. Data generating organizations have realized the need to share at least a subset of their data with users interested in developing applications. An API offers a method for one or two way communication among software(as well as hardware) components as long as they carry the right credentials. These credentials for authentication for programmatic access is defined by another standard OAuth(Open Authentication) delegation protocol[6] or API key in some case as in NYTimes data access [7].We will collect data about from at least two sources, one opinion-based social media in twitter, and research data in New York Times, for the same topic or key phrase. Process the two data sets collected individually using classical big data methods. Compare the outcomes using popular visualization methods.

### Phase 1 
Choose a topic of current interest to people in the USA. Something that is in the news. Use the topic as the key word or phrase to aggregate tweets and news articles about the topic for the same period. Use Twitter API, NYTimes API, and Common Crawl on espn.com, bleacherreport.com, cbssports.com, foxsports.com, and sportingnews.com.

### Phase 2
Import the VM appliance for Hadoop infrastructure and test the basic commands with the sample data provided.

### Phase 3 
Load the data aggregated in Phase 1 into the VM, two directories: TwitterData and NewsData. Each directory can have many files of data.

### Phase 4 
Code and execute MapReduce word count on each of the data sets using AWS Elastic MapReduce (EMR) and S3. Map will clean and parse the data sets into words, remove stop words, and reduce will count the useful words. Twitterdata -> TwitterWords and NewsData -> NewsWords. Review and visually compare the output for representative words about the topic. You may have to change the search word, obtain new sets of data that may comparable sets of output words. You can use Python or java for your coding language.

### Phase 5
Visualize each of the outputs using d3.js and on a simple web page that you create for this lab. 

### Phase 6
Now repeat for larger data set collected over week.

### Phase 7
Now design a web page and feed the results by embedding d3.js code (with replaceable worldclouds) in it, finalizing the display of results. In fact, you should be able to create interactive data product! Input a search topic, we will return the word cloud associated with that topic!

### Phase 8
We want to drill deeper into our analysis. Using the smallestdata sets you collected in Phase 1, analyze each set (Twitter and News) word co-occurrence for only the top ten words. Assume context for co-occurrence is the “tweet” in the case of TwitterData, and the paragraph of the news article in the NewsData.Your “map” function emits<word, co-occurring word> and your “reduce” function should collate the co-occurrences for the top ten words and output them in a suitable format. 
