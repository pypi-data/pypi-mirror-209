# spider-nest
Tools to pull text data from github, slack, website, stackoverflow, etc.

## Components
### gitpump
Fetch github data, including repos, issues, discussions, trendings. Requires github account tokens.

### slackpump
Fetch slack messages of a workspace. Requires slack bot token.

### stackpump
Fetch questions/answers from stackoverflow by web parser

### web2markdown
Get web pages and parse text content to markdown content.

## From source code
```commandline
git clone git@github.com:yhmo/spider-nest.git
cd spider-nest
pip3 install -r ./requirements.txt
```

## Installation
```commandline
pip3 install spider-nest
```

## Requirement
python >= 3.7

## How to run examples
### To run the examples of gitpump, follow the steps:
1. create a github personal token by following [this guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
2. create a text file `token_github.txt` under the examples folder
3. put some github tokens into the `token_github.txt`, no delimiter, one line for each token
4. now you can run examples `example_github_xxx.py`

### To run the example of example_slack_xxx.py
1. create a slack bot, bind the bot to a workspace, get the token
2. create a text file `token_slack.txt` under the examples folder
3. put the bot token into the `token_slack.txt`
4. now you can run examples `example_slack_xxx.py`

### You can run other examples without specific setting


