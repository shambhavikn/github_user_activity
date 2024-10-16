import requests
import sys


def git_event(username):
    #username='kamranahmedse'
    url=f'https://api.github.com/users/{username}/events'
    response=requests.get(url)

    if response.status_code==200:
        events=response.json()
        events[0]
        for event in events:
            #print(event,end='\n\n')
            if event['type']=='WatchEvent':
                print(f'Starred {event["repo"]["name"]}')
            elif event['type']=='PushEvent':
                print(f'Pushed commits into {event["repo"]["name"]}')
            elif event['type']=='PullRequestEvent':
                print(f'created pull request {event["payload"]["number"]} with action {event["payload"]["action"]}')
            elif event['type']=='PullRequestReviewEvent':
                print(f'reviewed pull request {event["payload"]["pull_request"]["number"]} with action {event["payload"]["action"]}')
            elif event['type']=='IssuesEvent':
                print(f'Created issue {event["payload"]["issue"]["number"]} with action {event["payload"]["action"]}')
            elif event['type']=='IssuesCommentEvent':
                print(f'Commented on issue {event["payload"]["issue"]["number"]}')
            elif event['type']=='CreateEvent':
                print(f'Created event {event["payload"]["ref_type"]} {event["payload"]["ref"]}, {event["payload"]["description"]}')
            else:
                print(f'{event["type"]}')
    
    else:
        print(f"Error fetching events for {username}: {response.status_code}")
        
        

def main():
    if len(sys.argv)>1:
        git_event(sys.argv[1])
    else:
        print('Not the correct format in command line')

if __name__=='__main__':
    main()
