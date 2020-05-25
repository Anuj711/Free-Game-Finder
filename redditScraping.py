import praw
import datetime
import smtplib, ssl
from email.message import EmailMessage


def main():
    reddit = praw.Reddit(client_id="EX7gKNMra7fgpg",
                         client_secret="-zWRsNlfw6wlSJS-t0pOnV1VPhQ",
                         password="$15@Anuj",
                         user_agent="Scraping",
                         username="warrior21q")
    free_Games = reddit.subreddit("FreeGameFindings").new(limit=5)

    # Message we are trying to send
    message = ""
    mainGames = {}
    mainGames2 = []
    mainGamesCounter = 0

    # Iterates through each post in the free games subreddit
    for post in free_Games:
        title = post.title
        #.encode('utf-8')
        print(title)
        date = int(post.created_utc)
        convertedDate = datetime.datetime.utcfromtimestamp(date)
        if "GOG" in post.title or "Epic" in post.title or "Humble" in post.title or "Uplay" in post.title or "UPLAY" in post.title or "uplay" in post.title:
            mainGamesCounter += 1
            mainGames2.append(title)
            # message += str(title)
        print(convertedDate, '\n')

    message+=("\nMAIN SITES THAT I CHECK")
    if mainGamesCounter == 0:
        message += ("\nNo games from main sites")
    else:
        message += ("\nGames are from main sites")
        for game in mainGames2:
            message += ('\n')
            message += game
        message.encode('utf-8')

    print(message)

    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "anujshukla01@gmail.com"
    receiver_email = "anujshukla01@gmail.com"
    password = "$19@Anuj"

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


if __name__ == '__main__':
    main()
