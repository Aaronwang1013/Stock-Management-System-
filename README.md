# Stock Management System


# Function
- trade record

- Backtesting 

- Forwardtesting


# Content 

- Market sentiment
- International envents
- Financial envents
- celebrity opinion


# Requirement
- SQL
- Crawler
- Data visualization

------------------------------------
## More detailed.

Three main functions

1. Web crawler & visualization
    - Web crawler module -> load data into database
        1. Price & volume in the past
        3. Investors trade info
        4. Technical indicators (TI)
    - Raw data ETL Module
        1. Pandas & SQL
    - Visualization module (matplotlib or ggplot or others)
        1. price changes
        2. Investors
        3. TI visualization add-on
    - Website framework module: deploy on Heroku/AWS?
        1. Front-end：Html、CSS、React
        2. back-end：Django
    - Database schema
2. Backtesting/Predicting
    - Ready-to-use modules by others & their preformance
    - Developing our own models
        1. LSTM model(one kind of RNN)
        2. Other ML/DL model
3. Keywords web crawler and content analysis
    - Topics
        1. Market sentiment
        2. International envents
        3. Financial envents
        4. celebrity opinion
    - Word art add-on (just for fun)
    - Sentiment analysis/visualization for single/multiple stock
        1. eng/ch NLP
        2. ML
